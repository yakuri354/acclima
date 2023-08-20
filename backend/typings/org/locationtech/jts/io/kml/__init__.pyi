
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import org.locationtech.jts.geom
import typing



class KMLReader:
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str], typing.Set[str]]): ...
    @typing.overload
    def __init__(self, geometryFactory: org.locationtech.jts.geom.GeometryFactory): ...
    @typing.overload
    def __init__(self, geometryFactory: org.locationtech.jts.geom.GeometryFactory, collection: typing.Union[java.util.Collection[str], typing.Sequence[str], typing.Set[str]]): ...
    def read(self, string: str) -> org.locationtech.jts.geom.Geometry: ...

class KMLWriter:
    ALTITUDE_MODE_CLAMPTOGROUND: typing.ClassVar[str] = ...
    ALTITUDE_MODE_RELATIVETOGROUND: typing.ClassVar[str] = ...
    ALTITUDE_MODE_ABSOLUTE: typing.ClassVar[str] = ...
    def __init__(self): ...
    def setAltitudeMode(self, string: str) -> None: ...
    def setExtrude(self, boolean: bool) -> None: ...
    def setLinePrefix(self, string: str) -> None: ...
    def setMaximumCoordinatesPerLine(self, int: int) -> None: ...
    def setPrecision(self, int: int) -> None: ...
    def setTesselate(self, boolean: bool) -> None: ...
    def setZ(self, double: float) -> None: ...
    @typing.overload
    def write(self, geometry: org.locationtech.jts.geom.Geometry) -> str: ...
    @typing.overload
    def write(self, geometry: org.locationtech.jts.geom.Geometry, writer: java.io.Writer) -> None: ...
    @typing.overload
    def write(self, geometry: org.locationtech.jts.geom.Geometry, stringBuffer: java.lang.StringBuffer) -> None: ...
    @typing.overload
    @staticmethod
    def writeGeometry(geometry: org.locationtech.jts.geom.Geometry, double: float) -> str: ...
    @typing.overload
    @staticmethod
    def writeGeometry(geometry: org.locationtech.jts.geom.Geometry, double: float, int: int, boolean: bool, string: str) -> str: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.locationtech.jts.io.kml")``.

    KMLReader: typing.Type[KMLReader]
    KMLWriter: typing.Type[KMLWriter]