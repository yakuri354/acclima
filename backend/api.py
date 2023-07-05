from typing import Optional
from datetime import datetime, timezone
import base64
from dataclasses import dataclass
from aiohttp import ClientSession
from asyncio import gather

from secret import WAQI_TOKEN, OWM_TOKEN

def avg(*l):
    return sum(l) / len(l)

@dataclass
class ScoreReport: # each score in [0; 1]
    air: float
    light: float
    noise: float

    def overall_score(self):
        return avg(self.air ** 0.5, self.light ** 1.5, self.noise)

async def get_scores(lat: float, lng: float, s: ClientSession):
    data = await gather(
        owm_data(lat, lng, s),
        lightpollutionmap_data(lat, lng, s),
        noise_data(lat, lng)
    )

    return ScoreReport(
        (5 - (data[0])["list"][0]["main"]["aqi"]) * 0.25,
        data[1].score() or 0.5,
        data[2]
    )

async def waqi_data(lat: float, lng: float, s: ClientSession):
    async with s.get(f"https://api.waqi.info/feed/geo:{lat};{lng}?token={WAQI_TOKEN}") as r:
        return await r.json()

async def owm_data(lat: float, lng: float, s: ClientSession):
    async with s.get(f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lng}&appid={OWM_TOKEN}") as r:
        return await r.json()

async def noise_data(lat: float, lng: float):
    return 0.5

@dataclass
class LightData:
    history: list[float]
    elevation: float

    @staticmethod
    def from_api(response: str):
        data, elev = response.split(",")
        return LightData([float(x) for x in data.split(";")], float(elev))

    def score(self) -> Optional[float]:
        def _calc(l: list, weight: float) -> float:
            if len(l) == 0:
                return 0
            return l[-1] * weight + _calc(l[:-1], weight / 2);

        f_his = [min(x, 150) / 150 for x in self.history if x != 0]
        if len(f_his) == 0:
            return None
        return _calc(f_his, 0.5)

async def lightpollutionmap_data(lat: float, lng: float, s: ClientSession) -> LightData:
    key = base64.b64encode((str(int(datetime.now(timezone.utc).timestamp() * 1000)) + ';isuckdicks:)').encode('ascii')).decode('utf-8')

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        # 'Cookie': 'ASP.NET_SessionId=F5606A7BA4779883278FA318',
        'Referer': 'https://www.lightpollutionmap.info/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Brave";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }

    async with s.get(
        f'https://www.lightpollutionmap.info/QueryRaster/?qk={key}&ql=viirs_2021&qt=point_t&qd={lng},{lat}',
        headers=headers) as r:
        return LightData.from_api(await r.text())
