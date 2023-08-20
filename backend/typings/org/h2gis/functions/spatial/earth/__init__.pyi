
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import datetime
import java.sql
import java.util
import jpype
import org.h2gis.api
import org.locationtech.jts.geom
import org.locationtech.jts.index.strtree
import typing



class ST_GeometryShadow(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def computeShadow(geometry: org.locationtech.jts.geom.Geometry, double: float, double2: float, double3: float) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def computeShadow(geometry: org.locationtech.jts.geom.Geometry, double: float, double2: float, double3: float, boolean: bool) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def computeShadow(geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry, double: float) -> org.locationtech.jts.geom.Geometry: ...
    def getJavaStaticMethod(self) -> str: ...
    @staticmethod
    def shadowOffset(double: float, double2: float, double3: float) -> typing.MutableSequence[float]: ...

class ST_Isovist(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @typing.overload
    @staticmethod
    def isovist(geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry, double: float) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def isovist(geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry, double: float, double2: float, double3: float) -> org.locationtech.jts.geom.Geometry: ...

class ST_SunPosition(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @typing.overload
    @staticmethod
    def sunPosition(geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def sunPosition(geometry: org.locationtech.jts.geom.Geometry, timestamp: typing.Union[java.sql.Timestamp, datetime.datetime]) -> org.locationtech.jts.geom.Geometry: ...

class ST_Svf(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    @staticmethod
    def addSegments(coordinateArray: typing.Union[typing.List[org.locationtech.jts.geom.Coordinate], jpype.JArray], geometryFactory: org.locationtech.jts.geom.GeometryFactory, sTRtree: org.locationtech.jts.index.strtree.STRtree) -> None: ...
    @typing.overload
    @staticmethod
    def computeSvf(point: org.locationtech.jts.geom.Point, geometry: org.locationtech.jts.geom.Geometry, double: float, int: int) -> float: ...
    @typing.overload
    @staticmethod
    def computeSvf(point: org.locationtech.jts.geom.Point, geometry: org.locationtech.jts.geom.Geometry, double: float, int: int, int2: int) -> float: ...
    def getJavaStaticMethod(self) -> str: ...

class SunCalc:
    @staticmethod
    def getPosition(date: java.util.Date, double: float, double2: float) -> org.locationtech.jts.geom.Coordinate: ...
    @staticmethod
    def isGeographic(double: float, double2: float) -> bool: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.functions.spatial.earth")``.

    ST_GeometryShadow: typing.Type[ST_GeometryShadow]
    ST_Isovist: typing.Type[ST_Isovist]
    ST_SunPosition: typing.Type[ST_SunPosition]
    ST_Svf: typing.Type[ST_Svf]
    SunCalc: typing.Type[SunCalc]
