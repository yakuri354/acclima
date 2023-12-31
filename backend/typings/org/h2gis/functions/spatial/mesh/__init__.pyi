
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import jpype
import org.h2gis.api
import org.locationtech.jts.geom
import typing



class DelaunayData:
    def __init__(self): ...
    def get3DArea(self) -> float: ...
    def getTriangles(self) -> org.locationtech.jts.geom.MultiPolygon: ...
    def getTrianglesSides(self) -> org.locationtech.jts.geom.MultiLineString: ...
    def put(self, geometry: org.locationtech.jts.geom.Geometry, mODE: 'DelaunayData.MODE') -> None: ...
    def triangulate(self) -> None: ...
    class MODE(java.lang.Enum['DelaunayData.MODE']):
        DELAUNAY: typing.ClassVar['DelaunayData.MODE'] = ...
        CONSTRAINED: typing.ClassVar['DelaunayData.MODE'] = ...
        TESSELLATION: typing.ClassVar['DelaunayData.MODE'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'DelaunayData.MODE': ...
        @staticmethod
        def values() -> typing.MutableSequence['DelaunayData.MODE']: ...

class FullConvexHull:
    @typing.overload
    def __init__(self, coordinateArray: typing.Union[typing.List[org.locationtech.jts.geom.Coordinate], jpype.JArray], geometryFactory: org.locationtech.jts.geom.GeometryFactory): ...
    @typing.overload
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry): ...
    def getConvexHull(self) -> org.locationtech.jts.geom.Geometry: ...

class ST_ConstrainedDelaunay(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def createCDT(geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.GeometryCollection: ...
    @typing.overload
    @staticmethod
    def createCDT(geometry: org.locationtech.jts.geom.Geometry, int: int) -> org.locationtech.jts.geom.GeometryCollection: ...
    def getJavaStaticMethod(self) -> str: ...

class ST_Delaunay(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def createDT(geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.GeometryCollection: ...
    @typing.overload
    @staticmethod
    def createDT(geometry: org.locationtech.jts.geom.Geometry, int: int) -> org.locationtech.jts.geom.GeometryCollection: ...
    def getJavaStaticMethod(self) -> str: ...

class ST_Tessellate(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @staticmethod
    def tessellate(geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.MultiPolygon: ...

class ST_Voronoi(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @typing.overload
    @staticmethod
    def voronoi(geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.GeometryCollection: ...
    @typing.overload
    @staticmethod
    def voronoi(geometry: org.locationtech.jts.geom.Geometry, int: int) -> org.locationtech.jts.geom.GeometryCollection: ...
    @typing.overload
    @staticmethod
    def voronoi(geometry: org.locationtech.jts.geom.Geometry, int: int, geometry2: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.GeometryCollection: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.functions.spatial.mesh")``.

    DelaunayData: typing.Type[DelaunayData]
    FullConvexHull: typing.Type[FullConvexHull]
    ST_ConstrainedDelaunay: typing.Type[ST_ConstrainedDelaunay]
    ST_Delaunay: typing.Type[ST_Delaunay]
    ST_Tessellate: typing.Type[ST_Tessellate]
    ST_Voronoi: typing.Type[ST_Voronoi]
