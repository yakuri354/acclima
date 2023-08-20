
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org.locationtech.jts.geom
import typing



class CascadedPolygonUnion:
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set]): ...
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set], unionStrategy: 'UnionStrategy'): ...
    @typing.overload
    def union(self) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def union(collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set]) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def union(collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set], unionStrategy: 'UnionStrategy') -> org.locationtech.jts.geom.Geometry: ...

class OverlapUnion:
    @typing.overload
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry): ...
    @typing.overload
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry, unionStrategy: 'UnionStrategy'): ...
    @typing.overload
    def union(self) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def union(geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry, unionStrategy: 'UnionStrategy') -> org.locationtech.jts.geom.Geometry: ...

class PointGeometryUnion:
    def __init__(self, puntal: org.locationtech.jts.geom.Puntal, geometry: org.locationtech.jts.geom.Geometry): ...
    @typing.overload
    def union(self) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def union(puntal: org.locationtech.jts.geom.Puntal, geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...

class UnaryUnionOp:
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set]): ...
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set], geometryFactory: org.locationtech.jts.geom.GeometryFactory): ...
    @typing.overload
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry): ...
    def setUnionFunction(self, unionStrategy: 'UnionStrategy') -> None: ...
    @typing.overload
    def union(self) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def union(collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set]) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def union(collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set], geometryFactory: org.locationtech.jts.geom.GeometryFactory) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def union(geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...

class UnionInteracting:
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry): ...
    @typing.overload
    def union(self) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def union(geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...

class UnionStrategy:
    def isFloatingPrecision(self) -> bool: ...
    def union(self, geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.locationtech.jts.operation.union")``.

    CascadedPolygonUnion: typing.Type[CascadedPolygonUnion]
    OverlapUnion: typing.Type[OverlapUnion]
    PointGeometryUnion: typing.Type[PointGeometryUnion]
    UnaryUnionOp: typing.Type[UnaryUnionOp]
    UnionInteracting: typing.Type[UnionInteracting]
    UnionStrategy: typing.Type[UnionStrategy]
