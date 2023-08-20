
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.h2gis.api
import org.locationtech.jts.geom
import typing



class MakeValidOp:
    def __init__(self): ...
    def makeValid(self, geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...
    def setPreserveCoordDim(self, boolean: bool) -> 'MakeValidOp': ...
    def setPreserveDuplicateCoord(self, boolean: bool) -> 'MakeValidOp': ...
    def setPreserveGeomDim(self, boolean: bool) -> 'MakeValidOp': ...

class ST_MakeValid(org.h2gis.api.DeterministicScalarFunction):
    REMARKS: typing.ClassVar[str] = ...
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @typing.overload
    @staticmethod
    def validGeom(geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def validGeom(geometry: org.locationtech.jts.geom.Geometry, boolean: bool) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def validGeom(geometry: org.locationtech.jts.geom.Geometry, boolean: bool, boolean2: bool) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def validGeom(geometry: org.locationtech.jts.geom.Geometry, boolean: bool, boolean2: bool, boolean3: bool) -> org.locationtech.jts.geom.Geometry: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.functions.spatial.clean")``.

    MakeValidOp: typing.Type[MakeValidOp]
    ST_MakeValid: typing.Type[ST_MakeValid]
