from sqlalchemy import DateTime, func, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from geoalchemy2 import Geometry
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from datetime import datetime
from noise.geo import SRID_FLAT, CACHE_DIST_TRESHOLD, Point
from typing import Callable, Self, Awaitable

SRID_CACHE = SRID_FLAT


class CacheBase(DeclarativeBase):
    __version__ = 0
    __threshold__ = CACHE_DIST_TRESHOLD

    id: Mapped[int] = mapped_column(primary_key=True)
    point: Mapped[Geometry] = mapped_column(Geometry("POINT", srid=SRID_CACHE))

    time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    version: Mapped[int] = mapped_column() # or else it wont get filtered in to_dict()

    async def with_cache(
        self,
        f: Callable[[], Awaitable[Self | None]],
        pt: Point,
        sm: async_sessionmaker[AsyncSession],
    ) -> Self | None:
        wkt = pt.with_srid(SRID_CACHE).to_wkt()
        async with sm() as s:
            q = (
                select(type(self))
                .where(type(self).point.ST_Distance(wkt) < self.__threshold__)
                .limit(1)
            )

            db_res = await s.execute(q)
            hit = db_res.scalar_one_or_none()

        if hit is not None:
            return hit

        data = await f()

        if data is None:
            return None

        data.point = wkt  # type: ignore
        data.version = self.__version__

        async with sm() as s:
            s.add(data)
            await s.commit()

        return data

    def to_dict(self):
        return {
            c.name: getattr(self, c.name)
            for c in self.__table__.columns
            if not hasattr(CacheBase(), c.name)
        }
