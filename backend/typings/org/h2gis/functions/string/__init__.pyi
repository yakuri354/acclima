
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.h2gis.api
import typing



class HexToVarBinary(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @staticmethod
    def toVarBinary(string: str) -> typing.MutableSequence[int]: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.functions.string")``.

    HexToVarBinary: typing.Type[HexToVarBinary]
