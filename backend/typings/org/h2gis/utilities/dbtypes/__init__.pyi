
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.net
import java.sql
import java.util
import java.util.regex
import typing



class Constants:
    H2_JDBC_PROTOCOL: typing.ClassVar[str] = ...
    POSTGRESQL_JDBC_PROTOCOL: typing.ClassVar[str] = ...
    POSTGRESQL_H2_JDBC_PROTOCOL: typing.ClassVar[str] = ...
    POSTGIS_JDBC_PROTOCOL: typing.ClassVar[str] = ...
    H2_JDBC_NAME: typing.ClassVar[str] = ...
    POSTGRESQL_JDBC_NAME: typing.ClassVar[str] = ...
    SCHEME_DBTYPE_MAP: typing.ClassVar[java.util.Map] = ...
    DB_NAME_TYPE_MAP: typing.ClassVar[java.util.Map] = ...
    driverDBTypeMap: typing.ClassVar[java.util.Map] = ...
    H2_SPECIAL_NAME_PATTERN: typing.ClassVar[java.util.regex.Pattern] = ...
    POSTGRESQL_SPECIAL_NAME_PATTERN: typing.ClassVar[java.util.regex.Pattern] = ...
    H2_RESERVED_WORDS: typing.ClassVar[java.util.Set] = ...
    POSTGRESQL_RESERVED_WORDS: typing.ClassVar[java.util.Set] = ...
    def __init__(self): ...

class DBTypes(java.lang.Enum['DBTypes']):
    POSTGRESQL: typing.ClassVar['DBTypes'] = ...
    POSTGIS: typing.ClassVar['DBTypes'] = ...
    H2: typing.ClassVar['DBTypes'] = ...
    H2GIS: typing.ClassVar['DBTypes'] = ...
    UNKNOWN: typing.ClassVar['DBTypes'] = ...
    def getReservedWords(self) -> java.util.Set[str]: ...
    def specialNamePattern(self) -> java.util.regex.Pattern: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'DBTypes': ...
    @staticmethod
    def values() -> typing.MutableSequence['DBTypes']: ...

class DBUtils:
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def getDBType(string: str) -> DBTypes: ...
    @typing.overload
    @staticmethod
    def getDBType(uRI: java.net.URI) -> DBTypes: ...
    @typing.overload
    @staticmethod
    def getDBType(connection: java.sql.Connection) -> DBTypes: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.utilities.dbtypes")``.

    Constants: typing.Type[Constants]
    DBTypes: typing.Type[DBTypes]
    DBUtils: typing.Type[DBUtils]
