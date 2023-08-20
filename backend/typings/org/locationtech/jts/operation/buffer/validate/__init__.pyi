
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.locationtech.jts.geom
import typing



class BufferCurveMaximumDistanceFinder:
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry): ...
    def findDistance(self, geometry: org.locationtech.jts.geom.Geometry) -> float: ...
    def getDistancePoints(self) -> 'PointPairDistance': ...
    class MaxMidpointDistanceFilter(org.locationtech.jts.geom.CoordinateSequenceFilter):
        def __init__(self, geometry: org.locationtech.jts.geom.Geometry): ...
        def filter(self, coordinateSequence: org.locationtech.jts.geom.CoordinateSequence, int: int) -> None: ...
        def getMaxPointDistance(self) -> 'PointPairDistance': ...
        def isDone(self) -> bool: ...
        def isGeometryChanged(self) -> bool: ...
    class MaxPointDistanceFilter(org.locationtech.jts.geom.CoordinateFilter):
        def __init__(self, geometry: org.locationtech.jts.geom.Geometry): ...
        def filter(self, coordinate: org.locationtech.jts.geom.Coordinate) -> None: ...
        def getMaxPointDistance(self) -> 'PointPairDistance': ...

class BufferDistanceValidator:
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry, double: float, geometry2: org.locationtech.jts.geom.Geometry): ...
    def getErrorIndicator(self) -> org.locationtech.jts.geom.Geometry: ...
    def getErrorLocation(self) -> org.locationtech.jts.geom.Coordinate: ...
    def getErrorMessage(self) -> str: ...
    def isValid(self) -> bool: ...

class BufferResultValidator:
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry, double: float, geometry2: org.locationtech.jts.geom.Geometry): ...
    def getErrorIndicator(self) -> org.locationtech.jts.geom.Geometry: ...
    def getErrorLocation(self) -> org.locationtech.jts.geom.Coordinate: ...
    def getErrorMessage(self) -> str: ...
    @typing.overload
    def isValid(self) -> bool: ...
    @typing.overload
    @staticmethod
    def isValid(geometry: org.locationtech.jts.geom.Geometry, double: float, geometry2: org.locationtech.jts.geom.Geometry) -> bool: ...
    @staticmethod
    def isValidMsg(geometry: org.locationtech.jts.geom.Geometry, double: float, geometry2: org.locationtech.jts.geom.Geometry) -> str: ...

class DistanceToPointFinder:
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def computeDistance(geometry: org.locationtech.jts.geom.Geometry, coordinate: org.locationtech.jts.geom.Coordinate, pointPairDistance: 'PointPairDistance') -> None: ...
    @typing.overload
    @staticmethod
    def computeDistance(lineSegment: org.locationtech.jts.geom.LineSegment, coordinate: org.locationtech.jts.geom.Coordinate, pointPairDistance: 'PointPairDistance') -> None: ...
    @typing.overload
    @staticmethod
    def computeDistance(lineString: org.locationtech.jts.geom.LineString, coordinate: org.locationtech.jts.geom.Coordinate, pointPairDistance: 'PointPairDistance') -> None: ...
    @typing.overload
    @staticmethod
    def computeDistance(polygon: org.locationtech.jts.geom.Polygon, coordinate: org.locationtech.jts.geom.Coordinate, pointPairDistance: 'PointPairDistance') -> None: ...

class PointPairDistance:
    def __init__(self): ...
    def getCoordinate(self, int: int) -> org.locationtech.jts.geom.Coordinate: ...
    def getCoordinates(self) -> typing.MutableSequence[org.locationtech.jts.geom.Coordinate]: ...
    def getDistance(self) -> float: ...
    @typing.overload
    def initialize(self) -> None: ...
    @typing.overload
    def initialize(self, coordinate: org.locationtech.jts.geom.Coordinate, coordinate2: org.locationtech.jts.geom.Coordinate) -> None: ...
    @typing.overload
    def setMaximum(self, coordinate: org.locationtech.jts.geom.Coordinate, coordinate2: org.locationtech.jts.geom.Coordinate) -> None: ...
    @typing.overload
    def setMaximum(self, pointPairDistance: 'PointPairDistance') -> None: ...
    @typing.overload
    def setMinimum(self, coordinate: org.locationtech.jts.geom.Coordinate, coordinate2: org.locationtech.jts.geom.Coordinate) -> None: ...
    @typing.overload
    def setMinimum(self, pointPairDistance: 'PointPairDistance') -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.locationtech.jts.operation.buffer.validate")``.

    BufferCurveMaximumDistanceFinder: typing.Type[BufferCurveMaximumDistanceFinder]
    BufferDistanceValidator: typing.Type[BufferDistanceValidator]
    BufferResultValidator: typing.Type[BufferResultValidator]
    DistanceToPointFinder: typing.Type[DistanceToPointFinder]
    PointPairDistance: typing.Type[PointPairDistance]