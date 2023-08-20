
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.h2gis.api
import org.locationtech.jts.geom
import typing



class ST_ConvexHull(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    @staticmethod
    def convexHull(geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...
    def getJavaStaticMethod(self) -> str: ...

class ST_Difference(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def difference(geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def difference(geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry, double: float) -> org.locationtech.jts.geom.Geometry: ...
    def getJavaStaticMethod(self) -> str: ...

class ST_Intersection(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @typing.overload
    @staticmethod
    def intersection(geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def intersection(geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry, double: float) -> org.locationtech.jts.geom.Geometry: ...

class ST_SymDifference(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @typing.overload
    @staticmethod
    def symDifference(geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def symDifference(geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry, double: float) -> org.locationtech.jts.geom.Geometry: ...

class ST_Union(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @typing.overload
    @staticmethod
    def union(geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def union(geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.functions.spatial.operators")``.

    ST_ConvexHull: typing.Type[ST_ConvexHull]
    ST_Difference: typing.Type[ST_Difference]
    ST_Intersection: typing.Type[ST_Intersection]
    ST_SymDifference: typing.Type[ST_SymDifference]
    ST_Union: typing.Type[ST_Union]
