
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org.locationtech.jts.geom
import org.locationtech.jts.planargraph
import typing



class EdgeString:
    def __init__(self, geometryFactory: org.locationtech.jts.geom.GeometryFactory): ...
    def add(self, lineMergeDirectedEdge: 'LineMergeDirectedEdge') -> None: ...
    def toLineString(self) -> org.locationtech.jts.geom.LineString: ...

class LineMergeDirectedEdge(org.locationtech.jts.planargraph.DirectedEdge):
    def __init__(self, node: org.locationtech.jts.planargraph.Node, node2: org.locationtech.jts.planargraph.Node, coordinate: org.locationtech.jts.geom.Coordinate, boolean: bool): ...
    def getNext(self) -> 'LineMergeDirectedEdge': ...

class LineMergeEdge(org.locationtech.jts.planargraph.Edge):
    def __init__(self, lineString: org.locationtech.jts.geom.LineString): ...
    def getLine(self) -> org.locationtech.jts.geom.LineString: ...

class LineMergeGraph(org.locationtech.jts.planargraph.PlanarGraph):
    def __init__(self): ...
    def addEdge(self, lineString: org.locationtech.jts.geom.LineString) -> None: ...

class LineMerger:
    def __init__(self): ...
    @typing.overload
    def add(self, collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set]) -> None: ...
    @typing.overload
    def add(self, geometry: org.locationtech.jts.geom.Geometry) -> None: ...
    def getMergedLineStrings(self) -> java.util.Collection: ...

class LineSequencer:
    def __init__(self): ...
    @typing.overload
    def add(self, collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set]) -> None: ...
    @typing.overload
    def add(self, geometry: org.locationtech.jts.geom.Geometry) -> None: ...
    def getSequencedLineStrings(self) -> org.locationtech.jts.geom.Geometry: ...
    def isSequenceable(self) -> bool: ...
    @staticmethod
    def isSequenced(geometry: org.locationtech.jts.geom.Geometry) -> bool: ...
    @staticmethod
    def sequence(geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.locationtech.jts.operation.linemerge")``.

    EdgeString: typing.Type[EdgeString]
    LineMergeDirectedEdge: typing.Type[LineMergeDirectedEdge]
    LineMergeEdge: typing.Type[LineMergeEdge]
    LineMergeGraph: typing.Type[LineMergeGraph]
    LineMerger: typing.Type[LineMerger]
    LineSequencer: typing.Type[LineSequencer]