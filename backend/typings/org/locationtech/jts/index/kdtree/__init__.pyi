
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org.locationtech.jts.geom
import typing



class KdNode:
    @typing.overload
    def __init__(self, double: float, double2: float, object: typing.Any): ...
    @typing.overload
    def __init__(self, coordinate: org.locationtech.jts.geom.Coordinate, object: typing.Any): ...
    def getCoordinate(self) -> org.locationtech.jts.geom.Coordinate: ...
    def getCount(self) -> int: ...
    def getData(self) -> typing.Any: ...
    def getLeft(self) -> 'KdNode': ...
    def getRight(self) -> 'KdNode': ...
    def getX(self) -> float: ...
    def getY(self) -> float: ...
    def isRepeated(self) -> bool: ...
    def splitValue(self, boolean: bool) -> float: ...

class KdNodeVisitor:
    def visit(self, kdNode: KdNode) -> None: ...

class KdTree:
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    def depth(self) -> int: ...
    def getRoot(self) -> KdNode: ...
    @typing.overload
    def insert(self, coordinate: org.locationtech.jts.geom.Coordinate) -> KdNode: ...
    @typing.overload
    def insert(self, coordinate: org.locationtech.jts.geom.Coordinate, object: typing.Any) -> KdNode: ...
    def isEmpty(self) -> bool: ...
    @typing.overload
    def query(self, envelope: org.locationtech.jts.geom.Envelope) -> java.util.List: ...
    @typing.overload
    def query(self, coordinate: org.locationtech.jts.geom.Coordinate) -> KdNode: ...
    @typing.overload
    def query(self, envelope: org.locationtech.jts.geom.Envelope, list: java.util.List) -> None: ...
    @typing.overload
    def query(self, envelope: org.locationtech.jts.geom.Envelope, kdNodeVisitor: KdNodeVisitor) -> None: ...
    def size(self) -> int: ...
    @typing.overload
    @staticmethod
    def toCoordinates(collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set]) -> typing.MutableSequence[org.locationtech.jts.geom.Coordinate]: ...
    @typing.overload
    @staticmethod
    def toCoordinates(collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set], boolean: bool) -> typing.MutableSequence[org.locationtech.jts.geom.Coordinate]: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.locationtech.jts.index.kdtree")``.

    KdNode: typing.Type[KdNode]
    KdNodeVisitor: typing.Type[KdNodeVisitor]
    KdTree: typing.Type[KdTree]
