from aiohttp import ClientSession
from config import WAQI_TOKEN, OWM_TOKEN
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from noise.geo import Point, SRID_ANGLE
from cache import CacheBase

AIR_VERSION = 1


# TODO caching
class AirResult(CacheBase):
    __tablename__ = "air_cache"
    __version__ = 1
    __threshold__ = 1000  # m

    aqi: Mapped[float]
    components: Mapped[dict[str, float]] = mapped_column(JSONB)

    def score(self) -> float:
        return (5 - self.aqi) * 0.25


async def air_data(lat: float, lng: float, s: ClientSession) -> AirResult:
    data = (await fetch_owm(lat, lng, s))["list"][0]
    return AirResult(aqi=data["main"]["aqi"], components=data["components"])


async def air_data_cached(
    lat: float, lng: float, s: ClientSession, sm: async_sessionmaker[AsyncSession]
):
    pt = Point(lat, lng, SRID_ANGLE)

    return await AirResult().with_cache(lambda: air_data(lat, lng, s), pt, sm)


async def fetch_waqi(lat: float, lng: float, s: ClientSession):
    async with s.get(
        f"https://api.waqi.info/feed/geo:{lat};{lng}?token={WAQI_TOKEN}"
    ) as r:
        return await r.json()


async def fetch_owm(lat: float, lng: float, s: ClientSession):
    async with s.get(
        f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lng}&appid={OWM_TOKEN}"
    ) as r:
        return await r.json()
