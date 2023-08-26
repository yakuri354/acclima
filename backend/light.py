from dataclasses import dataclass
import base64
from aiohttp import ClientSession
from datetime import datetime, timezone
from sqlalchemy import Double
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy.dialects.postgresql import ARRAY

from cache import CacheBase
from noise.geo import Point, SRID_ANGLE


class LightData(CacheBase):
    __tablename__ = "light_cache"
    __version__ = 1
    __threshold__ = 1000  # m

    history: Mapped[list[float]] = mapped_column(ARRAY(Double))
    elevation: Mapped[float] = mapped_column(Double)

    @staticmethod
    def from_api(response: str):
        data, elev = response.split(",")
        return LightData(
            history=[float(x) for x in data.split(";")], elevation=float(elev)
        )

    def score(self) -> float | None:
        def _calc(l: list, weight: float) -> float:
            if len(l) == 0:
                return 0
            return l[-1] * weight + _calc(l[:-1], weight / 2)

        f_his = [min(x, 150) / 150 for x in self.history if x != 0]
        if len(f_his) == 0:
            return None
        return _calc(f_his, 0.5)


async def lightpollutionmap_data(lat: float, lng: float, s: ClientSession) -> LightData:
    key = base64.b64encode(
        (
            str(int(datetime.now(timezone.utc).timestamp() * 1000)) + ";isuckdicks:)"
        ).encode("ascii")
    ).decode("utf-8")

    headers = {
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        # 'Cookie': 'ASP.NET_SessionId=F5606A7BA4779883278FA318',
        "Referer": "https://www.lightpollutionmap.info/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Brave";v="110"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
    }

    async with s.get(
        f"https://www.lightpollutionmap.info/QueryRaster/?qk={key}&ql=viirs_2021&qt=point_t&qd={lng},{lat}",
        headers=headers,
    ) as r:
        return LightData.from_api(await r.text())


async def light_data_cached(
    lat: float, lng: float, s: ClientSession, sm: async_sessionmaker[AsyncSession]
):
    pt = Point(lat, lng, SRID_ANGLE)
    return await LightData().with_cache(
        lambda: lightpollutionmap_data(lat, lng, s), pt, sm
    )
