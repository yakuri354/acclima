
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.sql
import org.h2.value
import org.h2gis.api
import org.locationtech.jts.geom
import org.locationtech.jts.index.strtree
import typing



class ST_Drape(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    @staticmethod
    def drape(geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...
    @staticmethod
    def drapeLineString(lineString: org.locationtech.jts.geom.LineString, geometry: org.locationtech.jts.geom.Geometry, sTRtree: org.locationtech.jts.index.strtree.STRtree) -> org.locationtech.jts.geom.Geometry: ...
    @staticmethod
    def drapeMultiLineString(multiLineString: org.locationtech.jts.geom.MultiLineString, geometry: org.locationtech.jts.geom.Geometry, sTRtree: org.locationtech.jts.index.strtree.STRtree) -> org.locationtech.jts.geom.Geometry: ...
    @staticmethod
    def drapeMultiPolygon(multiPolygon: org.locationtech.jts.geom.MultiPolygon, geometry: org.locationtech.jts.geom.Geometry, sTRtree: org.locationtech.jts.index.strtree.STRtree) -> org.locationtech.jts.geom.Geometry: ...
    @staticmethod
    def drapePoint(geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry, sTRtree: org.locationtech.jts.index.strtree.STRtree) -> org.locationtech.jts.geom.Geometry: ...
    @staticmethod
    def drapePoints(geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry, sTRtree: org.locationtech.jts.index.strtree.STRtree) -> org.locationtech.jts.geom.Geometry: ...
    @staticmethod
    def drapePolygon(polygon: org.locationtech.jts.geom.Polygon, geometry: org.locationtech.jts.geom.Geometry, sTRtree: org.locationtech.jts.index.strtree.STRtree) -> org.locationtech.jts.geom.Polygon: ...
    def getJavaStaticMethod(self) -> str: ...
    @staticmethod
    def lineMerge(geometry: org.locationtech.jts.geom.Geometry, geometryFactory: org.locationtech.jts.geom.GeometryFactory) -> org.locationtech.jts.geom.Geometry: ...

class ST_TriangleAspect(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    @staticmethod
    def computeAspect(geometry: org.locationtech.jts.geom.Geometry) -> float: ...
    def getJavaStaticMethod(self) -> str: ...
    @staticmethod
    def measureFromNorth(double: float) -> float: ...

class ST_TriangleContouring(org.h2gis.api.DeterministicScalarFunction):
    ISO_FIELD_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @staticmethod
    def triangleContouring(connection: java.sql.Connection, string: str, *value: org.h2.value.Value) -> java.sql.ResultSet: ...

class ST_TriangleDirection(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    @staticmethod
    def computeDirection(geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.LineString: ...
    def getJavaStaticMethod(self) -> str: ...

class ST_TriangleSlope(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    @staticmethod
    def computeSlope(geometry: org.locationtech.jts.geom.Geometry) -> float: ...
    def getJavaStaticMethod(self) -> str: ...

class TINFeatureFactory:
    EPSILON: typing.ClassVar[float] = ...
    @staticmethod
    def createTriangle(geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Triangle: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.functions.spatial.topography")``.

    ST_Drape: typing.Type[ST_Drape]
    ST_TriangleAspect: typing.Type[ST_TriangleAspect]
    ST_TriangleContouring: typing.Type[ST_TriangleContouring]
    ST_TriangleDirection: typing.Type[ST_TriangleDirection]
    ST_TriangleSlope: typing.Type[ST_TriangleSlope]
    TINFeatureFactory: typing.Type[TINFeatureFactory]
