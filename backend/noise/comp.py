import time
from aiohttp import ClientSession
import os
import shutil
from typing import Any
from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import Double as sqlDouble
import aiofiles.os

from . import groovy

from org.h2gis.functions.spatial.buffer import ST_Buffer
from java.lang import Double

from . import h2db
from .geo import *
from .overpass import overpass_fetch
from .const import *
from util import percentile, bounds
from logging import debug, info, warn, error
from cache import CacheBase
from task import spawn_task


# FIXME govnocode
def j_float2py(x):
    return float(str(x.toPlainString()))


class NoiseData(CacheBase):
    __tablename__ = "noise_cache"
    __threshold__ = CACHE_DIST_TRESHOLD
    __version__ = 1

    laeq_day: Mapped[float] = mapped_column(sqlDouble())
    laeq_evening: Mapped[float] = mapped_column(sqlDouble())
    laeq_night: Mapped[float] = mapped_column(sqlDouble())
    laeq_den: Mapped[float] = mapped_column(sqlDouble())

    def score(self):
        return 1.0 - bounds(0.0, (self.laeq_den - 35) / 45, 1.0)

    @staticmethod
    def zero():
        return NoiseData(laeq_day=0.0, laeq_evening=0.0, laeq_night=0.0, laeq_den=0.0)


# FIXME govnocode
class NoiseComputation:
    def __init__(self, pt: Point, session: ClientSession) -> None:
        self.cid = (str(time.time_ns()) + "0" * 20)[:20]  # govnocode
        self.sess = session
        self.pt = pt
        self.db_pt = pt.with_srid(SRID_H2DB).to_java()
        self.tmp_file = f"/tmp/osm_{self.cid}.osm"
        self.db_file = f"mem:{self.cid}"

    async def groovy_invoke(self, script: str, data: dict[str, Any]) -> Any:
        with await self.db_conn() as conn:
            return await groovy.invoke(script, conn, data)

    async def import_osm(self):
        # TODO fix ground import
        info(f"calling import_osm on {self.tmp_file}")
        await self.groovy_invoke(
            "Import_and_Export/Import_OSM",
            {
                "pathFile": self.tmp_file,
                "targetSRID": SRID_H2DB,
                "removeTunnels": True,
                "ignoreGround": True,
                "cid": self.cid,
            },
        )

    async def fetch_map(self):
        await overpass_fetch(self.pt, AREA_RADIUS, self.tmp_file, self.sess)

    async def db_conn(self):
        return await h2db.new_h2gis_conn(self.db_file)

    async def get_building(self):
        with await self.db_conn() as conn:
            # fuck h2
            res = await h2db.query_all(
                conn,
                f"""
                with
                    dist as (select min(ST_Length(ST_ShortestLine(?, the_geom))) from {BUILDINGS_TABLE})
                select * from {BUILDINGS_TABLE} where 
                    exists (select * from dist)
                    and (select * from dist) < ?
                    and ST_Length(ST_ShortestLine(?, the_geom)) <= (select * from dist) limit 1
            """,
                [self.db_pt, MAX_BUILDING_SEARCH_DIST, self.db_pt],
            )

            if len(res) > 0:
                return res[0]["THE_GEOM"]
            else:
                return None

    async def create_receivers_for_building(self):
        bld = await self.get_building()

        if bld is None:
            debug(f"fallback point {bld}")
            with await self.db_conn() as conn:
                await h2db.exec_upd(
                    conn,
                    f"""
                    create table {RECEIVERS_TABLE} (pk integer not null AUTO_INCREMENT, the_geom geometry, build_pk integer)
                """,
                )

                await h2db.exec_upd(
                    conn,
                    f"insert into {RECEIVERS_TABLE} values (1, ?, 1)",
                    [self.db_pt],
                )
        else:
            rcbs = Double @ RECEIVER_BUFFER_SIZE  # type: ignore
            fence = ST_Buffer.buffer(bld, rcbs)

            debug(f"invoke building_grid: {fence}")

            await self.groovy_invoke(
                "Receivers/Building_Grid",
                {
                    "tableBuilding": BUILDINGS_TABLE,
                    "sourcesTableName": ROADS_TABLE,
                    "fence": fence,
                },
            )

    async def compute_road_emision(self):
        await self.groovy_invoke(
            "NoiseModelling/Road_Emission_from_Traffic", {"tableRoads": ROADS_TABLE}
        )

    async def compute_propagation(self):
        await self.groovy_invoke(
            "NoiseModelling/Noise_level_from_source",
            {
                "tableBuilding": BUILDINGS_TABLE,
                "tableSources": LW_ROADS_TABLE,
                "tableReceivers": RECEIVERS_TABLE,
                # FIXME
                # "tableGroundAbs": GROUND_TABLE
            },
        )

    async def get_result(self) -> NoiseData:
        # TODO fixme
        with await self.db_conn() as conn:
            lden = await h2db.query_all(conn, f"select * from {LDEN_GEOM_TABLE}")
            lday = await h2db.query_all(conn, f"select * from {LDAY_GEOM_TABLE}")
            levening = await h2db.query_all(
                conn, f"select * from {LEVENING_GEOM_TABLE}"
            )
            lnight = await h2db.query_all(conn, f"select * from {LNIGHT_GEOM_TABLE}")

        # TODO do something smarter
        # compute_lvl = lambda x: avg(y["LAEQ"] for y in x)
        compute_lvl = lambda x: j_float2py(percentile([y["LAEQ"] for y in x], 0.75))

        return NoiseData(
            laeq_day=compute_lvl(lday),
            laeq_evening=compute_lvl(levening),
            laeq_night=compute_lvl(lnight),
            laeq_den=compute_lvl(lden),
        )

    async def run(self) -> NoiseData | None:
        await self.fetch_map()
        await self.import_osm()

        with await self.db_conn() as c:
            cr = await h2db.query_all(c, f"select count(*) as c from {ROADS_TABLE}")
            cb = await h2db.query_all(c, f"select count(*) as c from {BUILDINGS_TABLE}")

        if cr[0]["C"] == 0 or cb[0]["C"] == 0:
            return None
            # return NoiseData.null()

        await self.create_receivers_for_building()
        await self.compute_road_emision()
        await self.compute_propagation()

        return await self.get_result()
    
    async def __aenter__(self):
        self._bg_dbconn = await self.db_conn()
        return self
    
    async def __aexit__(self, _e_type, _e_val, _e_traceback):
        await h2db.exec_upd(self._bg_dbconn, "SHUTDOWN IMMEDIATELY")
        spawn_task(aiofiles.os.remove(self.tmp_file))


async def _compute_noise_no_cache(
    lat: float, lng: float, s: ClientSession, sm: async_sessionmaker[AsyncSession]
) -> NoiseData | None:
    pt = Point(lat, lng, SRID_ANGLE)
    async with NoiseComputation(pt, s) as comp:
        return await comp.run()


async def compute_noise_cached(
    lat: float, lng: float, s: ClientSession, sm: async_sessionmaker[AsyncSession]
) -> NoiseData | None:
    pt = Point(lat, lng, SRID_ANGLE)
    return await NoiseData().with_cache(
        lambda: _compute_noise_no_cache(lat, lng, s, sm), pt, sm
    )
