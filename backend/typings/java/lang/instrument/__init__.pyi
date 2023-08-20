
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.security
import java.util
import java.util.jar
import jpype
import typing



class ClassDefinition:
    def __init__(self, class_: typing.Type[typing.Any], byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]): ...
    def getDefinitionClass(self) -> typing.Type[typing.Any]: ...
    def getDefinitionClassFile(self) -> typing.MutableSequence[int]: ...

class ClassFileTransformer:
    @typing.overload
    def transform(self, classLoader: java.lang.ClassLoader, string: str, class2: typing.Type[typing.Any], protectionDomain: java.security.ProtectionDomain, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> typing.MutableSequence[int]: ...
    @typing.overload
    def transform(self, module: java.lang.Module, classLoader: java.lang.ClassLoader, string: str, class2: typing.Type[typing.Any], protectionDomain: java.security.ProtectionDomain, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> typing.MutableSequence[int]: ...

class IllegalClassFormatException(java.lang.Exception):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class Instrumentation:
    @typing.overload
    def addTransformer(self, classFileTransformer: ClassFileTransformer) -> None: ...
    @typing.overload
    def addTransformer(self, classFileTransformer: ClassFileTransformer, boolean: bool) -> None: ...
    def appendToBootstrapClassLoaderSearch(self, jarFile: java.util.jar.JarFile) -> None: ...
    def appendToSystemClassLoaderSearch(self, jarFile: java.util.jar.JarFile) -> None: ...
    def getAllLoadedClasses(self) -> typing.MutableSequence[typing.Type]: ...
    def getInitiatedClasses(self, classLoader: java.lang.ClassLoader) -> typing.MutableSequence[typing.Type]: ...
    def getObjectSize(self, object: typing.Any) -> int: ...
    def isModifiableClass(self, class_: typing.Type[typing.Any]) -> bool: ...
    def isModifiableModule(self, module: java.lang.Module) -> bool: ...
    def isNativeMethodPrefixSupported(self) -> bool: ...
    def isRedefineClassesSupported(self) -> bool: ...
    def isRetransformClassesSupported(self) -> bool: ...
    def redefineClasses(self, *classDefinition: ClassDefinition) -> None: ...
    def redefineModule(self, module: java.lang.Module, set: java.util.Set[java.lang.Module], map: typing.Union[java.util.Map[str, java.util.Set[java.lang.Module]], typing.Mapping[str, java.util.Set[java.lang.Module]]], map2: typing.Union[java.util.Map[str, java.util.Set[java.lang.Module]], typing.Mapping[str, java.util.Set[java.lang.Module]]], set2: java.util.Set[typing.Type[typing.Any]], map3: typing.Union[java.util.Map[typing.Type[typing.Any], java.util.List[typing.Type[typing.Any]]], typing.Mapping[typing.Type[typing.Any], java.util.List[typing.Type[typing.Any]]]]) -> None: ...
    def removeTransformer(self, classFileTransformer: ClassFileTransformer) -> bool: ...
    def retransformClasses(self, *class_: typing.Type[typing.Any]) -> None: ...
    def setNativeMethodPrefix(self, classFileTransformer: ClassFileTransformer, string: str) -> None: ...

class UnmodifiableClassException(java.lang.Exception):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class UnmodifiableModuleException(java.lang.RuntimeException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.lang.instrument")``.

    ClassDefinition: typing.Type[ClassDefinition]
    ClassFileTransformer: typing.Type[ClassFileTransformer]
    IllegalClassFormatException: typing.Type[IllegalClassFormatException]
    Instrumentation: typing.Type[Instrumentation]
    UnmodifiableClassException: typing.Type[UnmodifiableClassException]
    UnmodifiableModuleException: typing.Type[UnmodifiableModuleException]