
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.sql
import java.util
import org.cts.op
import org.cts.registry
import org.h2gis.api
import org.locationtech.jts.geom
import typing



class EPSGTuple:
    def __init__(self, int: int, int2: int): ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...

class ST_FindUTMSRID(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    @staticmethod
    def findSRID(connection: java.sql.Connection, geometry: org.locationtech.jts.geom.Geometry) -> int: ...
    def getJavaStaticMethod(self) -> str: ...

class ST_SetSRID(org.h2gis.api.AbstractFunction, org.h2gis.api.ScalarFunction):
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @staticmethod
    def setSRID(geometry: org.locationtech.jts.geom.Geometry, integer: int) -> org.locationtech.jts.geom.Geometry: ...

class ST_Transform(org.h2gis.api.AbstractFunction, org.h2gis.api.ScalarFunction):
    def __init__(self): ...
    @staticmethod
    def ST_Transform(connection: java.sql.Connection, geometry: org.locationtech.jts.geom.Geometry, integer: int) -> org.locationtech.jts.geom.Geometry: ...
    def getJavaStaticMethod(self) -> str: ...
    class CRSTransformFilter(org.locationtech.jts.geom.CoordinateFilter):
        def __init__(self, coordinateOperation: org.cts.op.CoordinateOperation): ...
        def filter(self, coordinate: org.locationtech.jts.geom.Coordinate) -> None: ...
    class CopCache(java.util.LinkedHashMap[EPSGTuple, org.cts.op.CoordinateOperation]):
        def __init__(self, int: int): ...

class SpatialRefRegistry(org.cts.registry.AbstractProjRegistry, org.cts.registry.Registry):
    def __init__(self): ...
    def getParameters(self, string: str) -> java.util.Map[str, str]: ...
    def getRegistryName(self) -> str: ...
    def getSupportedCodes(self) -> java.util.Set[str]: ...
    def setConnection(self, connection: java.sql.Connection) -> None: ...

class UpdateGeometrySRID(org.h2gis.api.AbstractFunction, org.h2gis.api.ScalarFunction):
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def changeSRID(connection: java.sql.Connection, string: str, string2: str, int: int) -> bool: ...
    @typing.overload
    @staticmethod
    def changeSRID(connection: java.sql.Connection, string: str, string2: str, string3: str, int: int) -> bool: ...
    @typing.overload
    @staticmethod
    def changeSRID(connection: java.sql.Connection, string: str, string2: str, string3: str, string4: str, int: int) -> bool: ...
    def getJavaStaticMethod(self) -> str: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.functions.spatial.crs")``.

    EPSGTuple: typing.Type[EPSGTuple]
    ST_FindUTMSRID: typing.Type[ST_FindUTMSRID]
    ST_SetSRID: typing.Type[ST_SetSRID]
    ST_Transform: typing.Type[ST_Transform]
    SpatialRefRegistry: typing.Type[SpatialRefRegistry]
    UpdateGeometrySRID: typing.Type[UpdateGeometrySRID]