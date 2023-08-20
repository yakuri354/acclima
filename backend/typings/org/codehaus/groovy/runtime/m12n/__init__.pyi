
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import groovy.lang
import java.lang
import java.util
import typing



class ExtensionModule:
    def __init__(self, string: str, string2: str): ...
    def getMetaMethods(self) -> java.util.List[groovy.lang.MetaMethod]: ...
    def getName(self) -> str: ...
    def getVersion(self) -> str: ...
    def toString(self) -> str: ...

class ExtensionModuleRegistry:
    def __init__(self): ...
    def addModule(self, extensionModule: ExtensionModule) -> None: ...
    def getModule(self, string: str) -> ExtensionModule: ...
    def getModules(self) -> java.util.List[ExtensionModule]: ...
    def hasModule(self, string: str) -> bool: ...
    def removeModule(self, extensionModule: ExtensionModule) -> None: ...

class ExtensionModuleScanner:
    LEGACY_MODULE_META_INF_FILE: typing.ClassVar[str] = ...
    MODULE_META_INF_FILE: typing.ClassVar[str] = ...
    def __init__(self, extensionModuleListener: 'ExtensionModuleScanner.ExtensionModuleListener', classLoader: java.lang.ClassLoader): ...
    def scanClasspathModules(self) -> None: ...
    def scanExtensionModuleFromProperties(self, properties: java.util.Properties) -> None: ...
    class ExtensionModuleListener:
        def onModule(self, extensionModule: ExtensionModule) -> None: ...

class PropertiesModuleFactory:
    MODULE_NAME_KEY: typing.ClassVar[str] = ...
    MODULE_VERSION_KEY: typing.ClassVar[str] = ...
    def __init__(self): ...
    def newModule(self, properties: java.util.Properties, classLoader: java.lang.ClassLoader) -> ExtensionModule: ...

class SimpleExtensionModule(ExtensionModule):
    def __init__(self, string: str, string2: str): ...
    def getInstanceMethodsExtensionClasses(self) -> java.util.List[typing.Type]: ...
    def getMetaMethods(self) -> java.util.List[groovy.lang.MetaMethod]: ...
    def getStaticMethodsExtensionClasses(self) -> java.util.List[typing.Type]: ...

class StandardPropertiesModuleFactory(PropertiesModuleFactory):
    MODULE_FACTORY_KEY: typing.ClassVar[str] = ...
    def __init__(self): ...
    def newModule(self, properties: java.util.Properties, classLoader: java.lang.ClassLoader) -> ExtensionModule: ...

class MetaInfExtensionModule(SimpleExtensionModule):
    MODULE_INSTANCE_CLASSES_KEY: typing.ClassVar[str] = ...
    MODULE_STATIC_CLASSES_KEY: typing.ClassVar[str] = ...
    def getInstanceMethodsExtensionClasses(self) -> java.util.List[typing.Type]: ...
    def getStaticMethodsExtensionClasses(self) -> java.util.List[typing.Type]: ...
    @staticmethod
    def newModule(properties: java.util.Properties, classLoader: java.lang.ClassLoader) -> 'MetaInfExtensionModule': ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.runtime.m12n")``.

    ExtensionModule: typing.Type[ExtensionModule]
    ExtensionModuleRegistry: typing.Type[ExtensionModuleRegistry]
    ExtensionModuleScanner: typing.Type[ExtensionModuleScanner]
    MetaInfExtensionModule: typing.Type[MetaInfExtensionModule]
    PropertiesModuleFactory: typing.Type[PropertiesModuleFactory]
    SimpleExtensionModule: typing.Type[SimpleExtensionModule]
    StandardPropertiesModuleFactory: typing.Type[StandardPropertiesModuleFactory]