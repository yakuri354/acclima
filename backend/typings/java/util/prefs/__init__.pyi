
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import jpype
import typing



class BackingStoreException(java.lang.Exception):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class InvalidPreferencesFormatException(java.lang.Exception):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class NodeChangeEvent(java.util.EventObject):
    def __init__(self, preferences: 'Preferences', preferences2: 'Preferences'): ...
    def getChild(self) -> 'Preferences': ...
    def getParent(self) -> 'Preferences': ...

class NodeChangeListener(java.util.EventListener):
    def childAdded(self, nodeChangeEvent: NodeChangeEvent) -> None: ...
    def childRemoved(self, nodeChangeEvent: NodeChangeEvent) -> None: ...

class PreferenceChangeEvent(java.util.EventObject):
    def __init__(self, preferences: 'Preferences', string: str, string2: str): ...
    def getKey(self) -> str: ...
    def getNewValue(self) -> str: ...
    def getNode(self) -> 'Preferences': ...

class PreferenceChangeListener(java.util.EventListener):
    def preferenceChange(self, preferenceChangeEvent: PreferenceChangeEvent) -> None: ...

class Preferences:
    MAX_KEY_LENGTH: typing.ClassVar[int] = ...
    MAX_VALUE_LENGTH: typing.ClassVar[int] = ...
    MAX_NAME_LENGTH: typing.ClassVar[int] = ...
    def absolutePath(self) -> str: ...
    def addNodeChangeListener(self, nodeChangeListener: NodeChangeListener) -> None: ...
    def addPreferenceChangeListener(self, preferenceChangeListener: typing.Union[PreferenceChangeListener, typing.Callable]) -> None: ...
    def childrenNames(self) -> typing.MutableSequence[str]: ...
    def clear(self) -> None: ...
    def exportNode(self, outputStream: java.io.OutputStream) -> None: ...
    def exportSubtree(self, outputStream: java.io.OutputStream) -> None: ...
    def flush(self) -> None: ...
    def get(self, string: str, string2: str) -> str: ...
    def getBoolean(self, string: str, boolean: bool) -> bool: ...
    def getByteArray(self, string: str, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> typing.MutableSequence[int]: ...
    def getDouble(self, string: str, double: float) -> float: ...
    def getFloat(self, string: str, float: float) -> float: ...
    def getInt(self, string: str, int: int) -> int: ...
    def getLong(self, string: str, long: int) -> int: ...
    @staticmethod
    def importPreferences(inputStream: java.io.InputStream) -> None: ...
    def isUserNode(self) -> bool: ...
    def keys(self) -> typing.MutableSequence[str]: ...
    def name(self) -> str: ...
    def node(self, string: str) -> 'Preferences': ...
    def nodeExists(self, string: str) -> bool: ...
    def parent(self) -> 'Preferences': ...
    def put(self, string: str, string2: str) -> None: ...
    def putBoolean(self, string: str, boolean: bool) -> None: ...
    def putByteArray(self, string: str, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> None: ...
    def putDouble(self, string: str, double: float) -> None: ...
    def putFloat(self, string: str, float: float) -> None: ...
    def putInt(self, string: str, int: int) -> None: ...
    def putLong(self, string: str, long: int) -> None: ...
    def remove(self, string: str) -> None: ...
    def removeNode(self) -> None: ...
    def removeNodeChangeListener(self, nodeChangeListener: NodeChangeListener) -> None: ...
    def removePreferenceChangeListener(self, preferenceChangeListener: typing.Union[PreferenceChangeListener, typing.Callable]) -> None: ...
    def sync(self) -> None: ...
    @staticmethod
    def systemNodeForPackage(class_: typing.Type[typing.Any]) -> 'Preferences': ...
    @staticmethod
    def systemRoot() -> 'Preferences': ...
    def toString(self) -> str: ...
    @staticmethod
    def userNodeForPackage(class_: typing.Type[typing.Any]) -> 'Preferences': ...
    @staticmethod
    def userRoot() -> 'Preferences': ...

class PreferencesFactory:
    def systemRoot(self) -> Preferences: ...
    def userRoot(self) -> Preferences: ...

class AbstractPreferences(Preferences):
    def absolutePath(self) -> str: ...
    def addNodeChangeListener(self, nodeChangeListener: NodeChangeListener) -> None: ...
    def addPreferenceChangeListener(self, preferenceChangeListener: typing.Union[PreferenceChangeListener, typing.Callable]) -> None: ...
    def childrenNames(self) -> typing.MutableSequence[str]: ...
    def clear(self) -> None: ...
    def exportNode(self, outputStream: java.io.OutputStream) -> None: ...
    def exportSubtree(self, outputStream: java.io.OutputStream) -> None: ...
    def flush(self) -> None: ...
    def get(self, string: str, string2: str) -> str: ...
    def getBoolean(self, string: str, boolean: bool) -> bool: ...
    def getByteArray(self, string: str, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> typing.MutableSequence[int]: ...
    def getDouble(self, string: str, double: float) -> float: ...
    def getFloat(self, string: str, float: float) -> float: ...
    def getInt(self, string: str, int: int) -> int: ...
    def getLong(self, string: str, long: int) -> int: ...
    def isUserNode(self) -> bool: ...
    def keys(self) -> typing.MutableSequence[str]: ...
    def name(self) -> str: ...
    def node(self, string: str) -> Preferences: ...
    def nodeExists(self, string: str) -> bool: ...
    def parent(self) -> Preferences: ...
    def put(self, string: str, string2: str) -> None: ...
    def putBoolean(self, string: str, boolean: bool) -> None: ...
    def putByteArray(self, string: str, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> None: ...
    def putDouble(self, string: str, double: float) -> None: ...
    def putFloat(self, string: str, float: float) -> None: ...
    def putInt(self, string: str, int: int) -> None: ...
    def putLong(self, string: str, long: int) -> None: ...
    def remove(self, string: str) -> None: ...
    def removeNode(self) -> None: ...
    def removeNodeChangeListener(self, nodeChangeListener: NodeChangeListener) -> None: ...
    def removePreferenceChangeListener(self, preferenceChangeListener: typing.Union[PreferenceChangeListener, typing.Callable]) -> None: ...
    def sync(self) -> None: ...
    def toString(self) -> str: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.util.prefs")``.

    AbstractPreferences: typing.Type[AbstractPreferences]
    BackingStoreException: typing.Type[BackingStoreException]
    InvalidPreferencesFormatException: typing.Type[InvalidPreferencesFormatException]
    NodeChangeEvent: typing.Type[NodeChangeEvent]
    NodeChangeListener: typing.Type[NodeChangeListener]
    PreferenceChangeEvent: typing.Type[PreferenceChangeEvent]
    PreferenceChangeListener: typing.Type[PreferenceChangeListener]
    Preferences: typing.Type[Preferences]
    PreferencesFactory: typing.Type[PreferencesFactory]