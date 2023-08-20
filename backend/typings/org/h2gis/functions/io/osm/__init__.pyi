
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.sql
import java.util
import jpype.protocol
import org.h2.value
import org.h2gis.api
import org.locationtech.jts.geom
import org.xml.sax
import org.xml.sax.helpers
import typing



class OSMDriverFunction(org.h2gis.api.DriverFunction):
    DESCRIPTION: typing.ClassVar[str] = ...
    DESCRIPTION_GZ: typing.ClassVar[str] = ...
    DESCRIPTION_BZ2: typing.ClassVar[str] = ...
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

class OSMElement:
    def __init__(self): ...
    def addTag(self, string: str, string2: str) -> bool: ...
    def getChangeSet(self) -> int: ...
    def getID(self) -> int: ...
    def getName(self) -> str: ...
    def getTags(self) -> java.util.HashMap[str, str]: ...
    def getTimeStamp(self) -> java.sql.Timestamp: ...
    def getUID(self) -> int: ...
    def getUser(self) -> str: ...
    def getVersion(self) -> int: ...
    def getVisible(self) -> bool: ...
    def setChangeset(self, string: str) -> None: ...
    def setId(self, string: str) -> None: ...
    def setName(self, string: str) -> None: ...
    def setTimestamp(self, string: str) -> None: ...
    def setUid(self, string: str) -> None: ...
    def setUser(self, string: str) -> None: ...
    def setVersion(self, string: str) -> None: ...
    def setVisible(self, string: str) -> None: ...

class OSMParser(org.xml.sax.helpers.DefaultHandler):
    def __init__(self, connection: java.sql.Connection, file: typing.Union[java.io.File, jpype.protocol.SupportsPath], string: str, boolean: bool): ...
    def endDocument(self) -> None: ...
    def endElement(self, string: str, string2: str, string3: str) -> None: ...
    def read(self, string: str, progressVisitor: org.h2gis.api.ProgressVisitor) -> typing.MutableSequence[str]: ...
    def startElement(self, string: str, string2: str, string3: str, attributes: org.xml.sax.Attributes) -> None: ...

class OSMPreParser(org.xml.sax.helpers.DefaultHandler):
    def __init__(self): ...
    def getTotalNode(self) -> int: ...
    def getTotalRelation(self) -> int: ...
    def getTotalWay(self) -> int: ...
    def getVersion(self) -> str: ...
    def read(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> bool: ...
    def startElement(self, string: str, string2: str, string3: str, attributes: org.xml.sax.Attributes) -> None: ...

class OSMRead(org.h2gis.api.AbstractFunction, org.h2gis.api.ScalarFunction):
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

class OSMTablesFactory:
    NODE: typing.ClassVar[str] = ...
    WAY: typing.ClassVar[str] = ...
    NODE_TAG: typing.ClassVar[str] = ...
    WAY_TAG: typing.ClassVar[str] = ...
    WAY_NODE: typing.ClassVar[str] = ...
    RELATION: typing.ClassVar[str] = ...
    RELATION_TAG: typing.ClassVar[str] = ...
    NODE_MEMBER: typing.ClassVar[str] = ...
    WAY_MEMBER: typing.ClassVar[str] = ...
    RELATION_MEMBER: typing.ClassVar[str] = ...
    @staticmethod
    def createNodeMemberTable(connection: java.sql.Connection, string: str) -> java.sql.PreparedStatement: ...
    @staticmethod
    def createNodeTable(connection: java.sql.Connection, string: str) -> java.sql.PreparedStatement: ...
    @staticmethod
    def createNodeTagTable(connection: java.sql.Connection, string: str) -> java.sql.PreparedStatement: ...
    @staticmethod
    def createRelationMemberTable(connection: java.sql.Connection, string: str) -> java.sql.PreparedStatement: ...
    @staticmethod
    def createRelationTable(connection: java.sql.Connection, string: str) -> java.sql.PreparedStatement: ...
    @staticmethod
    def createRelationTagTable(connection: java.sql.Connection, string: str) -> java.sql.PreparedStatement: ...
    @staticmethod
    def createWayMemberTable(connection: java.sql.Connection, string: str) -> java.sql.PreparedStatement: ...
    @staticmethod
    def createWayNodeTable(connection: java.sql.Connection, string: str) -> java.sql.PreparedStatement: ...
    @staticmethod
    def createWayTable(connection: java.sql.Connection, string: str) -> java.sql.PreparedStatement: ...
    @staticmethod
    def createWayTagTable(connection: java.sql.Connection, string: str) -> java.sql.PreparedStatement: ...
    @staticmethod
    def dropOSMTables(connection: java.sql.Connection, string: str) -> None: ...

class OSMTags:
    USER: typing.ClassVar[str] = ...
    UID: typing.ClassVar[str] = ...
    VISIBLE: typing.ClassVar[str] = ...
    VERSION: typing.ClassVar[str] = ...
    CHANGE_SET: typing.ClassVar[str] = ...
    TIMESTAMP: typing.ClassVar[str] = ...
    NODEFIELDCOUNT: typing.ClassVar[int] = ...
    WAYFIELDCOUNT: typing.ClassVar[int] = ...
    def __init__(self): ...

class ST_OSMDownloader(org.h2gis.api.AbstractFunction, org.h2gis.api.ScalarFunction):
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def downloadData(connection: java.sql.Connection, geometry: org.locationtech.jts.geom.Geometry, string: str) -> None: ...
    @typing.overload
    @staticmethod
    def downloadData(connection: java.sql.Connection, geometry: org.locationtech.jts.geom.Geometry, string: str, boolean: bool) -> None: ...
    @staticmethod
    def downloadOSMFile(file: typing.Union[java.io.File, jpype.protocol.SupportsPath], envelope: org.locationtech.jts.geom.Envelope) -> None: ...
    def getJavaStaticMethod(self) -> str: ...

class TAG_LOCATION(java.lang.Enum['TAG_LOCATION']):
    NODE: typing.ClassVar['TAG_LOCATION'] = ...
    WAY: typing.ClassVar['TAG_LOCATION'] = ...
    OTHER: typing.ClassVar['TAG_LOCATION'] = ...
    RELATION: typing.ClassVar['TAG_LOCATION'] = ...
    ND: typing.ClassVar['TAG_LOCATION'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'TAG_LOCATION': ...
    @staticmethod
    def values() -> typing.MutableSequence['TAG_LOCATION']: ...

class NodeOSMElement(OSMElement):
    def __init__(self, double: float, double2: float): ...
    def addTag(self, string: str, string2: str) -> bool: ...
    def getElevation(self) -> float: ...
    def getPoint(self, geometryFactory: org.locationtech.jts.geom.GeometryFactory) -> org.locationtech.jts.geom.Point: ...
    def setElevation(self, double: float) -> None: ...

class WayOSMElement(OSMElement):
    def __init__(self): ...
    def addRef(self, string: str) -> None: ...
    def getNodesRef(self) -> java.util.List[int]: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.functions.io.osm")``.

    NodeOSMElement: typing.Type[NodeOSMElement]
    OSMDriverFunction: typing.Type[OSMDriverFunction]
    OSMElement: typing.Type[OSMElement]
    OSMParser: typing.Type[OSMParser]
    OSMPreParser: typing.Type[OSMPreParser]
    OSMRead: typing.Type[OSMRead]
    OSMTablesFactory: typing.Type[OSMTablesFactory]
    OSMTags: typing.Type[OSMTags]
    ST_OSMDownloader: typing.Type[ST_OSMDownloader]
    TAG_LOCATION: typing.Type[TAG_LOCATION]
    WayOSMElement: typing.Type[WayOSMElement]