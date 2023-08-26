from dataclasses import dataclass
from aiohttp import ClientSession
from asyncio import gather
from noise.comp import _compute_noise_no_cache as noise_data, compute_noise_cached as noise_data_cached
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from typing import Tuple

from util import w_avg
from air import air_data_cached
from light import light_data_cached


@dataclass
class ScoreReport:  # each score in [0; 1]
    air: float | None
    light: float | None
    noise: float | None

    def overall_score(self):
        def _null(*l):
            return [(x if x[0] else (0.0, 0.0)) for x in l]

        return w_avg(_null((self.air, 15), (self.light, 5), (self.noise, 10)))


async def get_scores(
    lat: float, lng: float, s: ClientSession, db_sm: async_sessionmaker[AsyncSession]
):
    data = await gather(
        air_data_cached(lat, lng, s, db_sm),
        light_data_cached(lat, lng, s, db_sm),
        noise_data_cached(lat, lng, s, db_sm),
    )

    return ScoreReport(
        data[0].score() if data[0] else None,
        data[1].score() if data[1] else None,
        data[2].score() if data[2] else None,
    )
