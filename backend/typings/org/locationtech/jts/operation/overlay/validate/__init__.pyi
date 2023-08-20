
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org.locationtech.jts.geom
import typing



class FuzzyPointLocator:
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry, double: float): ...
    def getLocation(self, coordinate: org.locationtech.jts.geom.Coordinate) -> int: ...

class OffsetPointGenerator:
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry): ...
    def getPoints(self, double: float) -> java.util.List: ...
    def setSidesToGenerate(self, boolean: bool, boolean2: bool) -> None: ...

class OverlayResultValidator:
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry, geometry3: org.locationtech.jts.geom.Geometry): ...
    def getInvalidLocation(self) -> org.locationtech.jts.geom.Coordinate: ...
    @typing.overload
    def isValid(self, int: int) -> bool: ...
    @typing.overload
    @staticmethod
    def isValid(geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry, int: int, geometry3: org.locationtech.jts.geom.Geometry) -> bool: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.locationtech.jts.operation.overlay.validate")``.

    FuzzyPointLocator: typing.Type[FuzzyPointLocator]
    OffsetPointGenerator: typing.Type[OffsetPointGenerator]
    OverlayResultValidator: typing.Type[OverlayResultValidator]
