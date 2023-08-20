
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org.locationtech.jts.geom
import org.locationtech.jts.noding
import typing



class SnappingIntersectionAdder(org.locationtech.jts.noding.SegmentIntersector):
    def __init__(self, double: float, snappingPointIndex: 'SnappingPointIndex'): ...
    def isDone(self) -> bool: ...
    def processIntersections(self, segmentString: org.locationtech.jts.noding.SegmentString, int: int, segmentString2: org.locationtech.jts.noding.SegmentString, int2: int) -> None: ...

class SnappingNoder(org.locationtech.jts.noding.Noder):
    def __init__(self, double: float): ...
    def computeNodes(self, collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set]) -> None: ...
    def getNodedSubstrings(self) -> java.util.Collection: ...

class SnappingPointIndex:
    def __init__(self, double: float): ...
    def depth(self) -> int: ...
    def getTolerance(self) -> float: ...
    def snap(self, coordinate: org.locationtech.jts.geom.Coordinate) -> org.locationtech.jts.geom.Coordinate: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.locationtech.jts.noding.snap")``.

    SnappingIntersectionAdder: typing.Type[SnappingIntersectionAdder]
    SnappingNoder: typing.Type[SnappingNoder]
    SnappingPointIndex: typing.Type[SnappingPointIndex]
