
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org.locationtech.jts.geom
import typing



class LineDissolver:
    def __init__(self): ...
    @typing.overload
    def add(self, collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set]) -> None: ...
    @typing.overload
    def add(self, geometry: org.locationtech.jts.geom.Geometry) -> None: ...
    @staticmethod
    def dissolve(geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...
    def getResult(self) -> org.locationtech.jts.geom.Geometry: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.locationtech.jts.dissolve")``.

    LineDissolver: typing.Type[LineDissolver]
