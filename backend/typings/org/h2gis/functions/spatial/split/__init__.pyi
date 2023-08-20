
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org.h2gis.api
import org.locationtech.jts.geom
import org.locationtech.jts.noding
import typing



class ST_LineIntersector(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    @staticmethod
    def addGeometryToSegments(geometry: org.locationtech.jts.geom.Geometry, int: int, arrayList: java.util.ArrayList[org.locationtech.jts.noding.SegmentString]) -> None: ...
    def getJavaStaticMethod(self) -> str: ...
    @staticmethod
    def getSegments(geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry) -> java.util.ArrayList[org.locationtech.jts.noding.SegmentString]: ...
    @staticmethod
    def lineIntersector(geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...

class ST_Split(org.h2gis.api.DeterministicScalarFunction):
    PRECISION: typing.ClassVar[float] = ...
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @typing.overload
    @staticmethod
    def split(geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def split(geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry, double: float) -> org.locationtech.jts.geom.Geometry: ...

class ST_SubDivide(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def divide(geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def divide(geometry: org.locationtech.jts.geom.Geometry, int: int) -> org.locationtech.jts.geom.Geometry: ...
    @staticmethod
    def filterGeom(geometry: org.locationtech.jts.geom.Geometry, int: int, stack: java.util.Stack, list: java.util.List) -> None: ...
    def getJavaStaticMethod(self) -> str: ...
    @staticmethod
    def subdivide_recursive(geometry: org.locationtech.jts.geom.Geometry, int: int) -> java.util.List[org.locationtech.jts.geom.Geometry]: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.functions.spatial.split")``.

    ST_LineIntersector: typing.Type[ST_LineIntersector]
    ST_Split: typing.Type[ST_Split]
    ST_SubDivide: typing.Type[ST_SubDivide]
