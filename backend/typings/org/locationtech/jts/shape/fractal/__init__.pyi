
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.locationtech.jts.geom
import org.locationtech.jts.shape
import typing



class HilbertCode:
    MAX_LEVEL: typing.ClassVar[int] = ...
    def __init__(self): ...
    @staticmethod
    def decode(int: int, int2: int) -> org.locationtech.jts.geom.Coordinate: ...
    @staticmethod
    def encode(int: int, int2: int, int3: int) -> int: ...
    @staticmethod
    def level(int: int) -> int: ...
    @staticmethod
    def maxOrdinate(int: int) -> int: ...
    @staticmethod
    def size(int: int) -> int: ...

class HilbertCurveBuilder(org.locationtech.jts.shape.GeometricShapeBuilder):
    def __init__(self, geometryFactory: org.locationtech.jts.geom.GeometryFactory): ...
    def getGeometry(self) -> org.locationtech.jts.geom.Geometry: ...
    def setLevel(self, int: int) -> None: ...

class KochSnowflakeBuilder(org.locationtech.jts.shape.GeometricShapeBuilder):
    def __init__(self, geometryFactory: org.locationtech.jts.geom.GeometryFactory): ...
    def addSide(self, int: int, coordinate: org.locationtech.jts.geom.Coordinate, coordinate2: org.locationtech.jts.geom.Coordinate) -> None: ...
    def getGeometry(self) -> org.locationtech.jts.geom.Geometry: ...
    @staticmethod
    def recursionLevelForSize(int: int) -> int: ...

class MortonCode:
    MAX_LEVEL: typing.ClassVar[int] = ...
    def __init__(self): ...
    @staticmethod
    def decode(int: int) -> org.locationtech.jts.geom.Coordinate: ...
    @staticmethod
    def encode(int: int, int2: int) -> int: ...
    @staticmethod
    def level(int: int) -> int: ...
    @staticmethod
    def maxOrdinate(int: int) -> int: ...
    @staticmethod
    def size(int: int) -> int: ...

class MortonCurveBuilder(org.locationtech.jts.shape.GeometricShapeBuilder):
    def __init__(self, geometryFactory: org.locationtech.jts.geom.GeometryFactory): ...
    def getGeometry(self) -> org.locationtech.jts.geom.Geometry: ...
    def setLevel(self, int: int) -> None: ...

class SierpinskiCarpetBuilder(org.locationtech.jts.shape.GeometricShapeBuilder):
    def __init__(self, geometryFactory: org.locationtech.jts.geom.GeometryFactory): ...
    def getGeometry(self) -> org.locationtech.jts.geom.Geometry: ...
    @staticmethod
    def recursionLevelForSize(int: int) -> int: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.locationtech.jts.shape.fractal")``.

    HilbertCode: typing.Type[HilbertCode]
    HilbertCurveBuilder: typing.Type[HilbertCurveBuilder]
    KochSnowflakeBuilder: typing.Type[KochSnowflakeBuilder]
    MortonCode: typing.Type[MortonCode]
    MortonCurveBuilder: typing.Type[MortonCurveBuilder]
    SierpinskiCarpetBuilder: typing.Type[SierpinskiCarpetBuilder]
