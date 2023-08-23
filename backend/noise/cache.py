from geoalchemy2 import Geometry
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Double, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from aiohttp import ClientSession

from orm import Base

from .geo import Point
from .const import SRID_CACHE, SRID_ANGLE, NOISE_ALG_VERSION, CACHE_DIST_TRESHOLD
from .comp import NoiseComputation, NoiseData

class NoiseCompCache(Base):
    __tablename__ = "noise_cache"

    point: Mapped[Geometry] = mapped_column(Geometry("POINT", srid=SRID_CACHE))
    
    laeq_day: Mapped[float] = mapped_column(Double())
    laeq_evening: Mapped[float] = mapped_column(Double())
    laeq_night: Mapped[float] = mapped_column(Double())
    laeq_den: Mapped[float] = mapped_column(Double())
    
    version: Mapped[int] = mapped_column(default=NOISE_ALG_VERSION)
    
    def to_noise_data(self):
        return NoiseData(
            self.laeq_day,
            self.laeq_evening,
            self.laeq_night,
            self.laeq_den
        )
        
    @staticmethod
    def from_noise_data(point: str, nd: NoiseData):
        return NoiseCompCache(
            point=point,
            laeq_day=nd.laeq_day,
            laeq_evening=nd.laeq_evening,
            laeq_night=nd.laeq_night,
            laeq_den=nd.laeq_den
        )

class CachedNoiseComp(NoiseComputation):
    async def run(self, sm: async_sessionmaker[AsyncSession]) -> NoiseData | None:
        db_pt = self.pt.with_srid(SRID_CACHE).to_wkt()
        async with sm() as s:
            q = select(NoiseCompCache).where(
                NoiseCompCache.point.ST_Distance(db_pt) < CACHE_DIST_TRESHOLD
            ).limit(1)
            
            db_res = await s.execute(q)
            hit = db_res.scalar_one_or_none()

        if hit is None:
            data = await super().run()
            if data is None:
                return None
            async with sm() as s:
                s.add(NoiseCompCache.from_noise_data(db_pt, data))
                await s.commit()
            return data
        else:
            return hit.to_noise_data()

async def compute_noise_cached(lat: float, lng: float, s: ClientSession, sm: async_sessionmaker[AsyncSession]) -> NoiseData | None:
    pt = Point(lat, lng, SRID_ANGLE)
    comp = CachedNoiseComp(pt, s)
    return await comp.run(sm)

async def _compute_noise_no_cache(lat: float, lng: float, s: ClientSession, sm: async_sessionmaker[AsyncSession]):
    pt = Point(lat, lng, SRID_ANGLE)
    comp = NoiseComputation(pt, s)
    return await comp.run()
    