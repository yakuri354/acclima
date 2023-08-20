
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org
import org.locationtech.jts.algorithm.locate
import org.locationtech.jts.geom
import org.locationtech.jts.noding
import typing



class PreparedGeometry:
    def contains(self, geometry: org.locationtech.jts.geom.Geometry) -> bool: ...
    def containsProperly(self, geometry: org.locationtech.jts.geom.Geometry) -> bool: ...
    def coveredBy(self, geometry: org.locationtech.jts.geom.Geometry) -> bool: ...
    def covers(self, geometry: org.locationtech.jts.geom.Geometry) -> bool: ...
    def crosses(self, geometry: org.locationtech.jts.geom.Geometry) -> bool: ...
    def disjoint(self, geometry: org.locationtech.jts.geom.Geometry) -> bool: ...
    def getGeometry(self) -> org.locationtech.jts.geom.Geometry: ...
    def intersects(self, geometry: org.locationtech.jts.geom.Geometry) -> bool: ...
    def overlaps(self, geometry: org.locationtech.jts.geom.Geometry) -> bool: ...
    def touches(self, geometry: org.locationtech.jts.geom.Geometry) -> bool: ...
    def within(self, geometry: org.locationtech.jts.geom.Geometry) -> bool: ...

class PreparedGeometryFactory:
    def __init__(self): ...
    def create(self, geometry: org.locationtech.jts.geom.Geometry) -> PreparedGeometry: ...
    @staticmethod
    def prepare(geometry: org.locationtech.jts.geom.Geometry) -> PreparedGeometry: ...

class PreparedLineString(org.locationtech.jts.geom.prep.BasicPreparedGeometry):
    def __init__(self, lineal: org.locationtech.jts.geom.Lineal): ...
    def getIntersectionFinder(self) -> org.locationtech.jts.noding.FastSegmentSetIntersectionFinder: ...
    def intersects(self, geometry: org.locationtech.jts.geom.Geometry) -> bool: ...

class PreparedPoint(org.locationtech.jts.geom.prep.BasicPreparedGeometry):
    def __init__(self, puntal: org.locationtech.jts.geom.Puntal): ...
    def intersects(self, geometry: org.locationtech.jts.geom.Geometry) -> bool: ...

class PreparedPolygon(org.locationtech.jts.geom.prep.BasicPreparedGeometry):
    def __init__(self, polygonal: org.locationtech.jts.geom.Polygonal): ...
    def contains(self, geometry: org.locationtech.jts.geom.Geometry) -> bool: ...
    def containsProperly(self, geometry: org.locationtech.jts.geom.Geometry) -> bool: ...
    def covers(self, geometry: org.locationtech.jts.geom.Geometry) -> bool: ...
    def getIntersectionFinder(self) -> org.locationtech.jts.noding.FastSegmentSetIntersectionFinder: ...
    def getPointLocator(self) -> org.locationtech.jts.algorithm.locate.PointOnGeometryLocator: ...
    def intersects(self, geometry: org.locationtech.jts.geom.Geometry) -> bool: ...

class BasicPreparedGeometry: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.locationtech.jts.geom.prep")``.

    BasicPreparedGeometry: typing.Type[BasicPreparedGeometry]
    PreparedGeometry: typing.Type[PreparedGeometry]
    PreparedGeometryFactory: typing.Type[PreparedGeometryFactory]
    PreparedLineString: typing.Type[PreparedLineString]
    PreparedPoint: typing.Type[PreparedPoint]
    PreparedPolygon: typing.Type[PreparedPolygon]
