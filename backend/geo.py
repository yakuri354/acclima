import pyproj
import groovy
from org.h2gis.functions.spatial.create import ST_MakePoint
from org.h2gis.functions.spatial.crs import ST_SetSRID
from org.locationtech.jts.geom import Point as JPoint
from org.locationtech.jts.io import WKTWriter
from java.lang import Integer
from jpype import JConversion

ANGLE = 4326 # OSM
OSM_SRID = ANGLE
FLAT = 3857
DB_SRID = FLAT
# DB_SRID = ANGLE

def geom2wkt(g) -> str:
    wkt_w = WKTWriter()
    return wkt_w.write(g)

class Point:
    def __init__(self, x: float, y: float, srid: float = FLAT) -> None:
        self.x = x
        self.y = y
        self.srid = srid
        
    def with_srid(self, srid: float):
        if self.srid == srid:
            return self
        else:
            trans = pyproj.Transformer.from_crs(f"EPSG:{self.srid}", f"EPSG:{srid}")
            pt2 = trans.transform(self.x, self.y)
            return type(self)(*pt2, srid)
        
    def to_java(self) -> JPoint:
        return JPoint@ST_SetSRID.setSRID(ST_MakePoint.createPoint(self.x, self.y), Integer@self.srid)
    
    def to_wkt(self) -> str:
        return geom2wkt(self.to_java())
    
@JConversion("org.locationtech.jts.geom.Point", instanceof=Point)
def _JPointConvert(jcls, obj):
    return obj.to_java()