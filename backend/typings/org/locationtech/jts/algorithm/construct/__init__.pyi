
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.locationtech.jts.geom
import typing



class LargestEmptyCircle:
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry, double: float): ...
    @typing.overload
    def getCenter(self) -> org.locationtech.jts.geom.Point: ...
    @typing.overload
    @staticmethod
    def getCenter(geometry: org.locationtech.jts.geom.Geometry, double: float) -> org.locationtech.jts.geom.Point: ...
    @typing.overload
    def getRadiusLine(self) -> org.locationtech.jts.geom.LineString: ...
    @typing.overload
    @staticmethod
    def getRadiusLine(geometry: org.locationtech.jts.geom.Geometry, double: float) -> org.locationtech.jts.geom.LineString: ...
    def getRadiusPoint(self) -> org.locationtech.jts.geom.Point: ...

class MaximumInscribedCircle:
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry, double: float): ...
    @typing.overload
    def getCenter(self) -> org.locationtech.jts.geom.Point: ...
    @typing.overload
    @staticmethod
    def getCenter(geometry: org.locationtech.jts.geom.Geometry, double: float) -> org.locationtech.jts.geom.Point: ...
    @typing.overload
    def getRadiusLine(self) -> org.locationtech.jts.geom.LineString: ...
    @typing.overload
    @staticmethod
    def getRadiusLine(geometry: org.locationtech.jts.geom.Geometry, double: float) -> org.locationtech.jts.geom.LineString: ...
    def getRadiusPoint(self) -> org.locationtech.jts.geom.Point: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.locationtech.jts.algorithm.construct")``.

    LargestEmptyCircle: typing.Type[LargestEmptyCircle]
    MaximumInscribedCircle: typing.Type[MaximumInscribedCircle]
