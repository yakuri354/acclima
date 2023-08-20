
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.locationtech.jts.geom
import org.locationtech.jts.shape
import typing



class RandomPointsBuilder(org.locationtech.jts.shape.GeometricShapeBuilder):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, geometryFactory: org.locationtech.jts.geom.GeometryFactory): ...
    def getGeometry(self) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    def setExtent(self, envelope: org.locationtech.jts.geom.Envelope) -> None: ...
    @typing.overload
    def setExtent(self, geometry: org.locationtech.jts.geom.Geometry) -> None: ...

class RandomPointsInGridBuilder(org.locationtech.jts.shape.GeometricShapeBuilder):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, geometryFactory: org.locationtech.jts.geom.GeometryFactory): ...
    def getGeometry(self) -> org.locationtech.jts.geom.Geometry: ...
    def setConstrainedToCircle(self, boolean: bool) -> None: ...
    def setGutterFraction(self, double: float) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.locationtech.jts.shape.random")``.

    RandomPointsBuilder: typing.Type[RandomPointsBuilder]
    RandomPointsInGridBuilder: typing.Type[RandomPointsInGridBuilder]
