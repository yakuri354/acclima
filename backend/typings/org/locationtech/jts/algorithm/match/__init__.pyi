
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.locationtech.jts.geom
import typing



class SimilarityMeasure:
    def measure(self, geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry) -> float: ...

class SimilarityMeasureCombiner:
    def __init__(self): ...
    @staticmethod
    def combine(double: float, double2: float) -> float: ...

class AreaSimilarityMeasure(SimilarityMeasure):
    def __init__(self): ...
    def measure(self, geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry) -> float: ...

class FrechetSimilarityMeasure(SimilarityMeasure):
    def __init__(self): ...
    def measure(self, geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry) -> float: ...

class HausdorffSimilarityMeasure(SimilarityMeasure):
    def __init__(self): ...
    @staticmethod
    def diagonalSize(envelope: org.locationtech.jts.geom.Envelope) -> float: ...
    def measure(self, geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry) -> float: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.locationtech.jts.algorithm.match")``.

    AreaSimilarityMeasure: typing.Type[AreaSimilarityMeasure]
    FrechetSimilarityMeasure: typing.Type[FrechetSimilarityMeasure]
    HausdorffSimilarityMeasure: typing.Type[HausdorffSimilarityMeasure]
    SimilarityMeasure: typing.Type[SimilarityMeasure]
    SimilarityMeasureCombiner: typing.Type[SimilarityMeasureCombiner]
