
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.h2gis.api
import org.locationtech.jts.geom
import typing



class ST_PrecisionReducer(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @staticmethod
    def precisionReducer(geometry: org.locationtech.jts.geom.Geometry, int: int) -> org.locationtech.jts.geom.Geometry: ...
    @staticmethod
    def scaleFactorForDecimalPlaces(int: int) -> float: ...

class ST_Simplify(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @staticmethod
    def simplify(geometry: org.locationtech.jts.geom.Geometry, double: float) -> org.locationtech.jts.geom.Geometry: ...

class ST_SimplifyPreserveTopology(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @staticmethod
    def simplyPreserve(geometry: org.locationtech.jts.geom.Geometry, double: float) -> org.locationtech.jts.geom.Geometry: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.functions.spatial.generalize")``.

    ST_PrecisionReducer: typing.Type[ST_PrecisionReducer]
    ST_Simplify: typing.Type[ST_Simplify]
    ST_SimplifyPreserveTopology: typing.Type[ST_SimplifyPreserveTopology]
