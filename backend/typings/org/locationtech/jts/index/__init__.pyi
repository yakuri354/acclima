
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import jpype
import org.locationtech.jts.geom
import org.locationtech.jts.index.bintree
import org.locationtech.jts.index.chain
import org.locationtech.jts.index.hprtree
import org.locationtech.jts.index.intervalrtree
import org.locationtech.jts.index.kdtree
import org.locationtech.jts.index.quadtree
import org.locationtech.jts.index.strtree
import org.locationtech.jts.index.sweepline
import typing



class ItemVisitor:
    def visitItem(self, object: typing.Any) -> None: ...

class SpatialIndex:
    def insert(self, envelope: org.locationtech.jts.geom.Envelope, object: typing.Any) -> None: ...
    @typing.overload
    def query(self, envelope: org.locationtech.jts.geom.Envelope) -> java.util.List: ...
    @typing.overload
    def query(self, envelope: org.locationtech.jts.geom.Envelope, itemVisitor: ItemVisitor) -> None: ...
    def remove(self, envelope: org.locationtech.jts.geom.Envelope, object: typing.Any) -> bool: ...

class VertexSequencePackedRtree:
    def __init__(self, coordinateArray: typing.Union[typing.List[org.locationtech.jts.geom.Coordinate], jpype.JArray]): ...
    def getBounds(self) -> typing.MutableSequence[org.locationtech.jts.geom.Envelope]: ...
    def query(self, envelope: org.locationtech.jts.geom.Envelope) -> typing.MutableSequence[int]: ...
    def remove(self, int: int) -> None: ...

class ArrayListVisitor(ItemVisitor):
    def __init__(self): ...
    def getItems(self) -> java.util.ArrayList: ...
    def visitItem(self, object: typing.Any) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.locationtech.jts.index")``.

    ArrayListVisitor: typing.Type[ArrayListVisitor]
    ItemVisitor: typing.Type[ItemVisitor]
    SpatialIndex: typing.Type[SpatialIndex]
    VertexSequencePackedRtree: typing.Type[VertexSequencePackedRtree]
    bintree: org.locationtech.jts.index.bintree.__module_protocol__
    chain: org.locationtech.jts.index.chain.__module_protocol__
    hprtree: org.locationtech.jts.index.hprtree.__module_protocol__
    intervalrtree: org.locationtech.jts.index.intervalrtree.__module_protocol__
    kdtree: org.locationtech.jts.index.kdtree.__module_protocol__
    quadtree: org.locationtech.jts.index.quadtree.__module_protocol__
    strtree: org.locationtech.jts.index.strtree.__module_protocol__
    sweepline: org.locationtech.jts.index.sweepline.__module_protocol__
