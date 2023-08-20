
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import datetime
import decimal
import java.io
import java.math
import java.net
import java.sql
import java.util
import java.util.concurrent
import java.util.logging
import javax.sql
import jpype
import org.h2gis.utilities
import org.locationtech.jts.geom
import typing



class ConnectionWrapper(java.sql.Connection):
    def __init__(self, connection: java.sql.Connection): ...
    def abort(self, executor: java.util.concurrent.Executor) -> None: ...
    def clearWarnings(self) -> None: ...
    def close(self) -> None: ...
    def commit(self) -> None: ...
    def createArrayOf(self, string: str, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> java.sql.Array: ...
    def createBlob(self) -> java.sql.Blob: ...
    def createClob(self) -> java.sql.Clob: ...
    def createNClob(self) -> java.sql.NClob: ...
    def createSQLXML(self) -> java.sql.SQLXML: ...
    @typing.overload
    def createStatement(self) -> java.sql.Statement: ...
    @typing.overload
    def createStatement(self, int: int, int2: int) -> java.sql.Statement: ...
    @typing.overload
    def createStatement(self, int: int, int2: int, int3: int) -> java.sql.Statement: ...
    def createStruct(self, string: str, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> java.sql.Struct: ...
    def getAutoCommit(self) -> bool: ...
    def getCatalog(self) -> str: ...
    @typing.overload
    def getClientInfo(self, string: str) -> str: ...
    @typing.overload
    def getClientInfo(self) -> java.util.Properties: ...
    def getHoldability(self) -> int: ...
    def getMetaData(self) -> java.sql.DatabaseMetaData: ...
    def getNetworkTimeout(self) -> int: ...
    def getSchema(self) -> str: ...
    def getTransactionIsolation(self) -> int: ...
    def getTypeMap(self) -> java.util.Map[str, typing.Type[typing.Any]]: ...
    def getWarnings(self) -> java.sql.SQLWarning: ...
    def isClosed(self) -> bool: ...
    def isReadOnly(self) -> bool: ...
    def isValid(self, int: int) -> bool: ...
    def isWrapperFor(self, class_: typing.Type[typing.Any]) -> bool: ...
    def nativeSQL(self, string: str) -> str: ...
    @typing.overload
    def prepareCall(self, string: str) -> java.sql.CallableStatement: ...
    @typing.overload
    def prepareCall(self, string: str, int: int, int2: int) -> java.sql.CallableStatement: ...
    @typing.overload
    def prepareCall(self, string: str, int: int, int2: int, int3: int) -> java.sql.CallableStatement: ...
    @typing.overload
    def prepareStatement(self, string: str) -> java.sql.PreparedStatement: ...
    @typing.overload
    def prepareStatement(self, string: str, int: int) -> java.sql.PreparedStatement: ...
    @typing.overload
    def prepareStatement(self, string: str, int: int, int2: int) -> java.sql.PreparedStatement: ...
    @typing.overload
    def prepareStatement(self, string: str, int: int, int2: int, int3: int) -> java.sql.PreparedStatement: ...
    @typing.overload
    def prepareStatement(self, string: str, intArray: typing.Union[typing.List[int], jpype.JArray]) -> java.sql.PreparedStatement: ...
    @typing.overload
    def prepareStatement(self, string: str, stringArray: typing.Union[typing.List[str], jpype.JArray]) -> java.sql.PreparedStatement: ...
    def releaseSavepoint(self, savepoint: java.sql.Savepoint) -> None: ...
    @typing.overload
    def rollback(self) -> None: ...
    @typing.overload
    def rollback(self, savepoint: java.sql.Savepoint) -> None: ...
    def setAutoCommit(self, boolean: bool) -> None: ...
    def setCatalog(self, string: str) -> None: ...
    @typing.overload
    def setClientInfo(self, string: str, string2: str) -> None: ...
    @typing.overload
    def setClientInfo(self, properties: java.util.Properties) -> None: ...
    def setHoldability(self, int: int) -> None: ...
    def setNetworkTimeout(self, executor: java.util.concurrent.Executor, int: int) -> None: ...
    def setReadOnly(self, boolean: bool) -> None: ...
    @typing.overload
    def setSavepoint(self) -> java.sql.Savepoint: ...
    @typing.overload
    def setSavepoint(self, string: str) -> java.sql.Savepoint: ...
    def setSchema(self, string: str) -> None: ...
    def setTransactionIsolation(self, int: int) -> None: ...
    def setTypeMap(self, map: typing.Union[java.util.Map[str, typing.Type[typing.Any]], typing.Mapping[str, typing.Type[typing.Any]]]) -> None: ...
    _unwrap__T = typing.TypeVar('_unwrap__T')  # <T>
    def unwrap(self, class_: typing.Type[_unwrap__T]) -> _unwrap__T: ...

class DataSourceWrapper(javax.sql.DataSource):
    def __init__(self, dataSource: javax.sql.DataSource): ...
    @typing.overload
    def getConnection(self) -> java.sql.Connection: ...
    @typing.overload
    def getConnection(self, string: str, string2: str) -> java.sql.Connection: ...
    def getLogWriter(self) -> java.io.PrintWriter: ...
    def getLoginTimeout(self) -> int: ...
    def getParentLogger(self) -> java.util.logging.Logger: ...
    def isWrapperFor(self, class_: typing.Type[typing.Any]) -> bool: ...
    def setLogWriter(self, printWriter: java.io.PrintWriter) -> None: ...
    def setLoginTimeout(self, int: int) -> None: ...
    _unwrap__T = typing.TypeVar('_unwrap__T')  # <T>
    def unwrap(self, class_: typing.Type[_unwrap__T]) -> _unwrap__T: ...

class ResultSetMetaDataWrapper(java.sql.ResultSetMetaData):
    def __init__(self, resultSetMetaData: java.sql.ResultSetMetaData, statementWrapper: 'StatementWrapper'): ...
    def getCatalogName(self, int: int) -> str: ...
    def getColumnClassName(self, int: int) -> str: ...
    def getColumnCount(self) -> int: ...
    def getColumnDisplaySize(self, int: int) -> int: ...
    def getColumnLabel(self, int: int) -> str: ...
    def getColumnName(self, int: int) -> str: ...
    def getColumnType(self, int: int) -> int: ...
    def getColumnTypeName(self, int: int) -> str: ...
    def getPrecision(self, int: int) -> int: ...
    def getScale(self, int: int) -> int: ...
    def getSchemaName(self, int: int) -> str: ...
    def getTableName(self, int: int) -> str: ...
    def isAutoIncrement(self, int: int) -> bool: ...
    def isCaseSensitive(self, int: int) -> bool: ...
    def isCurrency(self, int: int) -> bool: ...
    def isDefinitelyWritable(self, int: int) -> bool: ...
    def isNullable(self, int: int) -> int: ...
    def isReadOnly(self, int: int) -> bool: ...
    def isSearchable(self, int: int) -> bool: ...
    def isSigned(self, int: int) -> bool: ...
    def isWrapperFor(self, class_: typing.Type[typing.Any]) -> bool: ...
    def isWritable(self, int: int) -> bool: ...
    _unwrap__T = typing.TypeVar('_unwrap__T')  # <T>
    def unwrap(self, class_: typing.Type[_unwrap__T]) -> _unwrap__T: ...

class ResultSetWrapper(java.sql.ResultSet):
    def __init__(self, resultSet: java.sql.ResultSet, statementWrapper: 'StatementWrapper'): ...
    def absolute(self, int: int) -> bool: ...
    def afterLast(self) -> None: ...
    def beforeFirst(self) -> None: ...
    def cancelRowUpdates(self) -> None: ...
    def clearWarnings(self) -> None: ...
    def close(self) -> None: ...
    def deleteRow(self) -> None: ...
    def findColumn(self, string: str) -> int: ...
    def first(self) -> bool: ...
    @typing.overload
    def getArray(self, int: int) -> java.sql.Array: ...
    @typing.overload
    def getArray(self, string: str) -> java.sql.Array: ...
    @typing.overload
    def getAsciiStream(self, int: int) -> java.io.InputStream: ...
    @typing.overload
    def getAsciiStream(self, string: str) -> java.io.InputStream: ...
    @typing.overload
    def getBigDecimal(self, int: int) -> java.math.BigDecimal: ...
    @typing.overload
    def getBigDecimal(self, int: int, int2: int) -> java.math.BigDecimal: ...
    @typing.overload
    def getBigDecimal(self, string: str) -> java.math.BigDecimal: ...
    @typing.overload
    def getBigDecimal(self, string: str, int: int) -> java.math.BigDecimal: ...
    @typing.overload
    def getBinaryStream(self, int: int) -> java.io.InputStream: ...
    @typing.overload
    def getBinaryStream(self, string: str) -> java.io.InputStream: ...
    @typing.overload
    def getBlob(self, int: int) -> java.sql.Blob: ...
    @typing.overload
    def getBlob(self, string: str) -> java.sql.Blob: ...
    @typing.overload
    def getBoolean(self, int: int) -> bool: ...
    @typing.overload
    def getBoolean(self, string: str) -> bool: ...
    @typing.overload
    def getByte(self, int: int) -> int: ...
    @typing.overload
    def getByte(self, string: str) -> int: ...
    @typing.overload
    def getBytes(self, int: int) -> typing.MutableSequence[int]: ...
    @typing.overload
    def getBytes(self, string: str) -> typing.MutableSequence[int]: ...
    @typing.overload
    def getCharacterStream(self, int: int) -> java.io.Reader: ...
    @typing.overload
    def getCharacterStream(self, string: str) -> java.io.Reader: ...
    @typing.overload
    def getClob(self, int: int) -> java.sql.Clob: ...
    @typing.overload
    def getClob(self, string: str) -> java.sql.Clob: ...
    def getConcurrency(self) -> int: ...
    def getCursorName(self) -> str: ...
    @typing.overload
    def getDate(self, int: int) -> java.sql.Date: ...
    @typing.overload
    def getDate(self, int: int, calendar: java.util.Calendar) -> java.sql.Date: ...
    @typing.overload
    def getDate(self, string: str) -> java.sql.Date: ...
    @typing.overload
    def getDate(self, string: str, calendar: java.util.Calendar) -> java.sql.Date: ...
    @typing.overload
    def getDouble(self, int: int) -> float: ...
    @typing.overload
    def getDouble(self, string: str) -> float: ...
    def getFetchDirection(self) -> int: ...
    def getFetchSize(self) -> int: ...
    @typing.overload
    def getFloat(self, int: int) -> float: ...
    @typing.overload
    def getFloat(self, string: str) -> float: ...
    def getHoldability(self) -> int: ...
    @typing.overload
    def getInt(self, int: int) -> int: ...
    @typing.overload
    def getInt(self, string: str) -> int: ...
    @typing.overload
    def getLong(self, int: int) -> int: ...
    @typing.overload
    def getLong(self, string: str) -> int: ...
    def getMetaData(self) -> java.sql.ResultSetMetaData: ...
    @typing.overload
    def getNCharacterStream(self, int: int) -> java.io.Reader: ...
    @typing.overload
    def getNCharacterStream(self, string: str) -> java.io.Reader: ...
    @typing.overload
    def getNClob(self, int: int) -> java.sql.NClob: ...
    @typing.overload
    def getNClob(self, string: str) -> java.sql.NClob: ...
    @typing.overload
    def getNString(self, int: int) -> str: ...
    @typing.overload
    def getNString(self, string: str) -> str: ...
    _getObject_1__T = typing.TypeVar('_getObject_1__T')  # <T>
    _getObject_4__T = typing.TypeVar('_getObject_4__T')  # <T>
    @typing.overload
    def getObject(self, int: int) -> typing.Any: ...
    @typing.overload
    def getObject(self, int: int, class_: typing.Type[_getObject_1__T]) -> _getObject_1__T: ...
    @typing.overload
    def getObject(self, int: int, map: typing.Union[java.util.Map[str, typing.Type[typing.Any]], typing.Mapping[str, typing.Type[typing.Any]]]) -> typing.Any: ...
    @typing.overload
    def getObject(self, string: str) -> typing.Any: ...
    @typing.overload
    def getObject(self, string: str, class_: typing.Type[_getObject_4__T]) -> _getObject_4__T: ...
    @typing.overload
    def getObject(self, string: str, map: typing.Union[java.util.Map[str, typing.Type[typing.Any]], typing.Mapping[str, typing.Type[typing.Any]]]) -> typing.Any: ...
    @typing.overload
    def getRef(self, int: int) -> java.sql.Ref: ...
    @typing.overload
    def getRef(self, string: str) -> java.sql.Ref: ...
    def getRow(self) -> int: ...
    @typing.overload
    def getRowId(self, int: int) -> java.sql.RowId: ...
    @typing.overload
    def getRowId(self, string: str) -> java.sql.RowId: ...
    @typing.overload
    def getSQLXML(self, int: int) -> java.sql.SQLXML: ...
    @typing.overload
    def getSQLXML(self, string: str) -> java.sql.SQLXML: ...
    @typing.overload
    def getShort(self, int: int) -> int: ...
    @typing.overload
    def getShort(self, string: str) -> int: ...
    def getStatement(self) -> java.sql.Statement: ...
    @typing.overload
    def getString(self, int: int) -> str: ...
    @typing.overload
    def getString(self, string: str) -> str: ...
    @typing.overload
    def getTime(self, int: int) -> java.sql.Time: ...
    @typing.overload
    def getTime(self, int: int, calendar: java.util.Calendar) -> java.sql.Time: ...
    @typing.overload
    def getTime(self, string: str) -> java.sql.Time: ...
    @typing.overload
    def getTime(self, string: str, calendar: java.util.Calendar) -> java.sql.Time: ...
    @typing.overload
    def getTimestamp(self, int: int) -> java.sql.Timestamp: ...
    @typing.overload
    def getTimestamp(self, int: int, calendar: java.util.Calendar) -> java.sql.Timestamp: ...
    @typing.overload
    def getTimestamp(self, string: str) -> java.sql.Timestamp: ...
    @typing.overload
    def getTimestamp(self, string: str, calendar: java.util.Calendar) -> java.sql.Timestamp: ...
    def getType(self) -> int: ...
    @typing.overload
    def getURL(self, int: int) -> java.net.URL: ...
    @typing.overload
    def getURL(self, string: str) -> java.net.URL: ...
    @typing.overload
    def getUnicodeStream(self, int: int) -> java.io.InputStream: ...
    @typing.overload
    def getUnicodeStream(self, string: str) -> java.io.InputStream: ...
    def getWarnings(self) -> java.sql.SQLWarning: ...
    def insertRow(self) -> None: ...
    def isAfterLast(self) -> bool: ...
    def isBeforeFirst(self) -> bool: ...
    def isClosed(self) -> bool: ...
    def isFirst(self) -> bool: ...
    def isLast(self) -> bool: ...
    def isWrapperFor(self, class_: typing.Type[typing.Any]) -> bool: ...
    def last(self) -> bool: ...
    def moveToCurrentRow(self) -> None: ...
    def moveToInsertRow(self) -> None: ...
    def next(self) -> bool: ...
    def previous(self) -> bool: ...
    def refreshRow(self) -> None: ...
    def relative(self, int: int) -> bool: ...
    def rowDeleted(self) -> bool: ...
    def rowInserted(self) -> bool: ...
    def rowUpdated(self) -> bool: ...
    def setFetchDirection(self, int: int) -> None: ...
    def setFetchSize(self, int: int) -> None: ...
    _unwrap__T = typing.TypeVar('_unwrap__T')  # <T>
    def unwrap(self, class_: typing.Type[_unwrap__T]) -> _unwrap__T: ...
    @typing.overload
    def updateArray(self, int: int, array: java.sql.Array) -> None: ...
    @typing.overload
    def updateArray(self, string: str, array: java.sql.Array) -> None: ...
    @typing.overload
    def updateAsciiStream(self, int: int, inputStream: java.io.InputStream) -> None: ...
    @typing.overload
    def updateAsciiStream(self, int: int, inputStream: java.io.InputStream, int2: int) -> None: ...
    @typing.overload
    def updateAsciiStream(self, int: int, inputStream: java.io.InputStream, long: int) -> None: ...
    @typing.overload
    def updateAsciiStream(self, string: str, inputStream: java.io.InputStream) -> None: ...
    @typing.overload
    def updateAsciiStream(self, string: str, inputStream: java.io.InputStream, int: int) -> None: ...
    @typing.overload
    def updateAsciiStream(self, string: str, inputStream: java.io.InputStream, long: int) -> None: ...
    @typing.overload
    def updateBigDecimal(self, int: int, bigDecimal: typing.Union[java.math.BigDecimal, decimal.Decimal]) -> None: ...
    @typing.overload
    def updateBigDecimal(self, string: str, bigDecimal: typing.Union[java.math.BigDecimal, decimal.Decimal]) -> None: ...
    @typing.overload
    def updateBinaryStream(self, int: int, inputStream: java.io.InputStream) -> None: ...
    @typing.overload
    def updateBinaryStream(self, int: int, inputStream: java.io.InputStream, int2: int) -> None: ...
    @typing.overload
    def updateBinaryStream(self, int: int, inputStream: java.io.InputStream, long: int) -> None: ...
    @typing.overload
    def updateBinaryStream(self, string: str, inputStream: java.io.InputStream) -> None: ...
    @typing.overload
    def updateBinaryStream(self, string: str, inputStream: java.io.InputStream, int: int) -> None: ...
    @typing.overload
    def updateBinaryStream(self, string: str, inputStream: java.io.InputStream, long: int) -> None: ...
    @typing.overload
    def updateBlob(self, int: int, inputStream: java.io.InputStream) -> None: ...
    @typing.overload
    def updateBlob(self, int: int, inputStream: java.io.InputStream, long: int) -> None: ...
    @typing.overload
    def updateBlob(self, int: int, blob: java.sql.Blob) -> None: ...
    @typing.overload
    def updateBlob(self, string: str, inputStream: java.io.InputStream) -> None: ...
    @typing.overload
    def updateBlob(self, string: str, inputStream: java.io.InputStream, long: int) -> None: ...
    @typing.overload
    def updateBlob(self, string: str, blob: java.sql.Blob) -> None: ...
    @typing.overload
    def updateBoolean(self, int: int, boolean: bool) -> None: ...
    @typing.overload
    def updateBoolean(self, string: str, boolean: bool) -> None: ...
    @typing.overload
    def updateByte(self, int: int, byte: int) -> None: ...
    @typing.overload
    def updateByte(self, string: str, byte: int) -> None: ...
    @typing.overload
    def updateBytes(self, int: int, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> None: ...
    @typing.overload
    def updateBytes(self, string: str, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> None: ...
    @typing.overload
    def updateCharacterStream(self, int: int, reader: java.io.Reader) -> None: ...
    @typing.overload
    def updateCharacterStream(self, int: int, reader: java.io.Reader, int2: int) -> None: ...
    @typing.overload
    def updateCharacterStream(self, int: int, reader: java.io.Reader, long: int) -> None: ...
    @typing.overload
    def updateCharacterStream(self, string: str, reader: java.io.Reader) -> None: ...
    @typing.overload
    def updateCharacterStream(self, string: str, reader: java.io.Reader, int: int) -> None: ...
    @typing.overload
    def updateCharacterStream(self, string: str, reader: java.io.Reader, long: int) -> None: ...
    @typing.overload
    def updateClob(self, int: int, reader: java.io.Reader) -> None: ...
    @typing.overload
    def updateClob(self, int: int, reader: java.io.Reader, long: int) -> None: ...
    @typing.overload
    def updateClob(self, int: int, clob: java.sql.Clob) -> None: ...
    @typing.overload
    def updateClob(self, string: str, reader: java.io.Reader) -> None: ...
    @typing.overload
    def updateClob(self, string: str, reader: java.io.Reader, long: int) -> None: ...
    @typing.overload
    def updateClob(self, string: str, clob: java.sql.Clob) -> None: ...
    @typing.overload
    def updateDate(self, int: int, date: typing.Union[java.sql.Date, datetime.date]) -> None: ...
    @typing.overload
    def updateDate(self, string: str, date: typing.Union[java.sql.Date, datetime.date]) -> None: ...
    @typing.overload
    def updateDouble(self, int: int, double: float) -> None: ...
    @typing.overload
    def updateDouble(self, string: str, double: float) -> None: ...
    @typing.overload
    def updateFloat(self, int: int, float: float) -> None: ...
    @typing.overload
    def updateFloat(self, string: str, float: float) -> None: ...
    @typing.overload
    def updateInt(self, int: int, int2: int) -> None: ...
    @typing.overload
    def updateInt(self, string: str, int: int) -> None: ...
    @typing.overload
    def updateLong(self, int: int, long: int) -> None: ...
    @typing.overload
    def updateLong(self, string: str, long: int) -> None: ...
    @typing.overload
    def updateNCharacterStream(self, int: int, reader: java.io.Reader) -> None: ...
    @typing.overload
    def updateNCharacterStream(self, int: int, reader: java.io.Reader, long: int) -> None: ...
    @typing.overload
    def updateNCharacterStream(self, string: str, reader: java.io.Reader) -> None: ...
    @typing.overload
    def updateNCharacterStream(self, string: str, reader: java.io.Reader, long: int) -> None: ...
    @typing.overload
    def updateNClob(self, int: int, reader: java.io.Reader) -> None: ...
    @typing.overload
    def updateNClob(self, int: int, reader: java.io.Reader, long: int) -> None: ...
    @typing.overload
    def updateNClob(self, int: int, nClob: java.sql.NClob) -> None: ...
    @typing.overload
    def updateNClob(self, string: str, reader: java.io.Reader) -> None: ...
    @typing.overload
    def updateNClob(self, string: str, reader: java.io.Reader, long: int) -> None: ...
    @typing.overload
    def updateNClob(self, string: str, nClob: java.sql.NClob) -> None: ...
    @typing.overload
    def updateNString(self, int: int, string: str) -> None: ...
    @typing.overload
    def updateNString(self, string: str, string2: str) -> None: ...
    @typing.overload
    def updateNull(self, int: int) -> None: ...
    @typing.overload
    def updateNull(self, string: str) -> None: ...
    @typing.overload
    def updateObject(self, int: int, object: typing.Any, sQLType: java.sql.SQLType) -> None: ...
    @typing.overload
    def updateObject(self, int: int, object: typing.Any, sQLType: java.sql.SQLType, int2: int) -> None: ...
    @typing.overload
    def updateObject(self, string: str, object: typing.Any, sQLType: java.sql.SQLType) -> None: ...
    @typing.overload
    def updateObject(self, string: str, object: typing.Any, sQLType: java.sql.SQLType, int: int) -> None: ...
    @typing.overload
    def updateObject(self, int: int, object: typing.Any) -> None: ...
    @typing.overload
    def updateObject(self, int: int, object: typing.Any, int2: int) -> None: ...
    @typing.overload
    def updateObject(self, string: str, object: typing.Any) -> None: ...
    @typing.overload
    def updateObject(self, string: str, object: typing.Any, int: int) -> None: ...
    @typing.overload
    def updateRef(self, int: int, ref: java.sql.Ref) -> None: ...
    @typing.overload
    def updateRef(self, string: str, ref: java.sql.Ref) -> None: ...
    def updateRow(self) -> None: ...
    @typing.overload
    def updateRowId(self, int: int, rowId: java.sql.RowId) -> None: ...
    @typing.overload
    def updateRowId(self, string: str, rowId: java.sql.RowId) -> None: ...
    @typing.overload
    def updateSQLXML(self, int: int, sQLXML: java.sql.SQLXML) -> None: ...
    @typing.overload
    def updateSQLXML(self, string: str, sQLXML: java.sql.SQLXML) -> None: ...
    @typing.overload
    def updateShort(self, int: int, short: int) -> None: ...
    @typing.overload
    def updateShort(self, string: str, short: int) -> None: ...
    @typing.overload
    def updateString(self, int: int, string: str) -> None: ...
    @typing.overload
    def updateString(self, string: str, string2: str) -> None: ...
    @typing.overload
    def updateTime(self, int: int, time: typing.Union[java.sql.Time, datetime.time]) -> None: ...
    @typing.overload
    def updateTime(self, string: str, time: typing.Union[java.sql.Time, datetime.time]) -> None: ...
    @typing.overload
    def updateTimestamp(self, int: int, timestamp: typing.Union[java.sql.Timestamp, datetime.datetime]) -> None: ...
    @typing.overload
    def updateTimestamp(self, string: str, timestamp: typing.Union[java.sql.Timestamp, datetime.datetime]) -> None: ...
    def wasNull(self) -> bool: ...

class StatementWrapper(java.sql.Statement):
    def __init__(self, statement: java.sql.Statement, connectionWrapper: ConnectionWrapper): ...
    def addBatch(self, string: str) -> None: ...
    def cancel(self) -> None: ...
    def clearBatch(self) -> None: ...
    def clearWarnings(self) -> None: ...
    def close(self) -> None: ...
    def closeOnCompletion(self) -> None: ...
    @typing.overload
    def execute(self, string: str) -> bool: ...
    @typing.overload
    def execute(self, string: str, int: int) -> bool: ...
    @typing.overload
    def execute(self, string: str, intArray: typing.Union[typing.List[int], jpype.JArray]) -> bool: ...
    @typing.overload
    def execute(self, string: str, stringArray: typing.Union[typing.List[str], jpype.JArray]) -> bool: ...
    def executeBatch(self) -> typing.MutableSequence[int]: ...
    def executeQuery(self, string: str) -> java.sql.ResultSet: ...
    @typing.overload
    def executeUpdate(self, string: str) -> int: ...
    @typing.overload
    def executeUpdate(self, string: str, int: int) -> int: ...
    @typing.overload
    def executeUpdate(self, string: str, intArray: typing.Union[typing.List[int], jpype.JArray]) -> int: ...
    @typing.overload
    def executeUpdate(self, string: str, stringArray: typing.Union[typing.List[str], jpype.JArray]) -> int: ...
    def getConnection(self) -> java.sql.Connection: ...
    def getFetchDirection(self) -> int: ...
    def getFetchSize(self) -> int: ...
    def getGeneratedKeys(self) -> java.sql.ResultSet: ...
    def getMaxFieldSize(self) -> int: ...
    def getMaxRows(self) -> int: ...
    @typing.overload
    def getMoreResults(self) -> bool: ...
    @typing.overload
    def getMoreResults(self, int: int) -> bool: ...
    def getQueryTimeout(self) -> int: ...
    def getResultSet(self) -> java.sql.ResultSet: ...
    def getResultSetConcurrency(self) -> int: ...
    def getResultSetHoldability(self) -> int: ...
    def getResultSetType(self) -> int: ...
    def getUpdateCount(self) -> int: ...
    def getWarnings(self) -> java.sql.SQLWarning: ...
    def isCloseOnCompletion(self) -> bool: ...
    def isClosed(self) -> bool: ...
    def isPoolable(self) -> bool: ...
    def isWrapperFor(self, class_: typing.Type[typing.Any]) -> bool: ...
    def setCursorName(self, string: str) -> None: ...
    def setEscapeProcessing(self, boolean: bool) -> None: ...
    def setFetchDirection(self, int: int) -> None: ...
    def setFetchSize(self, int: int) -> None: ...
    def setMaxFieldSize(self, int: int) -> None: ...
    def setMaxRows(self, int: int) -> None: ...
    def setPoolable(self, boolean: bool) -> None: ...
    def setQueryTimeout(self, int: int) -> None: ...
    _unwrap__T = typing.TypeVar('_unwrap__T')  # <T>
    def unwrap(self, class_: typing.Type[_unwrap__T]) -> _unwrap__T: ...

class PreparedStatementWrapper(StatementWrapper, java.sql.PreparedStatement):
    def __init__(self, preparedStatement: java.sql.PreparedStatement, connectionWrapper: ConnectionWrapper): ...
    @typing.overload
    def addBatch(self) -> None: ...
    @typing.overload
    def addBatch(self, string: str) -> None: ...
    def clearParameters(self) -> None: ...
    @typing.overload
    def execute(self) -> bool: ...
    @typing.overload
    def execute(self, string: str) -> bool: ...
    @typing.overload
    def execute(self, string: str, int: int) -> bool: ...
    @typing.overload
    def execute(self, string: str, intArray: typing.Union[typing.List[int], jpype.JArray]) -> bool: ...
    @typing.overload
    def execute(self, string: str, stringArray: typing.Union[typing.List[str], jpype.JArray]) -> bool: ...
    @typing.overload
    def executeQuery(self) -> java.sql.ResultSet: ...
    @typing.overload
    def executeQuery(self, string: str) -> java.sql.ResultSet: ...
    @typing.overload
    def executeUpdate(self) -> int: ...
    @typing.overload
    def executeUpdate(self, string: str) -> int: ...
    @typing.overload
    def executeUpdate(self, string: str, int: int) -> int: ...
    @typing.overload
    def executeUpdate(self, string: str, intArray: typing.Union[typing.List[int], jpype.JArray]) -> int: ...
    @typing.overload
    def executeUpdate(self, string: str, stringArray: typing.Union[typing.List[str], jpype.JArray]) -> int: ...
    def getMetaData(self) -> java.sql.ResultSetMetaData: ...
    def getParameterMetaData(self) -> java.sql.ParameterMetaData: ...
    def setArray(self, int: int, array: java.sql.Array) -> None: ...
    @typing.overload
    def setAsciiStream(self, int: int, inputStream: java.io.InputStream) -> None: ...
    @typing.overload
    def setAsciiStream(self, int: int, inputStream: java.io.InputStream, int2: int) -> None: ...
    @typing.overload
    def setAsciiStream(self, int: int, inputStream: java.io.InputStream, long: int) -> None: ...
    def setBigDecimal(self, int: int, bigDecimal: typing.Union[java.math.BigDecimal, decimal.Decimal]) -> None: ...
    @typing.overload
    def setBinaryStream(self, int: int, inputStream: java.io.InputStream) -> None: ...
    @typing.overload
    def setBinaryStream(self, int: int, inputStream: java.io.InputStream, int2: int) -> None: ...
    @typing.overload
    def setBinaryStream(self, int: int, inputStream: java.io.InputStream, long: int) -> None: ...
    @typing.overload
    def setBlob(self, int: int, inputStream: java.io.InputStream) -> None: ...
    @typing.overload
    def setBlob(self, int: int, inputStream: java.io.InputStream, long: int) -> None: ...
    @typing.overload
    def setBlob(self, int: int, blob: java.sql.Blob) -> None: ...
    def setBoolean(self, int: int, boolean: bool) -> None: ...
    def setByte(self, int: int, byte: int) -> None: ...
    def setBytes(self, int: int, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> None: ...
    @typing.overload
    def setCharacterStream(self, int: int, reader: java.io.Reader) -> None: ...
    @typing.overload
    def setCharacterStream(self, int: int, reader: java.io.Reader, int2: int) -> None: ...
    @typing.overload
    def setCharacterStream(self, int: int, reader: java.io.Reader, long: int) -> None: ...
    @typing.overload
    def setClob(self, int: int, reader: java.io.Reader) -> None: ...
    @typing.overload
    def setClob(self, int: int, reader: java.io.Reader, long: int) -> None: ...
    @typing.overload
    def setClob(self, int: int, clob: java.sql.Clob) -> None: ...
    @typing.overload
    def setDate(self, int: int, date: typing.Union[java.sql.Date, datetime.date]) -> None: ...
    @typing.overload
    def setDate(self, int: int, date: typing.Union[java.sql.Date, datetime.date], calendar: java.util.Calendar) -> None: ...
    def setDouble(self, int: int, double: float) -> None: ...
    def setFloat(self, int: int, float: float) -> None: ...
    def setInt(self, int: int, int2: int) -> None: ...
    def setLong(self, int: int, long: int) -> None: ...
    @typing.overload
    def setNCharacterStream(self, int: int, reader: java.io.Reader) -> None: ...
    @typing.overload
    def setNCharacterStream(self, int: int, reader: java.io.Reader, long: int) -> None: ...
    @typing.overload
    def setNClob(self, int: int, reader: java.io.Reader) -> None: ...
    @typing.overload
    def setNClob(self, int: int, reader: java.io.Reader, long: int) -> None: ...
    @typing.overload
    def setNClob(self, int: int, nClob: java.sql.NClob) -> None: ...
    def setNString(self, int: int, string: str) -> None: ...
    @typing.overload
    def setNull(self, int: int, int2: int) -> None: ...
    @typing.overload
    def setNull(self, int: int, int2: int, string: str) -> None: ...
    @typing.overload
    def setObject(self, int: int, object: typing.Any, sQLType: java.sql.SQLType) -> None: ...
    @typing.overload
    def setObject(self, int: int, object: typing.Any, sQLType: java.sql.SQLType, int2: int) -> None: ...
    @typing.overload
    def setObject(self, int: int, object: typing.Any) -> None: ...
    @typing.overload
    def setObject(self, int: int, object: typing.Any, int2: int) -> None: ...
    @typing.overload
    def setObject(self, int: int, object: typing.Any, int2: int, int3: int) -> None: ...
    def setRef(self, int: int, ref: java.sql.Ref) -> None: ...
    def setRowId(self, int: int, rowId: java.sql.RowId) -> None: ...
    def setSQLXML(self, int: int, sQLXML: java.sql.SQLXML) -> None: ...
    def setShort(self, int: int, short: int) -> None: ...
    def setString(self, int: int, string: str) -> None: ...
    @typing.overload
    def setTime(self, int: int, time: typing.Union[java.sql.Time, datetime.time]) -> None: ...
    @typing.overload
    def setTime(self, int: int, time: typing.Union[java.sql.Time, datetime.time], calendar: java.util.Calendar) -> None: ...
    @typing.overload
    def setTimestamp(self, int: int, timestamp: typing.Union[java.sql.Timestamp, datetime.datetime]) -> None: ...
    @typing.overload
    def setTimestamp(self, int: int, timestamp: typing.Union[java.sql.Timestamp, datetime.datetime], calendar: java.util.Calendar) -> None: ...
    def setURL(self, int: int, uRL: java.net.URL) -> None: ...
    def setUnicodeStream(self, int: int, inputStream: java.io.InputStream, int2: int) -> None: ...

class SpatialResultSetImpl(ResultSetWrapper, org.h2gis.utilities.SpatialResultSet):
    def __init__(self, resultSet: java.sql.ResultSet, statementWrapper: StatementWrapper): ...
    @typing.overload
    def getGeometry(self) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    def getGeometry(self, int: int) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    def getGeometry(self, string: str) -> org.locationtech.jts.geom.Geometry: ...
    _unwrap__T = typing.TypeVar('_unwrap__T')  # <T>
    def unwrap(self, class_: typing.Type[_unwrap__T]) -> _unwrap__T: ...
    @typing.overload
    def updateGeometry(self, int: int, geometry: org.locationtech.jts.geom.Geometry) -> None: ...
    @typing.overload
    def updateGeometry(self, string: str, geometry: org.locationtech.jts.geom.Geometry) -> None: ...

class SpatialResultSetMetaDataImpl(ResultSetMetaDataWrapper, org.h2gis.utilities.SpatialResultSetMetaData):
    def __init__(self, resultSetMetaData: java.sql.ResultSetMetaData, statementWrapper: StatementWrapper): ...
    def getFirstGeometryFieldIndex(self) -> int: ...
    @typing.overload
    def getGeometryType(self) -> int: ...
    @typing.overload
    def getGeometryType(self, int: int) -> int: ...
    _unwrap__T = typing.TypeVar('_unwrap__T')  # <T>
    def unwrap(self, class_: typing.Type[_unwrap__T]) -> _unwrap__T: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.utilities.wrapper")``.

    ConnectionWrapper: typing.Type[ConnectionWrapper]
    DataSourceWrapper: typing.Type[DataSourceWrapper]
    PreparedStatementWrapper: typing.Type[PreparedStatementWrapper]
    ResultSetMetaDataWrapper: typing.Type[ResultSetMetaDataWrapper]
    ResultSetWrapper: typing.Type[ResultSetWrapper]
    SpatialResultSetImpl: typing.Type[SpatialResultSetImpl]
    SpatialResultSetMetaDataImpl: typing.Type[SpatialResultSetMetaDataImpl]
    StatementWrapper: typing.Type[StatementWrapper]
