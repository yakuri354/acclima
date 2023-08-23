from dataclasses import dataclass
from aiohttp import ClientSession
from asyncio import gather
# from noise.cache import compute_noise_cached as noise_data
from noise.cache import _compute_noise_no_cache as noise_data
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from util import w_avg
from air import owm_data
from light import lightpollutionmap_data


@dataclass
class ScoreReport: # each score in [0; 1]
    air: float
    light: float
    noise: float | None

    def overall_score(self):
        return w_avg((self.air, 15), (self.light, 5), (self.noise, 10) if self.noise else (0, 0))


async def get_scores(lat: float, lng: float, s: ClientSession, db_sm: async_sessionmaker[AsyncSession]):
    data = await gather(
        owm_data(lat, lng, s),
        lightpollutionmap_data(lat, lng, s),
        noise_data(lat, lng, s, db_sm)
    )

    return ScoreReport(
        (5 - (data[0])["list"][0]["main"]["aqi"]) * 0.25,
        data[1].score() or 0.5,
        data[2].score() if data[2] else None
    )
