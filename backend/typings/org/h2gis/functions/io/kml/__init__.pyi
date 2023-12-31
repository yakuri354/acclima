
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.sql
import javax.xml.stream
import jpype
import jpype.protocol
import org.h2.value
import org.h2gis.api
import org.locationtech.jts.geom
import typing



class AltitudeMode:
    KML_CLAMPTOGROUND: typing.ClassVar[int] = ...
    KML_RELATIVETOGROUND: typing.ClassVar[int] = ...
    KML_ABSOLUTE: typing.ClassVar[int] = ...
    GX_CLAMPTOSEAFLOOR: typing.ClassVar[int] = ...
    GX_RELATIVETOSEAFLOOR: typing.ClassVar[int] = ...
    NONE: typing.ClassVar[int] = ...
    @staticmethod
    def append(int: int, stringBuilder: java.lang.StringBuilder) -> None: ...

class ExtrudeMode(java.lang.Enum['ExtrudeMode']):
    TRUE: typing.ClassVar['ExtrudeMode'] = ...
    FALSE: typing.ClassVar['ExtrudeMode'] = ...
    NONE: typing.ClassVar['ExtrudeMode'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ExtrudeMode': ...
    @staticmethod
    def values() -> typing.MutableSequence['ExtrudeMode']: ...

class KMLDriverFunction(org.h2gis.api.DriverFunction):
    def __init__(self): ...
    @typing.overload
    def exportTable(self, connection: java.sql.Connection, string: str, file: typing.Union[java.io.File, jpype.protocol.SupportsPath], boolean: bool, progressVisitor: org.h2gis.api.ProgressVisitor) -> typing.MutableSequence[str]: ...
    @typing.overload
    def exportTable(self, connection: java.sql.Connection, string: str, file: typing.Union[java.io.File, jpype.protocol.SupportsPath], string2: str, boolean: bool, progressVisitor: org.h2gis.api.ProgressVisitor) -> typing.MutableSequence[str]: ...
    @typing.overload
    def exportTable(self, connection: java.sql.Connection, string: str, file: typing.Union[java.io.File, jpype.protocol.SupportsPath], string2: str, progressVisitor: org.h2gis.api.ProgressVisitor) -> typing.MutableSequence[str]: ...
    @typing.overload
    def exportTable(self, connection: java.sql.Connection, string: str, file: typing.Union[java.io.File, jpype.protocol.SupportsPath], progressVisitor: org.h2gis.api.ProgressVisitor) -> typing.MutableSequence[str]: ...
    def getExportFormats(self) -> typing.MutableSequence[str]: ...
    def getFormatDescription(self, string: str) -> str: ...
    def getImportDriverType(self) -> org.h2gis.api.DriverFunction.IMPORT_DRIVER_TYPE: ...
    def getImportFormats(self) -> typing.MutableSequence[str]: ...
    @typing.overload
    def importFile(self, connection: java.sql.Connection, string: str, file: typing.Union[java.io.File, jpype.protocol.SupportsPath], boolean: bool, progressVisitor: org.h2gis.api.ProgressVisitor) -> typing.MutableSequence[str]: ...
    @typing.overload
    def importFile(self, connection: java.sql.Connection, string: str, file: typing.Union[java.io.File, jpype.protocol.SupportsPath], string2: str, boolean: bool, progressVisitor: org.h2gis.api.ProgressVisitor) -> typing.MutableSequence[str]: ...
    @typing.overload
    def importFile(self, connection: java.sql.Connection, string: str, file: typing.Union[java.io.File, jpype.protocol.SupportsPath], string2: str, progressVisitor: org.h2gis.api.ProgressVisitor) -> typing.MutableSequence[str]: ...
    @typing.overload
    def importFile(self, connection: java.sql.Connection, string: str, file: typing.Union[java.io.File, jpype.protocol.SupportsPath], progressVisitor: org.h2gis.api.ProgressVisitor) -> typing.MutableSequence[str]: ...
    def isSpatialFormat(self, string: str) -> bool: ...

class KMLGeometry:
    @staticmethod
    def appendKMLCoordinates(coordinateArray: typing.Union[typing.List[org.locationtech.jts.geom.Coordinate], jpype.JArray], stringBuilder: java.lang.StringBuilder) -> None: ...
    @typing.overload
    @staticmethod
    def toKMLGeometry(geometry: org.locationtech.jts.geom.Geometry, stringBuilder: java.lang.StringBuilder) -> None: ...
    @typing.overload
    @staticmethod
    def toKMLGeometry(geometry: org.locationtech.jts.geom.Geometry, extrudeMode: ExtrudeMode, int: int, stringBuilder: java.lang.StringBuilder) -> None: ...
    @staticmethod
    def toKMLLineString(lineString: org.locationtech.jts.geom.LineString, extrudeMode: ExtrudeMode, int: int, stringBuilder: java.lang.StringBuilder) -> None: ...
    @staticmethod
    def toKMLLinearRing(lineString: org.locationtech.jts.geom.LineString, extrudeMode: ExtrudeMode, int: int, stringBuilder: java.lang.StringBuilder) -> None: ...
    @staticmethod
    def toKMLMultiGeometry(geometryCollection: org.locationtech.jts.geom.GeometryCollection, extrudeMode: ExtrudeMode, int: int, stringBuilder: java.lang.StringBuilder) -> None: ...
    @staticmethod
    def toKMLPoint(point: org.locationtech.jts.geom.Point, extrudeMode: ExtrudeMode, int: int, stringBuilder: java.lang.StringBuilder) -> None: ...
    @staticmethod
    def toKMLPolygon(polygon: org.locationtech.jts.geom.Polygon, extrudeMode: ExtrudeMode, int: int, stringBuilder: java.lang.StringBuilder) -> None: ...

class KMLWrite(org.h2gis.api.AbstractFunction, org.h2gis.api.ScalarFunction):
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def exportTable(connection: java.sql.Connection, string: str, string2: str) -> None: ...
    @typing.overload
    @staticmethod
    def exportTable(connection: java.sql.Connection, string: str, string2: str, string3: str, boolean: bool) -> None: ...
    @typing.overload
    @staticmethod
    def exportTable(connection: java.sql.Connection, string: str, string2: str, value: org.h2.value.Value) -> None: ...
    def getJavaStaticMethod(self) -> str: ...

class KMLWriterDriver:
    def __init__(self, connection: java.sql.Connection, file: typing.Union[java.io.File, jpype.protocol.SupportsPath], string: str, boolean: bool): ...
    def write(self, string: str, progressVisitor: org.h2gis.api.ProgressVisitor) -> None: ...
    def writeExtendedData(self, xMLStreamWriter: javax.xml.stream.XMLStreamWriter, resultSet: java.sql.ResultSet) -> None: ...
    def writePlacemark(self, xMLStreamWriter: javax.xml.stream.XMLStreamWriter, resultSet: java.sql.ResultSet, string: str) -> None: ...
    def writeSimpleData(self, xMLStreamWriter: javax.xml.stream.XMLStreamWriter, string: str, string2: str) -> None: ...

class ST_AsKml(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @typing.overload
    @staticmethod
    def toKml(geometry: org.locationtech.jts.geom.Geometry) -> str: ...
    @typing.overload
    @staticmethod
    def toKml(geometry: org.locationtech.jts.geom.Geometry, boolean: bool, int: int) -> str: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.functions.io.kml")``.

    AltitudeMode: typing.Type[AltitudeMode]
    ExtrudeMode: typing.Type[ExtrudeMode]
    KMLDriverFunction: typing.Type[KMLDriverFunction]
    KMLGeometry: typing.Type[KMLGeometry]
    KMLWrite: typing.Type[KMLWrite]
    KMLWriterDriver: typing.Type[KMLWriterDriver]
    ST_AsKml: typing.Type[ST_AsKml]
