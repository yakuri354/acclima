
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.locationtech.jts.geom
import typing



class GeometryExtrude:
    @typing.overload
    @staticmethod
    def extractRoof(lineString: org.locationtech.jts.geom.LineString, double: float) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def extractRoof(polygon: org.locationtech.jts.geom.Polygon, double: float) -> org.locationtech.jts.geom.Polygon: ...
    @typing.overload
    @staticmethod
    def extractWalls(lineString: org.locationtech.jts.geom.LineString, double: float) -> org.locationtech.jts.geom.MultiPolygon: ...
    @typing.overload
    @staticmethod
    def extractWalls(polygon: org.locationtech.jts.geom.Polygon, double: float) -> org.locationtech.jts.geom.MultiPolygon: ...
    @staticmethod
    def extrudeLineStringAsGeometry(lineString: org.locationtech.jts.geom.LineString, double: float) -> org.locationtech.jts.geom.GeometryCollection: ...
    @staticmethod
    def extrudePolygonAsGeometry(polygon: org.locationtech.jts.geom.Polygon, double: float) -> org.locationtech.jts.geom.GeometryCollection: ...
    class UpdateZValue(org.locationtech.jts.geom.CoordinateSequenceFilter):
        def __init__(self, double: float): ...
        def filter(self, coordinateSequence: org.locationtech.jts.geom.CoordinateSequence, int: int) -> None: ...
        def isDone(self) -> bool: ...
        def isGeometryChanged(self) -> bool: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.functions.spatial.volume")``.

    GeometryExtrude: typing.Type[GeometryExtrude]
