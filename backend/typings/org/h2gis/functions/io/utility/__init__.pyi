
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.nio
import java.nio.channels
import java.sql
import java.util
import jpype
import jpype.protocol
import org.h2gis.api
import org.h2gis.utilities
import org.locationtech.jts.geom
import typing



class CoordinatesUtils:
    @staticmethod
    def contains(coordinateArray: typing.Union[typing.List[org.locationtech.jts.geom.Coordinate], jpype.JArray], coordinate2: org.locationtech.jts.geom.Coordinate) -> bool: ...
    @staticmethod
    def contains2D(coordinateArray: typing.Union[typing.List[org.locationtech.jts.geom.Coordinate], jpype.JArray], coordinate2: org.locationtech.jts.geom.Coordinate) -> bool: ...
    @staticmethod
    def contains3D(coordinateArray: typing.Union[typing.List[org.locationtech.jts.geom.Coordinate], jpype.JArray], coordinate2: org.locationtech.jts.geom.Coordinate) -> bool: ...
    @staticmethod
    def getFurthestCoordinate(coordinate: org.locationtech.jts.geom.Coordinate, coordinateArray: typing.Union[typing.List[org.locationtech.jts.geom.Coordinate], jpype.JArray]) -> typing.MutableSequence[org.locationtech.jts.geom.Coordinate]: ...
    @staticmethod
    def interpolate(coordinate: org.locationtech.jts.geom.Coordinate, coordinate2: org.locationtech.jts.geom.Coordinate, coordinate3: org.locationtech.jts.geom.Coordinate) -> float: ...
    @typing.overload
    @staticmethod
    def length3D(coordinateSequence: org.locationtech.jts.geom.CoordinateSequence) -> float: ...
    @typing.overload
    @staticmethod
    def length3D(geometry: org.locationtech.jts.geom.Geometry) -> float: ...
    @typing.overload
    @staticmethod
    def length3D(lineString: org.locationtech.jts.geom.LineString) -> float: ...
    @typing.overload
    @staticmethod
    def length3D(polygon: org.locationtech.jts.geom.Polygon) -> float: ...
    @staticmethod
    def zMinMax(coordinateArray: typing.Union[typing.List[org.locationtech.jts.geom.Coordinate], jpype.JArray]) -> typing.MutableSequence[float]: ...

class IOMethods:
    def __init__(self): ...
    def addDriver(self, driverFunction: org.h2gis.api.DriverFunction) -> None: ...
    @staticmethod
    def exportToDataBase(connection: java.sql.Connection, string: str, connection2: java.sql.Connection, string2: str, int: int, int2: int) -> str: ...
    def exportToFile(self, connection: java.sql.Connection, string: str, string2: str, string3: str, boolean: bool) -> typing.MutableSequence[str]: ...
    def getAllExportDriverSupportedExtensions(self) -> java.util.List[str]: ...
    def getAllImportDriverSupportedExtensions(self) -> java.util.List[str]: ...
    def getDriverFunctionList(self) -> java.util.List[org.h2gis.api.DriverFunction]: ...
    def getExportDriverFromFile(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> org.h2gis.api.DriverFunction: ...
    def getImportDriverFromFile(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> org.h2gis.api.DriverFunction: ...
    def importFile(self, connection: java.sql.Connection, string: str, string2: str, string3: str, boolean: bool) -> typing.MutableSequence[str]: ...
    @staticmethod
    def linkedFile(connection: java.sql.Connection, string: str, string2: str, boolean: bool) -> str: ...
    @typing.overload
    @staticmethod
    def linkedTable(connection: java.sql.Connection, map: typing.Union[java.util.Map[str, str], typing.Mapping[str, str]], string: str, string2: str, boolean: bool) -> str: ...
    @typing.overload
    @staticmethod
    def linkedTable(connection: java.sql.Connection, map: typing.Union[java.util.Map[str, str], typing.Mapping[str, str]], string: str, string2: str, boolean: bool, int: int) -> str: ...
    @typing.overload
    @staticmethod
    def linkedTable(connection: java.sql.Connection, properties: java.util.Properties, string: str, string2: str, boolean: bool) -> str: ...
    @typing.overload
    @staticmethod
    def linkedTable(connection: java.sql.Connection, properties: java.util.Properties, string: str, string2: str, boolean: bool, int: int) -> str: ...
    def removeDriver(self, driverFunction: org.h2gis.api.DriverFunction) -> None: ...

class PRJUtil:
    def __init__(self): ...
    @staticmethod
    def getSRID(file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> int: ...
    @staticmethod
    def getValidSRID(connection: java.sql.Connection, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> int: ...
    @staticmethod
    def isSRIDValid(int: int, connection: java.sql.Connection) -> bool: ...
    @typing.overload
    @staticmethod
    def writePRJ(connection: java.sql.Connection, int: int, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> None: ...
    @typing.overload
    @staticmethod
    def writePRJ(connection: java.sql.Connection, tableLocation: org.h2gis.utilities.TableLocation, string: str, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> None: ...

class ReadBufferManager:
    @typing.overload
    def __init__(self, fileChannel: java.nio.channels.FileChannel): ...
    @typing.overload
    def __init__(self, fileChannel: java.nio.channels.FileChannel, int: int): ...
    @typing.overload
    def get(self) -> int: ...
    @typing.overload
    def get(self, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> java.nio.ByteBuffer: ...
    @typing.overload
    def get(self, long: int, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> java.nio.ByteBuffer: ...
    def getByte(self, long: int) -> int: ...
    @typing.overload
    def getDouble(self) -> float: ...
    @typing.overload
    def getDouble(self, long: int) -> float: ...
    @typing.overload
    def getInt(self) -> int: ...
    @typing.overload
    def getInt(self, long: int) -> int: ...
    def getLength(self) -> int: ...
    @typing.overload
    def getLong(self) -> int: ...
    @typing.overload
    def getLong(self, long: int) -> int: ...
    def getPosition(self) -> int: ...
    def isEOF(self) -> bool: ...
    def order(self, byteOrder: java.nio.ByteOrder) -> None: ...
    def position(self, long: int) -> None: ...
    def remaining(self) -> int: ...
    def skip(self, int: int) -> None: ...

class WriteBufferManager:
    def __init__(self, fileChannel: java.nio.channels.FileChannel): ...
    def flush(self) -> None: ...
    def order(self, byteOrder: java.nio.ByteOrder) -> None: ...
    @typing.overload
    def put(self, byte: int) -> None: ...
    @typing.overload
    def put(self, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> None: ...
    def putDouble(self, double: float) -> None: ...
    def putInt(self, int: int) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.functions.io.utility")``.

    CoordinatesUtils: typing.Type[CoordinatesUtils]
    IOMethods: typing.Type[IOMethods]
    PRJUtil: typing.Type[PRJUtil]
    ReadBufferManager: typing.Type[ReadBufferManager]
    WriteBufferManager: typing.Type[WriteBufferManager]
