
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org.locationtech.jts.geom
import org.locationtech.jts.triangulate.tri
import typing



class ConstrainedDelaunayTriangulator:
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry): ...
    def getResult(self) -> org.locationtech.jts.geom.Geometry: ...
    def getTriangles(self) -> java.util.List[org.locationtech.jts.triangulate.tri.Tri]: ...
    @staticmethod
    def triangulate(geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...

class PolygonHoleJoiner:
    def __init__(self, polygon: org.locationtech.jts.geom.Polygon): ...
    def compute(self) -> typing.MutableSequence[org.locationtech.jts.geom.Coordinate]: ...
    @staticmethod
    def join(polygon: org.locationtech.jts.geom.Polygon) -> typing.MutableSequence[org.locationtech.jts.geom.Coordinate]: ...
    @staticmethod
    def joinAsPolygon(polygon: org.locationtech.jts.geom.Polygon) -> org.locationtech.jts.geom.Polygon: ...

class PolygonTriangulator:
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry): ...
    def getResult(self) -> org.locationtech.jts.geom.Geometry: ...
    def getTriangles(self) -> java.util.List[org.locationtech.jts.triangulate.tri.Tri]: ...
    @staticmethod
    def triangulate(geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.locationtech.jts.triangulate.polygon")``.

    ConstrainedDelaunayTriangulator: typing.Type[ConstrainedDelaunayTriangulator]
    PolygonHoleJoiner: typing.Type[PolygonHoleJoiner]
    PolygonTriangulator: typing.Type[PolygonTriangulator]
