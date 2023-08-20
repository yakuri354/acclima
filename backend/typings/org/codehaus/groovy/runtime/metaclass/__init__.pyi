
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import groovy.lang
import java.io
import java.lang
import java.lang.reflect
import java.security
import java.util
import jpype
import org
import org.codehaus.groovy.ast
import org.codehaus.groovy.reflection
import org.codehaus.groovy.runtime
import org.codehaus.groovy.runtime.callsite
import org.codehaus.groovy.runtime.m12n
import org.codehaus.groovy.util
import typing



class ClosureMetaClass(groovy.lang.MetaClassImpl):
    def __init__(self, metaClassRegistry: groovy.lang.MetaClassRegistry, class_: typing.Type): ...
    def addMetaBeanProperty(self, metaBeanProperty: groovy.lang.MetaBeanProperty) -> None: ...
    def addMetaMethod(self, metaMethod: groovy.lang.MetaMethod) -> None: ...
    def addNewInstanceMethod(self, method: java.lang.reflect.Method) -> None: ...
    def addNewStaticMethod(self, method: java.lang.reflect.Method) -> None: ...
    def createPogoCallCurrentSite(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, class_: typing.Type, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createPogoCallSite(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createPojoCallSite(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    @typing.overload
    def getAttribute(self, class_: typing.Type, object: typing.Any, string: str, boolean: bool) -> typing.Any: ...
    @typing.overload
    def getAttribute(self, object: typing.Any, string: str) -> typing.Any: ...
    @typing.overload
    def getAttribute(self, class_: typing.Type, object: typing.Any, string: str, boolean: bool, boolean2: bool) -> typing.Any: ...
    def getMetaMethods(self) -> java.util.List[groovy.lang.MetaMethod]: ...
    def getMetaProperty(self, string: str) -> groovy.lang.MetaProperty: ...
    @typing.overload
    def getMethodWithoutCaching(self, class_: typing.Type, string: str, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], boolean: bool) -> groovy.lang.MetaMethod: ...
    @typing.overload
    def getMethodWithoutCaching(self, int: int, class_: typing.Type, string: str, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], boolean: bool) -> groovy.lang.MetaMethod: ...
    def getMethods(self) -> java.util.List[groovy.lang.MetaMethod]: ...
    def getProperties(self) -> java.util.List[groovy.lang.MetaProperty]: ...
    @typing.overload
    def getProperty(self, object: typing.Any, string: str) -> typing.Any: ...
    @typing.overload
    def getProperty(self, class_: typing.Type, object: typing.Any, string: str, boolean: bool, boolean2: bool) -> typing.Any: ...
    @typing.overload
    def getStaticMetaMethod(self, string: str, classArray: typing.Union[typing.List[typing.Type], jpype.JArray]) -> groovy.lang.MetaMethod: ...
    @typing.overload
    def getStaticMetaMethod(self, string: str, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> groovy.lang.MetaMethod: ...
    def initialize(self) -> None: ...
    @typing.overload
    def invokeMethod(self, object: typing.Any, string: str, object2: typing.Any) -> typing.Any: ...
    @typing.overload
    def invokeMethod(self, object: typing.Any, string: str, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> typing.Any: ...
    @typing.overload
    def invokeMethod(self, class_: typing.Type, object: typing.Any, string: str, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray], boolean: bool, boolean2: bool) -> typing.Any: ...
    def invokeStaticMethod(self, object: typing.Any, string: str, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> typing.Any: ...
    def pickMethod(self, string: str, classArray: typing.Union[typing.List[typing.Type], jpype.JArray]) -> groovy.lang.MetaMethod: ...
    @staticmethod
    def resetCachedMetaClasses() -> None: ...
    @typing.overload
    def respondsTo(self, object: typing.Any, string: str) -> java.util.List: ...
    @typing.overload
    def respondsTo(self, object: typing.Any, string: str, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> java.util.List: ...
    @typing.overload
    def retrieveConstructor(self, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> groovy.lang.MetaMethod: ...
    @typing.overload
    def retrieveConstructor(self, classArray: typing.Union[typing.List[typing.Type], jpype.JArray]) -> java.lang.reflect.Constructor: ...
    @typing.overload
    def retrieveStaticMethod(self, string: str, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> groovy.lang.MetaMethod: ...
    @typing.overload
    def retrieveStaticMethod(self, string: str, classArray: typing.Union[typing.List[typing.Type], jpype.JArray]) -> groovy.lang.MetaMethod: ...
    @typing.overload
    def setAttribute(self, object: typing.Any, string: str, object2: typing.Any) -> None: ...
    @typing.overload
    def setAttribute(self, class_: typing.Type, object: typing.Any, string: str, object2: typing.Any, boolean: bool, boolean2: bool) -> None: ...
    def setProperties(self, object: typing.Any, map: typing.Union[java.util.Map, typing.Mapping]) -> None: ...
    @typing.overload
    def setProperty(self, object: typing.Any, string: str, object2: typing.Any) -> None: ...
    @typing.overload
    def setProperty(self, class_: typing.Type, object: typing.Any, string: str, object2: typing.Any, boolean: bool, boolean2: bool) -> None: ...

class ClosureMetaMethod(groovy.lang.MetaMethod, groovy.lang.ClosureInvokingMethod):
    @typing.overload
    def __init__(self, string: str, closure: groovy.lang.Closure, cachedMethod: org.codehaus.groovy.reflection.CachedMethod): ...
    @typing.overload
    def __init__(self, string: str, class_: typing.Type, closure: groovy.lang.Closure, cachedMethod: org.codehaus.groovy.reflection.CachedMethod): ...
    @staticmethod
    def copy(closureMetaMethod: 'ClosureMetaMethod') -> 'ClosureMetaMethod': ...
    @staticmethod
    def createMethodList(string: str, class_: typing.Type, closure: groovy.lang.Closure) -> java.util.List[groovy.lang.MetaMethod]: ...
    def getClosure(self) -> groovy.lang.Closure: ...
    def getDeclaringClass(self) -> org.codehaus.groovy.reflection.CachedClass: ...
    def getDoCall(self) -> org.codehaus.groovy.reflection.CachedMethod: ...
    def getModifiers(self) -> int: ...
    def getName(self) -> str: ...
    def getReturnType(self) -> typing.Type: ...
    def invoke(self, object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> typing.Any: ...

class ClosureStaticMetaMethod(groovy.lang.MetaMethod, groovy.lang.ClosureInvokingMethod):
    @typing.overload
    def __init__(self, string: str, class_: typing.Type, closure: groovy.lang.Closure): ...
    @typing.overload
    def __init__(self, string: str, class_: typing.Type, closure: groovy.lang.Closure, classArray: typing.Union[typing.List[typing.Type], jpype.JArray]): ...
    def getClosure(self) -> groovy.lang.Closure: ...
    def getDeclaringClass(self) -> org.codehaus.groovy.reflection.CachedClass: ...
    def getModifiers(self) -> int: ...
    def getName(self) -> str: ...
    def getReturnType(self) -> typing.Type: ...
    def invoke(self, object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> typing.Any: ...

class ConcurrentReaderHashMap(java.util.AbstractMap, java.lang.Cloneable, java.io.Serializable):
    DEFAULT_INITIAL_CAPACITY: typing.ClassVar[int] = ...
    DEFAULT_LOAD_FACTOR: typing.ClassVar[float] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, float: float): ...
    @typing.overload
    def __init__(self, map: typing.Union[java.util.Map, typing.Mapping]): ...
    def capacity(self) -> int: ...
    def clear(self) -> None: ...
    def clone(self) -> typing.Any: ...
    def contains(self, object: typing.Any) -> bool: ...
    def containsKey(self, object: typing.Any) -> bool: ...
    def containsValue(self, object: typing.Any) -> bool: ...
    def elements(self) -> java.util.Enumeration: ...
    def entrySet(self) -> java.util.Set: ...
    def get(self, object: typing.Any) -> typing.Any: ...
    def isEmpty(self) -> bool: ...
    def keySet(self) -> java.util.Set: ...
    def keys(self) -> java.util.Enumeration: ...
    def loadFactor(self) -> float: ...
    def put(self, object: typing.Any, object2: typing.Any) -> typing.Any: ...
    def putAll(self, map: typing.Union[java.util.Map, typing.Mapping]) -> None: ...
    @typing.overload
    def remove(self, object: typing.Any, object2: typing.Any) -> bool: ...
    @typing.overload
    def remove(self, object: typing.Any) -> typing.Any: ...
    def size(self) -> int: ...
    def values(self) -> java.util.Collection: ...

class DefaultMetaClassInfo:
    def __init__(self): ...
    @staticmethod
    def disabledStandardMetaClass() -> bool: ...
    @staticmethod
    def getCurrentConstantMetaClassVersioning() -> 'DefaultMetaClassInfo.ConstantMetaClassVersioning': ...
    @staticmethod
    def getNewConstantMetaClassVersioning() -> 'DefaultMetaClassInfo.ConstantMetaClassVersioning': ...
    @staticmethod
    def isOrigBool() -> bool: ...
    @staticmethod
    def isOrigByte() -> bool: ...
    @staticmethod
    def isOrigChar() -> bool: ...
    @staticmethod
    def isOrigDouble() -> bool: ...
    @staticmethod
    def isOrigFloat() -> bool: ...
    @staticmethod
    def isOrigInt() -> bool: ...
    @staticmethod
    def isOrigIntArray() -> bool: ...
    @staticmethod
    def isOrigLong() -> bool: ...
    @staticmethod
    def isOrigShort() -> bool: ...
    @staticmethod
    def setCategoryUsed(boolean: bool) -> None: ...
    @staticmethod
    def setOrigBool(boolean: bool) -> None: ...
    @staticmethod
    def setOrigByte(boolean: bool) -> None: ...
    @staticmethod
    def setOrigChar(boolean: bool) -> None: ...
    @staticmethod
    def setOrigDouble(boolean: bool) -> None: ...
    @staticmethod
    def setOrigFloat(boolean: bool) -> None: ...
    @staticmethod
    def setOrigInt(boolean: bool) -> None: ...
    @staticmethod
    def setOrigIntArray(boolean: bool) -> None: ...
    @staticmethod
    def setOrigLong(boolean: bool) -> None: ...
    @staticmethod
    def setOrigShort(boolean: bool) -> None: ...
    @staticmethod
    def setPrimitiveMeta(class_: typing.Type, boolean: bool) -> None: ...
    @staticmethod
    def setWithoutCustomMetaclassCreationHandle(boolean: bool) -> None: ...
    class ConstantMetaClassVersioning:
        def __init__(self): ...
        def isValid(self) -> bool: ...

class MetaClassRegistryImpl(groovy.lang.MetaClassRegistry):
    MODULE_META_INF_FILE: typing.ClassVar[str] = ...
    LOAD_DEFAULT: typing.ClassVar[int] = ...
    DONT_LOAD_DEFAULT: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, boolean: bool): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, boolean: bool): ...
    def addMetaClassRegistryChangeEventListener(self, metaClassRegistryChangeEventListener: groovy.lang.MetaClassRegistryChangeEventListener) -> None: ...
    def addNonRemovableMetaClassRegistryChangeEventListener(self, metaClassRegistryChangeEventListener: groovy.lang.MetaClassRegistryChangeEventListener) -> None: ...
    @staticmethod
    def getInstance(int: int) -> groovy.lang.MetaClassRegistry: ...
    def getInstanceMethods(self) -> org.codehaus.groovy.util.FastArray: ...
    @typing.overload
    def getMetaClass(self, class_: typing.Type) -> groovy.lang.MetaClass: ...
    @typing.overload
    def getMetaClass(self, object: typing.Any) -> groovy.lang.MetaClass: ...
    def getMetaClassCreationHandler(self) -> groovy.lang.MetaClassRegistry.MetaClassCreationHandle: ...
    def getMetaClassRegistryChangeEventListeners(self) -> typing.MutableSequence[groovy.lang.MetaClassRegistryChangeEventListener]: ...
    def getModuleRegistry(self) -> org.codehaus.groovy.runtime.m12n.ExtensionModuleRegistry: ...
    def getStaticMethods(self) -> org.codehaus.groovy.util.FastArray: ...
    def iterator(self) -> java.util.Iterator: ...
    def registerExtensionModuleFromProperties(self, properties: java.util.Properties, classLoader: java.lang.ClassLoader, map: typing.Union[java.util.Map[org.codehaus.groovy.reflection.CachedClass, java.util.List[groovy.lang.MetaMethod]], typing.Mapping[org.codehaus.groovy.reflection.CachedClass, java.util.List[groovy.lang.MetaMethod]]]) -> None: ...
    def removeMetaClass(self, class_: typing.Type) -> None: ...
    def removeMetaClassRegistryChangeEventListener(self, metaClassRegistryChangeEventListener: groovy.lang.MetaClassRegistryChangeEventListener) -> None: ...
    @typing.overload
    def setMetaClass(self, class_: typing.Type, metaClass: groovy.lang.MetaClass) -> None: ...
    @typing.overload
    def setMetaClass(self, object: typing.Any, metaClass: groovy.lang.MetaClass) -> None: ...
    def setMetaClassCreationHandle(self, metaClassCreationHandle: groovy.lang.MetaClassRegistry.MetaClassCreationHandle) -> None: ...
    def useAccessible(self) -> bool: ...

class MetaMethodIndex:
    methodHeaders: org.codehaus.groovy.util.SingleKeyHashMap = ...
    def __init__(self, cachedClass: org.codehaus.groovy.reflection.CachedClass): ...
    def addMethodToList(self, object: typing.Any, metaMethod: groovy.lang.MetaMethod) -> typing.Any: ...
    def clear(self) -> None: ...
    @typing.overload
    def clearCaches(self) -> None: ...
    @typing.overload
    def clearCaches(self, string: str) -> None: ...
    @typing.overload
    def copy(self, class_: typing.Type, header: 'MetaMethodIndex.Header') -> None: ...
    @typing.overload
    def copy(self, header: 'MetaMethodIndex.Header', header2: 'MetaMethodIndex.Header') -> None: ...
    def copyAllMethodsToSuper(self, header: 'MetaMethodIndex.Header', header2: 'MetaMethodIndex.Header') -> None: ...
    def copyMethodsToSuper(self) -> None: ...
    @typing.overload
    def copyNonPrivateMethods(self, class_: typing.Type, class2: typing.Type) -> None: ...
    @typing.overload
    def copyNonPrivateMethods(self, header: 'MetaMethodIndex.Header', header2: 'MetaMethodIndex.Header') -> None: ...
    def copyNonPrivateMethodsDown(self, class_: typing.Type, class2: typing.Type) -> None: ...
    def copyNonPrivateMethodsFromSuper(self, header: 'MetaMethodIndex.Header') -> None: ...
    def copyNonPrivateNonNewMetaMethods(self, header: 'MetaMethodIndex.Header', header2: 'MetaMethodIndex.Header') -> None: ...
    def getEntrySetIterator(self) -> 'MetaMethodIndex.EntryIterator': ...
    def getHeader(self, class_: typing.Type) -> 'MetaMethodIndex.Header': ...
    def getMethods(self, class_: typing.Type, string: str) -> 'MetaMethodIndex.Entry': ...
    def getOrPutMethods(self, string: str, header: 'MetaMethodIndex.Header') -> 'MetaMethodIndex.Entry': ...
    def getTable(self) -> typing.MutableSequence['MetaMethodIndex.Entry']: ...
    @staticmethod
    def hash(int: int) -> int: ...
    def init(self, int: int) -> None: ...
    def isEmpty(self) -> bool: ...
    def resize(self, int: int) -> None: ...
    def size(self) -> int: ...
    class CacheEntry:
        params: typing.MutableSequence[typing.Type] = ...
        method: groovy.lang.MetaMethod = ...
        def __init__(self, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], metaMethod: groovy.lang.MetaMethod): ...
    class Entry:
        hash: int = ...
        nextHashEntry: 'MetaMethodIndex.Entry' = ...
        nextClassEntry: 'MetaMethodIndex.Entry' = ...
        name: str = ...
        cls: typing.Type = ...
        methods: typing.Any = ...
        methodsForSuper: typing.Any = ...
        staticMethods: typing.Any = ...
        cachedMethod: 'MetaMethodIndex.CacheEntry' = ...
        cachedMethodForSuper: 'MetaMethodIndex.CacheEntry' = ...
        cachedStaticMethod: 'MetaMethodIndex.CacheEntry' = ...
        def __init__(self): ...
        def toString(self) -> str: ...
    class EntryIterator:
        def hasNext(self) -> bool: ...
        def next(self) -> 'MetaMethodIndex.Entry': ...
    class Header:
        head: 'MetaMethodIndex.Entry' = ...
        clsHashCode31: int = ...
        subclass: typing.Type = ...
        @typing.overload
        def __init__(self, class_: typing.Type): ...
        @typing.overload
        def __init__(self, class_: typing.Type, class2: typing.Type): ...

class MethodHelper:
    def __init__(self): ...
    @staticmethod
    def isPublic(method: java.lang.reflect.Method) -> bool: ...
    @staticmethod
    def isStatic(method: java.lang.reflect.Method) -> bool: ...

class MethodSelectionException(groovy.lang.GroovyRuntimeException):
    def __init__(self, string: str, fastArray: org.codehaus.groovy.util.FastArray, classArray: typing.Union[typing.List[typing.Type], jpype.JArray]): ...
    def getMessage(self) -> str: ...

class MissingMethodExceptionNoStack(groovy.lang.MissingMethodException):
    @typing.overload
    def __init__(self, string: str, class_: typing.Type, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]): ...
    @typing.overload
    def __init__(self, string: str, class_: typing.Type, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray], boolean: bool): ...
    def fillInStackTrace(self) -> java.lang.Throwable: ...

class MissingPropertyExceptionNoStack(groovy.lang.MissingPropertyException):
    def __init__(self, string: str, class_: typing.Type): ...
    def fillInStackTrace(self) -> java.lang.Throwable: ...

class MixinInstanceMetaMethod(groovy.lang.MetaMethod):
    def __init__(self, metaMethod: groovy.lang.MetaMethod, mixinInMetaClass: org.codehaus.groovy.reflection.MixinInMetaClass): ...
    def getDeclaringClass(self) -> org.codehaus.groovy.reflection.CachedClass: ...
    def getModifiers(self) -> int: ...
    def getName(self) -> str: ...
    def getReturnType(self) -> typing.Type: ...
    def invoke(self, object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> typing.Any: ...

class MixinInstanceMetaProperty(groovy.lang.MetaBeanProperty):
    def __init__(self, metaProperty: groovy.lang.MetaProperty, mixinInMetaClass: org.codehaus.groovy.reflection.MixinInMetaClass): ...

class MultipleSetterProperty(groovy.lang.MetaProperty):
    def __init__(self, string: str): ...
    def createStaticVersion(self) -> groovy.lang.MetaProperty: ...
    def getField(self) -> org.codehaus.groovy.reflection.CachedField: ...
    def getGetter(self) -> groovy.lang.MetaMethod: ...
    def getProperty(self, object: typing.Any) -> typing.Any: ...
    def setField(self, cachedField: org.codehaus.groovy.reflection.CachedField) -> None: ...
    def setGetter(self, metaMethod: groovy.lang.MetaMethod) -> None: ...
    def setProperty(self, object: typing.Any, object2: typing.Any) -> None: ...

class OwnedMetaClass(groovy.lang.DelegatingMetaClass):
    def __init__(self, metaClass: groovy.lang.MetaClass): ...
    def equals(self, object: typing.Any) -> bool: ...
    @typing.overload
    def getAttribute(self, class_: typing.Type, object: typing.Any, string: str, boolean: bool) -> typing.Any: ...
    @typing.overload
    def getAttribute(self, object: typing.Any, string: str) -> typing.Any: ...
    def getClassNode(self) -> org.codehaus.groovy.ast.ClassNode: ...
    @typing.overload
    def getMetaMethod(self, string: str, classArray: typing.Union[typing.List[typing.Type], jpype.JArray]) -> groovy.lang.MetaMethod: ...
    @typing.overload
    def getMetaMethod(self, string: str, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> groovy.lang.MetaMethod: ...
    def getMetaMethods(self) -> java.util.List[groovy.lang.MetaMethod]: ...
    def getMetaProperty(self, string: str) -> groovy.lang.MetaProperty: ...
    def getMethods(self) -> java.util.List[groovy.lang.MetaMethod]: ...
    def getProperties(self) -> java.util.List[groovy.lang.MetaProperty]: ...
    @typing.overload
    def getProperty(self, string: str) -> typing.Any: ...
    @typing.overload
    def getProperty(self, class_: typing.Type, object: typing.Any, string: str, boolean: bool, boolean2: bool) -> typing.Any: ...
    @typing.overload
    def getProperty(self, object: typing.Any, string: str) -> typing.Any: ...
    @typing.overload
    def getStaticMetaMethod(self, string: str, classArray: typing.Union[typing.List[typing.Type], jpype.JArray]) -> groovy.lang.MetaMethod: ...
    @typing.overload
    def getStaticMetaMethod(self, string: str, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> groovy.lang.MetaMethod: ...
    def getTheClass(self) -> typing.Type: ...
    def hasProperty(self, object: typing.Any, string: str) -> groovy.lang.MetaProperty: ...
    def hashCode(self) -> int: ...
    def invokeConstructor(self, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> typing.Any: ...
    @typing.overload
    def invokeMethod(self, string: str, object: typing.Any) -> typing.Any: ...
    @typing.overload
    def invokeMethod(self, class_: typing.Type, object: typing.Any, string: str, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray], boolean: bool, boolean2: bool) -> typing.Any: ...
    @typing.overload
    def invokeMethod(self, object: typing.Any, string: str, object2: typing.Any) -> typing.Any: ...
    @typing.overload
    def invokeMethod(self, object: typing.Any, string: str, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> typing.Any: ...
    def invokeMissingMethod(self, object: typing.Any, string: str, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> typing.Any: ...
    def invokeMissingProperty(self, object: typing.Any, string: str, object2: typing.Any, boolean: bool) -> typing.Any: ...
    def invokeStaticMethod(self, object: typing.Any, string: str, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> typing.Any: ...
    def isGroovyObject(self) -> bool: ...
    @typing.overload
    def respondsTo(self, object: typing.Any, string: str) -> java.util.List[groovy.lang.MetaMethod]: ...
    @typing.overload
    def respondsTo(self, object: typing.Any, string: str, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> java.util.List[groovy.lang.MetaMethod]: ...
    def selectConstructorAndTransformArguments(self, int: int, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> int: ...
    @typing.overload
    def setAttribute(self, class_: typing.Type, object: typing.Any, string: str, object2: typing.Any, boolean: bool, boolean2: bool) -> None: ...
    @typing.overload
    def setAttribute(self, object: typing.Any, string: str, object2: typing.Any) -> None: ...
    @typing.overload
    def setProperty(self, string: str, object: typing.Any) -> None: ...
    @typing.overload
    def setProperty(self, class_: typing.Type, object: typing.Any, string: str, object2: typing.Any, boolean: bool, boolean2: bool) -> None: ...
    @typing.overload
    def setProperty(self, object: typing.Any, string: str, object2: typing.Any) -> None: ...
    def toString(self) -> str: ...

class ReflectionMetaMethod(groovy.lang.MetaMethod):
    def __init__(self, cachedMethod: org.codehaus.groovy.reflection.CachedMethod): ...
    def getCachedMethod(self) -> groovy.lang.MetaMethod: ...
    def getDeclaringClass(self) -> org.codehaus.groovy.reflection.CachedClass: ...
    def getModifiers(self) -> int: ...
    def getName(self) -> str: ...
    def getReturnType(self) -> typing.Type: ...
    def invoke(self, object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> typing.Any: ...
    def toString(self) -> str: ...

class ReflectorLoader(java.lang.ClassLoader):
    def __init__(self, classLoader: java.lang.ClassLoader): ...
    def defineClass(self, string: str, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes], protectionDomain: java.security.ProtectionDomain) -> typing.Type: ...
    def getLoadedClass(self, string: str) -> typing.Type: ...

class TemporaryMethodKey(org.codehaus.groovy.runtime.MethodKey):
    def __init__(self, class_: typing.Type, string: str, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray], boolean: bool): ...
    def getParameterCount(self) -> int: ...
    def getParameterType(self, int: int) -> typing.Type: ...

class ThreadManagedMetaBeanProperty(groovy.lang.MetaBeanProperty):
    @typing.overload
    def __init__(self, class_: typing.Type, string: str, class2: typing.Type, closure: groovy.lang.Closure): ...
    @typing.overload
    def __init__(self, class_: typing.Type, string: str, class2: typing.Type, object: typing.Any): ...
    def getGetter(self) -> groovy.lang.MetaMethod: ...
    @typing.overload
    def getInitialValue(self) -> typing.Any: ...
    @typing.overload
    def getInitialValue(self, object: typing.Any) -> typing.Any: ...
    def getSetter(self) -> groovy.lang.MetaMethod: ...
    def setInitialValueCreator(self, closure: groovy.lang.Closure) -> None: ...

class TransformMetaMethod(groovy.lang.MetaMethod):
    def __init__(self, metaMethod: groovy.lang.MetaMethod): ...
    def getDeclaringClass(self) -> org.codehaus.groovy.reflection.CachedClass: ...
    def getModifiers(self) -> int: ...
    def getName(self) -> str: ...
    def getReturnType(self) -> typing.Type: ...
    def invoke(self, object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> typing.Any: ...

class MissingMethodExecutionFailed(MissingMethodExceptionNoStack):
    def __init__(self, string: str, class_: typing.Type, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray], boolean: bool, throwable: java.lang.Throwable): ...
    def getCause(self) -> java.lang.Throwable: ...

class MixedInMetaClass(OwnedMetaClass):
    def __init__(self, object: typing.Any, object2: typing.Any): ...
    @typing.overload
    def invokeMethod(self, string: str, object: typing.Any) -> typing.Any: ...
    @typing.overload
    def invokeMethod(self, class_: typing.Type, object: typing.Any, string: str, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray], boolean: bool, boolean2: bool) -> typing.Any: ...
    @typing.overload
    def invokeMethod(self, object: typing.Any, string: str, object2: typing.Any) -> typing.Any: ...
    @typing.overload
    def invokeMethod(self, object: typing.Any, string: str, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> typing.Any: ...

class NewMetaMethod(ReflectionMetaMethod):
    def __init__(self, cachedMethod: org.codehaus.groovy.reflection.CachedMethod): ...
    def getBytecodeParameterTypes(self) -> typing.MutableSequence[org.codehaus.groovy.reflection.CachedClass]: ...
    def getDeclaringClass(self) -> org.codehaus.groovy.reflection.CachedClass: ...
    def getOwnerClass(self) -> org.codehaus.groovy.reflection.CachedClass: ...

class NewInstanceMetaMethod(NewMetaMethod):
    def __init__(self, cachedMethod: org.codehaus.groovy.reflection.CachedMethod): ...
    def getModifiers(self) -> int: ...
    def invoke(self, object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> typing.Any: ...
    def isStatic(self) -> bool: ...

class NewStaticMetaMethod(NewMetaMethod):
    def __init__(self, cachedMethod: org.codehaus.groovy.reflection.CachedMethod): ...
    def getModifiers(self) -> int: ...
    def invoke(self, object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> typing.Any: ...
    def isStatic(self) -> bool: ...

class MethodMetaProperty(groovy.lang.MetaProperty):
    def __init__(self, string: str, metaMethod: groovy.lang.MetaMethod): ...
    def getMetaMethod(self) -> groovy.lang.MetaMethod: ...
    def getProperty(self, object: typing.Any) -> typing.Any: ...
    def setProperty(self, object: typing.Any, object2: typing.Any) -> None: ...
    class GetBeanMethodMetaProperty(org.codehaus.groovy.runtime.metaclass.MethodMetaProperty):
        def __init__(self, string: str, metaMethod: groovy.lang.MetaMethod): ...
        def getProperty(self, object: typing.Any) -> typing.Any: ...
    class GetMethodMetaProperty(org.codehaus.groovy.runtime.metaclass.MethodMetaProperty):
        def __init__(self, string: str, metaMethod: groovy.lang.MetaMethod): ...
        def getProperty(self, object: typing.Any) -> typing.Any: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.runtime.metaclass")``.

    ClosureMetaClass: typing.Type[ClosureMetaClass]
    ClosureMetaMethod: typing.Type[ClosureMetaMethod]
    ClosureStaticMetaMethod: typing.Type[ClosureStaticMetaMethod]
    ConcurrentReaderHashMap: typing.Type[ConcurrentReaderHashMap]
    DefaultMetaClassInfo: typing.Type[DefaultMetaClassInfo]
    MetaClassRegistryImpl: typing.Type[MetaClassRegistryImpl]
    MetaMethodIndex: typing.Type[MetaMethodIndex]
    MethodHelper: typing.Type[MethodHelper]
    MethodMetaProperty: typing.Type[MethodMetaProperty]
    MethodSelectionException: typing.Type[MethodSelectionException]
    MissingMethodExceptionNoStack: typing.Type[MissingMethodExceptionNoStack]
    MissingMethodExecutionFailed: typing.Type[MissingMethodExecutionFailed]
    MissingPropertyExceptionNoStack: typing.Type[MissingPropertyExceptionNoStack]
    MixedInMetaClass: typing.Type[MixedInMetaClass]
    MixinInstanceMetaMethod: typing.Type[MixinInstanceMetaMethod]
    MixinInstanceMetaProperty: typing.Type[MixinInstanceMetaProperty]
    MultipleSetterProperty: typing.Type[MultipleSetterProperty]
    NewInstanceMetaMethod: typing.Type[NewInstanceMetaMethod]
    NewMetaMethod: typing.Type[NewMetaMethod]
    NewStaticMetaMethod: typing.Type[NewStaticMetaMethod]
    OwnedMetaClass: typing.Type[OwnedMetaClass]
    ReflectionMetaMethod: typing.Type[ReflectionMetaMethod]
    ReflectorLoader: typing.Type[ReflectorLoader]
    TemporaryMethodKey: typing.Type[TemporaryMethodKey]
    ThreadManagedMetaBeanProperty: typing.Type[ThreadManagedMetaBeanProperty]
    TransformMetaMethod: typing.Type[TransformMetaMethod]