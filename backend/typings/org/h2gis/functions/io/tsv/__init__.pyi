
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.sql
import jpype.protocol
import org.h2.value
import org.h2gis.api
import typing



class TSVDriverFunction(org.h2gis.api.DriverFunction):
    DESCRIPTION: typing.ClassVar[str] = ...
    def __init__(self): ...
    def exportFromResultSet(self, connection: java.sql.Connection, resultSet: java.sql.ResultSet, writer: java.io.Writer, string: str, progressVisitor: org.h2gis.api.ProgressVisitor) -> None: ...
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

class TSVRead(org.h2gis.api.AbstractFunction, org.h2gis.api.ScalarFunction):
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @typing.overload
    @staticmethod
    def importTable(connection: java.sql.Connection, string: str) -> None: ...
    @typing.overload
    @staticmethod
    def importTable(connection: java.sql.Connection, string: str, string2: str, string3: str, boolean: bool) -> None: ...
    @typing.overload
    @staticmethod
    def importTable(connection: java.sql.Connection, string: str, string2: str, value: org.h2.value.Value) -> None: ...
    @typing.overload
    @staticmethod
    def importTable(connection: java.sql.Connection, string: str, value: org.h2.value.Value) -> None: ...

class TSVWrite(org.h2gis.api.AbstractFunction, org.h2gis.api.ScalarFunction):
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


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.functions.io.tsv")``.

    TSVDriverFunction: typing.Type[TSVDriverFunction]
    TSVRead: typing.Type[TSVRead]
    TSVWrite: typing.Type[TSVWrite]
