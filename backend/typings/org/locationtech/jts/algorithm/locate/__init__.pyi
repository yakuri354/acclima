
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.locationtech.jts.geom
import typing



class PointOnGeometryLocator:
    def locate(self, coordinate: org.locationtech.jts.geom.Coordinate) -> int: ...

class IndexedPointInAreaLocator(PointOnGeometryLocator):
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry): ...
    def locate(self, coordinate: org.locationtech.jts.geom.Coordinate) -> int: ...

class SimplePointInAreaLocator(PointOnGeometryLocator):
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry): ...
    @staticmethod
    def containsPointInPolygon(coordinate: org.locationtech.jts.geom.Coordinate, polygon: org.locationtech.jts.geom.Polygon) -> bool: ...
    @staticmethod
    def isContained(coordinate: org.locationtech.jts.geom.Coordinate, geometry: org.locationtech.jts.geom.Geometry) -> bool: ...
    @typing.overload
    def locate(self, coordinate: org.locationtech.jts.geom.Coordinate) -> int: ...
    @typing.overload
    @staticmethod
    def locate(coordinate: org.locationtech.jts.geom.Coordinate, geometry: org.locationtech.jts.geom.Geometry) -> int: ...
    @staticmethod
    def locatePointInPolygon(coordinate: org.locationtech.jts.geom.Coordinate, polygon: org.locationtech.jts.geom.Polygon) -> int: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.locationtech.jts.algorithm.locate")``.

    IndexedPointInAreaLocator: typing.Type[IndexedPointInAreaLocator]
    PointOnGeometryLocator: typing.Type[PointOnGeometryLocator]
    SimplePointInAreaLocator: typing.Type[SimplePointInAreaLocator]
