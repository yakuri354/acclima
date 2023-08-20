
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import java.util.stream
import jpype
import org.codehaus.groovy.vmplugin.v7
import typing



class Java8(org.codehaus.groovy.vmplugin.v7.Java7):
    def __init__(self): ...
    def getPluginDefaultGroovyMethods(self) -> typing.MutableSequence[typing.Type[typing.Any]]: ...
    def getVersion(self) -> int: ...

class PluginDefaultGroovyMethods:
    @staticmethod
    def asBoolean(optional: java.util.Optional[typing.Any]) -> bool: ...
    _stream_6__T = typing.TypeVar('_stream_6__T')  # <T>
    @typing.overload
    @staticmethod
    def stream(booleanArray: typing.Union[typing.List[bool], jpype.JArray]) -> java.util.stream.Stream[bool]: ...
    @typing.overload
    @staticmethod
    def stream(byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> java.util.stream.Stream[int]: ...
    @typing.overload
    @staticmethod
    def stream(charArray: typing.Union[typing.List[str], jpype.JArray]) -> java.util.stream.Stream[str]: ...
    @typing.overload
    @staticmethod
    def stream(doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> java.util.stream.Stream[float]: ...
    @typing.overload
    @staticmethod
    def stream(floatArray: typing.Union[typing.List[float], jpype.JArray]) -> java.util.stream.Stream[float]: ...
    @typing.overload
    @staticmethod
    def stream(intArray: typing.Union[typing.List[int], jpype.JArray]) -> java.util.stream.Stream[int]: ...
    @typing.overload
    @staticmethod
    def stream(tArray: typing.Union[typing.List[_stream_6__T], jpype.JArray]) -> java.util.stream.Stream[_stream_6__T]: ...
    @typing.overload
    @staticmethod
    def stream(longArray: typing.Union[typing.List[int], jpype.JArray]) -> java.util.stream.Stream[int]: ...
    @typing.overload
    @staticmethod
    def stream(shortArray: typing.Union[typing.List[int], jpype.JArray]) -> java.util.stream.Stream[int]: ...
    _toList_0__T = typing.TypeVar('_toList_0__T')  # <T>
    _toList_1__T = typing.TypeVar('_toList_1__T')  # <T>
    @typing.overload
    @staticmethod
    def toList(baseStream: java.util.stream.BaseStream[_toList_0__T, java.util.stream.BaseStream]) -> java.util.List[_toList_0__T]: ...
    @typing.overload
    @staticmethod
    def toList(stream: java.util.stream.Stream[_toList_1__T]) -> java.util.List[_toList_1__T]: ...
    _toSet_0__T = typing.TypeVar('_toSet_0__T')  # <T>
    _toSet_1__T = typing.TypeVar('_toSet_1__T')  # <T>
    @typing.overload
    @staticmethod
    def toSet(baseStream: java.util.stream.BaseStream[_toSet_0__T, java.util.stream.BaseStream]) -> java.util.Set[_toSet_0__T]: ...
    @typing.overload
    @staticmethod
    def toSet(stream: java.util.stream.Stream[_toSet_1__T]) -> java.util.Set[_toSet_1__T]: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.vmplugin.v8")``.

    Java8: typing.Type[Java8]
    PluginDefaultGroovyMethods: typing.Type[PluginDefaultGroovyMethods]
