
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.locationtech.jts.geom
import typing



class RectangleContains:
    def __init__(self, polygon: org.locationtech.jts.geom.Polygon): ...
    @typing.overload
    def contains(self, geometry: org.locationtech.jts.geom.Geometry) -> bool: ...
    @typing.overload
    @staticmethod
    def contains(polygon: org.locationtech.jts.geom.Polygon, geometry: org.locationtech.jts.geom.Geometry) -> bool: ...

class RectangleIntersects:
    def __init__(self, polygon: org.locationtech.jts.geom.Polygon): ...
    @typing.overload
    def intersects(self, geometry: org.locationtech.jts.geom.Geometry) -> bool: ...
    @typing.overload
    @staticmethod
    def intersects(polygon: org.locationtech.jts.geom.Polygon, geometry: org.locationtech.jts.geom.Geometry) -> bool: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.locationtech.jts.operation.predicate")``.

    RectangleContains: typing.Type[RectangleContains]
    RectangleIntersects: typing.Type[RectangleIntersects]
