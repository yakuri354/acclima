
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.h2gis.api
import typing



class DoubleRange(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def createArray(double: float, double2: float) -> typing.MutableSequence[float]: ...
    @typing.overload
    @staticmethod
    def createArray(double: float, double2: float, double3: float) -> typing.MutableSequence[float]: ...
    def getJavaStaticMethod(self) -> str: ...

class H2GISversion(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @staticmethod
    def geth2gisVersion() -> str: ...

class IntegerRange(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def createArray(int: int, int2: int) -> typing.MutableSequence[int]: ...
    @typing.overload
    @staticmethod
    def createArray(int: int, int2: int, int3: int) -> typing.MutableSequence[int]: ...
    def getJavaStaticMethod(self) -> str: ...

class JTSVersion(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @staticmethod
    def getjtsVersion() -> str: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.functions.system")``.

    DoubleRange: typing.Type[DoubleRange]
    H2GISversion: typing.Type[H2GISversion]
    IntegerRange: typing.Type[IntegerRange]
    JTSVersion: typing.Type[JTSVersion]
