
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.sql
import jpype.protocol
import org.h2gis.api
import org.h2gis.functions.io.asc
import org.h2gis.functions.io.csv
import org.h2gis.functions.io.dbf
import org.h2gis.functions.io.file_table
import org.h2gis.functions.io.geojson
import org.h2gis.functions.io.gpx
import org.h2gis.functions.io.json
import org.h2gis.functions.io.kml
import org.h2gis.functions.io.osm
import org.h2gis.functions.io.shp
import org.h2gis.functions.io.tsv
import org.h2gis.functions.io.utility
import typing



class DriverManager(org.h2gis.api.AbstractFunction, org.h2gis.api.ScalarFunction, org.h2gis.api.DriverFunction):
    def __init__(self): ...
    @staticmethod
    def check(connection: java.sql.Connection, string: str, file: typing.Union[java.io.File, jpype.protocol.SupportsPath], progressVisitor: org.h2gis.api.ProgressVisitor) -> org.h2gis.api.ProgressVisitor: ...
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
    def getJavaStaticMethod(self) -> str: ...
    @typing.overload
    def importFile(self, connection: java.sql.Connection, string: str, file: typing.Union[java.io.File, jpype.protocol.SupportsPath], boolean: bool, progressVisitor: org.h2gis.api.ProgressVisitor) -> typing.MutableSequence[str]: ...
    @typing.overload
    def importFile(self, connection: java.sql.Connection, string: str, file: typing.Union[java.io.File, jpype.protocol.SupportsPath], string2: str, boolean: bool, progressVisitor: org.h2gis.api.ProgressVisitor) -> typing.MutableSequence[str]: ...
    @typing.overload
    def importFile(self, connection: java.sql.Connection, string: str, file: typing.Union[java.io.File, jpype.protocol.SupportsPath], string2: str, progressVisitor: org.h2gis.api.ProgressVisitor) -> typing.MutableSequence[str]: ...
    @typing.overload
    def importFile(self, connection: java.sql.Connection, string: str, file: typing.Union[java.io.File, jpype.protocol.SupportsPath], progressVisitor: org.h2gis.api.ProgressVisitor) -> typing.MutableSequence[str]: ...
    def isSpatialFormat(self, string: str) -> bool: ...
    @staticmethod
    def openFile(connection: java.sql.Connection, string: str, string2: str) -> typing.MutableSequence[str]: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.functions.io")``.

    DriverManager: typing.Type[DriverManager]
    asc: org.h2gis.functions.io.asc.__module_protocol__
    csv: org.h2gis.functions.io.csv.__module_protocol__
    dbf: org.h2gis.functions.io.dbf.__module_protocol__
    file_table: org.h2gis.functions.io.file_table.__module_protocol__
    geojson: org.h2gis.functions.io.geojson.__module_protocol__
    gpx: org.h2gis.functions.io.gpx.__module_protocol__
    json: org.h2gis.functions.io.json.__module_protocol__
    kml: org.h2gis.functions.io.kml.__module_protocol__
    osm: org.h2gis.functions.io.osm.__module_protocol__
    shp: org.h2gis.functions.io.shp.__module_protocol__
    tsv: org.h2gis.functions.io.tsv.__module_protocol__
    utility: org.h2gis.functions.io.utility.__module_protocol__
