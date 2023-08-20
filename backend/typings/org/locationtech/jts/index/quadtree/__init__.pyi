
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.util
import org.locationtech.jts.geom
import org.locationtech.jts.index
import typing



class DoubleBits:
    EXPONENT_BIAS: typing.ClassVar[int] = ...
    def __init__(self, double: float): ...
    def biasedExponent(self) -> int: ...
    @staticmethod
    def exponent(double: float) -> int: ...
    def getBit(self, int: int) -> int: ...
    def getDouble(self) -> float: ...
    def getExponent(self) -> int: ...
    @staticmethod
    def maximumCommonMantissa(double: float, double2: float) -> float: ...
    def numCommonMantissaBits(self, doubleBits: 'DoubleBits') -> int: ...
    @staticmethod
    def powerOf2(int: int) -> float: ...
    @staticmethod
    def toBinaryString(double: float) -> str: ...
    def toString(self) -> str: ...
    @staticmethod
    def truncateToPowerOfTwo(double: float) -> float: ...
    def zeroLowerBits(self, int: int) -> None: ...

class IntervalSize:
    MIN_BINARY_EXPONENT: typing.ClassVar[int] = ...
    def __init__(self): ...
    @staticmethod
    def isZeroWidth(double: float, double2: float) -> bool: ...

class Key:
    def __init__(self, envelope: org.locationtech.jts.geom.Envelope): ...
    def computeKey(self, envelope: org.locationtech.jts.geom.Envelope) -> None: ...
    @staticmethod
    def computeQuadLevel(envelope: org.locationtech.jts.geom.Envelope) -> int: ...
    def getCentre(self) -> org.locationtech.jts.geom.Coordinate: ...
    def getEnvelope(self) -> org.locationtech.jts.geom.Envelope: ...
    def getLevel(self) -> int: ...
    def getPoint(self) -> org.locationtech.jts.geom.Coordinate: ...

class NodeBase(java.io.Serializable):
    def __init__(self): ...
    def add(self, object: typing.Any) -> None: ...
    def addAllItems(self, list: java.util.List) -> java.util.List: ...
    def addAllItemsFromOverlapping(self, envelope: org.locationtech.jts.geom.Envelope, list: java.util.List) -> None: ...
    def getItems(self) -> java.util.List: ...
    @staticmethod
    def getSubnodeIndex(envelope: org.locationtech.jts.geom.Envelope, double: float, double2: float) -> int: ...
    def hasChildren(self) -> bool: ...
    def hasItems(self) -> bool: ...
    def isEmpty(self) -> bool: ...
    def isPrunable(self) -> bool: ...
    def remove(self, envelope: org.locationtech.jts.geom.Envelope, object: typing.Any) -> bool: ...
    def visit(self, envelope: org.locationtech.jts.geom.Envelope, itemVisitor: org.locationtech.jts.index.ItemVisitor) -> None: ...

class Quadtree(org.locationtech.jts.index.SpatialIndex, java.io.Serializable):
    def __init__(self): ...
    def depth(self) -> int: ...
    @staticmethod
    def ensureExtent(envelope: org.locationtech.jts.geom.Envelope, double: float) -> org.locationtech.jts.geom.Envelope: ...
    def insert(self, envelope: org.locationtech.jts.geom.Envelope, object: typing.Any) -> None: ...
    def isEmpty(self) -> bool: ...
    @typing.overload
    def query(self, envelope: org.locationtech.jts.geom.Envelope) -> java.util.List: ...
    @typing.overload
    def query(self, envelope: org.locationtech.jts.geom.Envelope, itemVisitor: org.locationtech.jts.index.ItemVisitor) -> None: ...
    def queryAll(self) -> java.util.List: ...
    def remove(self, envelope: org.locationtech.jts.geom.Envelope, object: typing.Any) -> bool: ...
    def size(self) -> int: ...

class Node(NodeBase):
    def __init__(self, envelope: org.locationtech.jts.geom.Envelope, int: int): ...
    @staticmethod
    def createExpanded(node: 'Node', envelope: org.locationtech.jts.geom.Envelope) -> 'Node': ...
    @staticmethod
    def createNode(envelope: org.locationtech.jts.geom.Envelope) -> 'Node': ...
    def find(self, envelope: org.locationtech.jts.geom.Envelope) -> NodeBase: ...
    def getEnvelope(self) -> org.locationtech.jts.geom.Envelope: ...
    def getNode(self, envelope: org.locationtech.jts.geom.Envelope) -> 'Node': ...

class Root(NodeBase):
    def __init__(self): ...
    def insert(self, envelope: org.locationtech.jts.geom.Envelope, object: typing.Any) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.locationtech.jts.index.quadtree")``.

    DoubleBits: typing.Type[DoubleBits]
    IntervalSize: typing.Type[IntervalSize]
    Key: typing.Type[Key]
    Node: typing.Type[Node]
    NodeBase: typing.Type[NodeBase]
    Quadtree: typing.Type[Quadtree]
    Root: typing.Type[Root]
