
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.sql
import jpype
import org.h2.api
import org.h2gis.api
import org.locationtech.jts.geom
import typing



class ST_Accum(org.h2gis.api.AbstractFunction, org.h2.api.Aggregate):
    def __init__(self): ...
    def add(self, object: typing.Any) -> None: ...
    def getInternalType(self, intArray: typing.Union[typing.List[int], jpype.JArray]) -> int: ...
    def getResult(self) -> org.locationtech.jts.geom.GeometryCollection: ...
    def init(self, connection: java.sql.Connection) -> None: ...

class ST_LineMerge(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @staticmethod
    def merge(geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...

class ST_Collect(ST_Accum):
    def __init__(self): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.functions.spatial.aggregate")``.

    ST_Accum: typing.Type[ST_Accum]
    ST_Collect: typing.Type[ST_Collect]
    ST_LineMerge: typing.Type[ST_LineMerge]
