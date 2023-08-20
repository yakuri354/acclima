import textwrap
import time
from aiohttp import ClientSession
import groovy
import os
import db
import shutil
from geo import *
from typing import Any
from dataclasses import dataclass
import geopy.distance
from org.h2gis.functions.spatial.create import ST_MakePoint
from org.h2gis.functions.spatial.crs import ST_SetSRID
from org.locationtech.jts.geom import Point as JPoint
from org.h2gis.functions.spatial.buffer import ST_Buffer
from java.lang import Integer, Double
from decimal import Decimal

def dbg(*a):
    print(*a)

OVERPASS_URL = "https://overpass-api.de/api/interpreter"
# OVERPASS_TAGS = ["building", "highway", "aeroway", "amenity", "landcover", "landuse", "leisure", "natural", "water", "waterway"]
# FIXME 1
OVERPASS_TAGS = ["building", "highway"]
AREA_RADIUS = 1000 # m

MAX_DIST = 1000 # m
RECEIVER_BUFFER_SIZE = 20.0 # m

# hardcoded in noisemodelling
BUILDINGS_TABLE = "BUILDINGS"
ROADS_TABLE = "ROADS"
GROUND_TABLE = "GROUND"
LW_ROADS_TABLE = "LW_ROADS"
RECEIVERS_TABLE = "RECEIVERS"

LDEN_GEOM_TABLE = "LDEN_GEOM"
LDAY_GEOM_TABLE = "LDAY_GEOM"
LEVENING_GEOM_TABLE = "LEVENING_GEOM"
LNIGHT_GEOM_TABLE = "LNIGHT_GEOM"

def avg(it):
    return sum(it) / len(it)

def percentile(it, p):
    return sorted(it)[int(len(it) * p)]
    
# FIXME govnocode
def jdec2py(x):
    return Decimal(str(x.toPlainString()))

def overpass_query(pt: Point, r: float):
    p2 = pt.with_srid(OSM_SRID)
    way_filter = "\n".join([
      f"way[{tag}](around:{r},{p2.x},{p2.y});" for tag in OVERPASS_TAGS
    ])
    q = f"""(
        {way_filter}
    );
    out meta;
    >;
    out meta qt;
    """
    return textwrap.dedent(q)
    
#     return textwrap.dedent(q)
# def overpass_query(poly: list[Point]):
#     coords = ",".join([str(x) for p in poly for x in [p.getX(), p.getY()]])
#     way_filter = "\n".join([
#       f"way[{tag}]({coords});" for tag in OVERPASS_TAGS
#     ])
#     q = f"""(
#         {way_filter}
#     );
#     out meta;
#     >;
#     out meta qt;
#     """
    
#     return textwrap.dedent(q)

# def approx_circle(pt: Point, r: float, n: int) -> list[Point]:
#     dist = geopy.distance.distance(kilometers=r)

#     return [dist.destination(geopy.Point(), x * (360 / n)) for x in range(n)]

@dataclass
class NoiseData:
    laeq_day: Decimal
    laeq_evening: Decimal
    laeq_night: Decimal
    laeq_den: Decimal

# FIXME govnocode
class NoiseComputation:
    def __init__(self, pt: Point, session: ClientSession) -> None:
        self.cid = (str(time.time_ns()) + '0' * 20)[:20] # govnocode
        self.sess = session
        self.pt = pt
        self.db_pt = pt.with_srid(DB_SRID).to_java()
        self.tmp_file = f"/tmp/osm_{self.cid}.osm"
        self.db_file = f"/tmp/db_{self.cid}"
        
    async def groovy_invoke(self, script: str, data: dict[str, Any]) -> Any:
        with await self.db_conn() as conn:
            return await groovy.invoke(script, conn, data)

    async def import_osm(self):
        # TODO fix ground import
        await self.groovy_invoke("Import_And_Export/Import_OSM", {
            "pathFile": self.tmp_file,
            "targetSRID": DB_SRID,
            "removeTunnels": True,
            "ignoreGround": True,
            "cid": self.cid
        })

    async def fetch_map(self):
        query = overpass_query(self.pt, AREA_RADIUS)
        
        async with self.sess.get(OVERPASS_URL, params={"data": query}) as resp:
            with open(self.tmp_file, 'wb') as fd:
                sz = 0
                async for chunk in resp.content.iter_any():
                    sz += len(chunk)
                    dbg("got ", sz)
                    fd.write(chunk)
        
    async def db_conn(self):
        if os.path.exists(self.db_file):
            shutil.rmtree(self.db_file)

        os.makedirs(self.db_file)
        
        return await db.new_h2gis_conn(self.db_file)
        
    async def get_building(self):
        with await self.db_conn() as conn:
            # fuck h2
            res = await db.query_all(conn, f"""
                with
                    dist as (select min(ST_Length(ST_ShortestLine(?, the_geom))) from {BUILDINGS_TABLE})
                select * from {BUILDINGS_TABLE} where 
                    exists (select * from dist)
                    and (select * from dist) < ?
                    and ST_Length(ST_ShortestLine(?, the_geom)) <= (select * from dist) limit 1
            """, [self.db_pt, MAX_DIST, self.db_pt])
            
            if len(res) > 0:
                return res[0]["THE_GEOM"]
            else:
                return None

    async def create_receivers_for_building(self):
        bld = await self.get_building()
        
        if bld is None:
            dbg(f"fallback point {bld}")
            with await self.db_conn() as conn:
                await db.exec_upd(conn, f"""
                    create table {RECEIVERS_TABLE} (pk integer not null AUTO_INCREMENT, the_geom geometry, build_pk integer)
                """)

                await db.exec_upd(conn, f"insert into {RECEIVERS_TABLE} values (1, ?, 1)", [self.db_pt])
        else:
            fence = ST_Buffer.buffer(bld, Double@RECEIVER_BUFFER_SIZE)
            dbg(f"invoke building_grid: {fence}")
            # await self.groovy_invoke("Receivers/Building_Grid", {
            await self.groovy_invoke("Receivers/Building_Grid", {
                "tableBuilding": BUILDINGS_TABLE,
                "sourcesTableName": ROADS_TABLE,
                "fence": fence
            })

    async def compute_road_emision(self):
        await self.groovy_invoke("NoiseModelling/Road_Emission_from_Traffic", {
            "tableRoads": ROADS_TABLE
        })
        
    async def compute_propagation(self):
        await self.groovy_invoke("NoiseModelling/Noise_level_from_source", {
            "tableBuilding": BUILDINGS_TABLE,
            "tableSources": LW_ROADS_TABLE,
            "tableReceivers": RECEIVERS_TABLE,
            # FIXME
            # "tableGroundAbs": GROUND_TABLE
        })
        
    async def get_result(self) -> NoiseData:
        # TODO fixme
        with await self.db_conn() as conn:
            lden = await db.query_all(conn, f"select * from {LDEN_GEOM_TABLE}") 
            lday = await db.query_all(conn, f"select * from {LDAY_GEOM_TABLE}")
            levening = await db.query_all(conn, f"select * from {LEVENING_GEOM_TABLE}")
            lnight = await db.query_all(conn, f"select * from {LNIGHT_GEOM_TABLE}")

        # TODO do something smarter
        # compute_lvl = lambda x: avg(y["LAEQ"] for y in x)
        compute_lvl = lambda x: jdec2py(percentile([y["LAEQ"] for y in x], 0.75))
        
        return NoiseData(
            laeq_day=compute_lvl(lday),
            laeq_evening=compute_lvl(levening),
            laeq_night=compute_lvl(lnight),
            laeq_den=compute_lvl(lden),
        )

    async def run(self) -> NoiseData:
        await self.fetch_map()
        await self.import_osm()
        await self.create_receivers_for_building()
        await self.compute_road_emision()
        await self.compute_propagation()
        
        return await self.get_result()