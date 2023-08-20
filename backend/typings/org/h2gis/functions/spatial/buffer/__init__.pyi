
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.h2.value
import org.h2gis.api
import org.locationtech.jts.geom
import typing



class ST_Buffer(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def buffer(geometry: org.locationtech.jts.geom.Geometry, double: float) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def buffer(geometry: org.locationtech.jts.geom.Geometry, double: float, value: org.h2.value.Value) -> org.locationtech.jts.geom.Geometry: ...
    def getJavaStaticMethod(self) -> str: ...

class ST_OffSetCurve(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @typing.overload
    @staticmethod
    def offsetCurve(geometry: org.locationtech.jts.geom.Geometry, double: float) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def offsetCurve(geometry: org.locationtech.jts.geom.Geometry, double: float, string: str) -> org.locationtech.jts.geom.Geometry: ...

class ST_RingSideBuffer(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @typing.overload
    @staticmethod
    def ringSideBuffer(geometry: org.locationtech.jts.geom.Geometry, double: float, int: int) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def ringSideBuffer(geometry: org.locationtech.jts.geom.Geometry, double: float, int: int, string: str) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def ringSideBuffer(geometry: org.locationtech.jts.geom.Geometry, double: float, int: int, string: str, boolean: bool) -> org.locationtech.jts.geom.Geometry: ...

class ST_SideBuffer(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @typing.overload
    @staticmethod
    def singleSideBuffer(geometry: org.locationtech.jts.geom.Geometry, double: float) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def singleSideBuffer(geometry: org.locationtech.jts.geom.Geometry, double: float, string: str) -> org.locationtech.jts.geom.Geometry: ...

class ST_VariableBuffer(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    @staticmethod
    def buffer(geometry: org.locationtech.jts.geom.Geometry, double: float, double2: float) -> org.locationtech.jts.geom.Geometry: ...
    def getJavaStaticMethod(self) -> str: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.functions.spatial.buffer")``.

    ST_Buffer: typing.Type[ST_Buffer]
    ST_OffSetCurve: typing.Type[ST_OffSetCurve]
    ST_RingSideBuffer: typing.Type[ST_RingSideBuffer]
    ST_SideBuffer: typing.Type[ST_SideBuffer]
    ST_VariableBuffer: typing.Type[ST_VariableBuffer]
