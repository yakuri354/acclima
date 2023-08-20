
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.locationtech.jts.geom
import typing



class Densifier:
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry): ...
    @staticmethod
    def densify(geometry: org.locationtech.jts.geom.Geometry, double: float) -> org.locationtech.jts.geom.Geometry: ...
    def getResultGeometry(self) -> org.locationtech.jts.geom.Geometry: ...
    def setDistanceTolerance(self, double: float) -> None: ...
    def setValidate(self, boolean: bool) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.locationtech.jts.densify")``.

    Densifier: typing.Type[Densifier]
