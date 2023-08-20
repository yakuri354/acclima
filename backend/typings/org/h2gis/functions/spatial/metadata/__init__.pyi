
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.sql
import org.h2gis.api
import typing



class FindGeometryMetadata(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    @staticmethod
    def extractMetadata(connection: java.sql.Connection, string: str, string2: str, string3: str, string4: str, string5: str, string6: str, string7: str) -> typing.MutableSequence[str]: ...
    def getJavaStaticMethod(self) -> str: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.functions.spatial.metadata")``.

    FindGeometryMetadata: typing.Type[FindGeometryMetadata]
