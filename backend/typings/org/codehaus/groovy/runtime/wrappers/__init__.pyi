
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import groovy.lang
import typing



class Wrapper(groovy.lang.GroovyObject):
    def __init__(self, class_: typing.Type): ...
    def getMetaClass(self) -> groovy.lang.MetaClass: ...
    def getType(self) -> typing.Type: ...
    def unwrap(self) -> typing.Any: ...

class GroovyObjectWrapper(Wrapper):
    def __init__(self, groovyObject: groovy.lang.GroovyObject, class_: typing.Type): ...
    def getProperty(self, string: str) -> typing.Any: ...
    def invokeMethod(self, string: str, object: typing.Any) -> typing.Any: ...
    def setMetaClass(self, metaClass: groovy.lang.MetaClass) -> None: ...
    def setProperty(self, string: str, object: typing.Any) -> None: ...
    def unwrap(self) -> typing.Any: ...

class PojoWrapper(Wrapper):
    def __init__(self, object: typing.Any, class_: typing.Type): ...
    def getProperty(self, string: str) -> typing.Any: ...
    def invokeMethod(self, string: str, object: typing.Any) -> typing.Any: ...
    def setMetaClass(self, metaClass: groovy.lang.MetaClass) -> None: ...
    def setProperty(self, string: str, object: typing.Any) -> None: ...
    def unwrap(self) -> typing.Any: ...

class BooleanWrapper(PojoWrapper):
    def __init__(self, boolean: bool): ...

class ByteWrapper(PojoWrapper):
    def __init__(self, byte: int): ...

class CharWrapper(PojoWrapper):
    def __init__(self, char: str): ...

class DoubleWrapper(PojoWrapper):
    def __init__(self, double: float): ...

class FloatWrapper(PojoWrapper):
    def __init__(self, float: float): ...

class IntWrapper(PojoWrapper):
    def __init__(self, int: int): ...

class LongWrapper(PojoWrapper):
    def __init__(self, long: int): ...

class ShortWrapper(PojoWrapper):
    def __init__(self, short: int): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.runtime.wrappers")``.

    BooleanWrapper: typing.Type[BooleanWrapper]
    ByteWrapper: typing.Type[ByteWrapper]
    CharWrapper: typing.Type[CharWrapper]
    DoubleWrapper: typing.Type[DoubleWrapper]
    FloatWrapper: typing.Type[FloatWrapper]
    GroovyObjectWrapper: typing.Type[GroovyObjectWrapper]
    IntWrapper: typing.Type[IntWrapper]
    LongWrapper: typing.Type[LongWrapper]
    PojoWrapper: typing.Type[PojoWrapper]
    ShortWrapper: typing.Type[ShortWrapper]
    Wrapper: typing.Type[Wrapper]