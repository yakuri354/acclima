
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.locationtech.jts.algorithm
import org.locationtech.jts.geom
import org.locationtech.jts.operation.buffer
import org.locationtech.jts.operation.distance
import org.locationtech.jts.operation.distance3d
import org.locationtech.jts.operation.linemerge
import org.locationtech.jts.operation.overlay
import org.locationtech.jts.operation.overlayng
import org.locationtech.jts.operation.polygonize
import org.locationtech.jts.operation.predicate
import org.locationtech.jts.operation.relate
import org.locationtech.jts.operation.union
import org.locationtech.jts.operation.valid
import typing



class BoundaryOp:
    @typing.overload
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry): ...
    @typing.overload
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry, boundaryNodeRule: org.locationtech.jts.algorithm.BoundaryNodeRule): ...
    @typing.overload
    def getBoundary(self) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def getBoundary(geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def getBoundary(geometry: org.locationtech.jts.geom.Geometry, boundaryNodeRule: org.locationtech.jts.algorithm.BoundaryNodeRule) -> org.locationtech.jts.geom.Geometry: ...
    @staticmethod
    def hasBoundary(geometry: org.locationtech.jts.geom.Geometry, boundaryNodeRule: org.locationtech.jts.algorithm.BoundaryNodeRule) -> bool: ...

class GeometryGraphOperation:
    @typing.overload
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry): ...
    @typing.overload
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry): ...
    @typing.overload
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry, boundaryNodeRule: org.locationtech.jts.algorithm.BoundaryNodeRule): ...
    def getArgGeometry(self, int: int) -> org.locationtech.jts.geom.Geometry: ...

class IsSimpleOp:
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry): ...
    @typing.overload
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry, boundaryNodeRule: org.locationtech.jts.algorithm.BoundaryNodeRule): ...
    def getNonSimpleLocation(self) -> org.locationtech.jts.geom.Coordinate: ...
    @typing.overload
    def isSimple(self) -> bool: ...
    @typing.overload
    def isSimple(self, lineString: org.locationtech.jts.geom.LineString) -> bool: ...
    @typing.overload
    def isSimple(self, multiLineString: org.locationtech.jts.geom.MultiLineString) -> bool: ...
    @typing.overload
    def isSimple(self, multiPoint: org.locationtech.jts.geom.MultiPoint) -> bool: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.locationtech.jts.operation")``.

    BoundaryOp: typing.Type[BoundaryOp]
    GeometryGraphOperation: typing.Type[GeometryGraphOperation]
    IsSimpleOp: typing.Type[IsSimpleOp]
    buffer: org.locationtech.jts.operation.buffer.__module_protocol__
    distance: org.locationtech.jts.operation.distance.__module_protocol__
    distance3d: org.locationtech.jts.operation.distance3d.__module_protocol__
    linemerge: org.locationtech.jts.operation.linemerge.__module_protocol__
    overlay: org.locationtech.jts.operation.overlay.__module_protocol__
    overlayng: org.locationtech.jts.operation.overlayng.__module_protocol__
    polygonize: org.locationtech.jts.operation.polygonize.__module_protocol__
    predicate: org.locationtech.jts.operation.predicate.__module_protocol__
    relate: org.locationtech.jts.operation.relate.__module_protocol__
    union: org.locationtech.jts.operation.union.__module_protocol__
    valid: org.locationtech.jts.operation.valid.__module_protocol__
