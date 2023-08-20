
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.applet
import java.awt
import java.beans.beancontext
import java.io
import java.lang
import java.lang.annotation
import java.lang.reflect
import java.util
import jpype
import org.xml.sax
import org.xml.sax.helpers
import typing



class AppletInitializer:
    def activate(self, applet: java.applet.Applet) -> None: ...
    def initialize(self, applet: java.applet.Applet, beanContext: java.beans.beancontext.BeanContext) -> None: ...

class BeanInfo:
    ICON_COLOR_16x16: typing.ClassVar[int] = ...
    ICON_COLOR_32x32: typing.ClassVar[int] = ...
    ICON_MONO_16x16: typing.ClassVar[int] = ...
    ICON_MONO_32x32: typing.ClassVar[int] = ...
    def getAdditionalBeanInfo(self) -> typing.MutableSequence['BeanInfo']: ...
    def getBeanDescriptor(self) -> 'BeanDescriptor': ...
    def getDefaultEventIndex(self) -> int: ...
    def getDefaultPropertyIndex(self) -> int: ...
    def getEventSetDescriptors(self) -> typing.MutableSequence['EventSetDescriptor']: ...
    def getIcon(self, int: int) -> java.awt.Image: ...
    def getMethodDescriptors(self) -> typing.MutableSequence['MethodDescriptor']: ...
    def getPropertyDescriptors(self) -> typing.MutableSequence['PropertyDescriptor']: ...

class BeanProperty(java.lang.annotation.Annotation):
    def bound(self) -> bool: ...
    def description(self) -> str: ...
    def enumerationValues(self) -> typing.MutableSequence[str]: ...
    def equals(self, object: typing.Any) -> bool: ...
    def expert(self) -> bool: ...
    def hashCode(self) -> int: ...
    def hidden(self) -> bool: ...
    def preferred(self) -> bool: ...
    def required(self) -> bool: ...
    def toString(self) -> str: ...
    def visualUpdate(self) -> bool: ...

class Beans:
    def __init__(self): ...
    @staticmethod
    def getInstanceOf(object: typing.Any, class_: typing.Type[typing.Any]) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def instantiate(classLoader: java.lang.ClassLoader, string: str) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def instantiate(classLoader: java.lang.ClassLoader, string: str, beanContext: java.beans.beancontext.BeanContext) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def instantiate(classLoader: java.lang.ClassLoader, string: str, beanContext: java.beans.beancontext.BeanContext, appletInitializer: AppletInitializer) -> typing.Any: ...
    @staticmethod
    def isDesignTime() -> bool: ...
    @staticmethod
    def isGuiAvailable() -> bool: ...
    @staticmethod
    def isInstanceOf(object: typing.Any, class_: typing.Type[typing.Any]) -> bool: ...
    @staticmethod
    def setDesignTime(boolean: bool) -> None: ...
    @staticmethod
    def setGuiAvailable(boolean: bool) -> None: ...

class ConstructorProperties(java.lang.annotation.Annotation):
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    def value(self) -> typing.MutableSequence[str]: ...

class Customizer:
    def addPropertyChangeListener(self, propertyChangeListener: 'PropertyChangeListener') -> None: ...
    def removePropertyChangeListener(self, propertyChangeListener: 'PropertyChangeListener') -> None: ...
    def setObject(self, object: typing.Any) -> None: ...

class DesignMode:
    PROPERTYNAME: typing.ClassVar[str] = ...
    def isDesignTime(self) -> bool: ...
    def setDesignTime(self, boolean: bool) -> None: ...

class Encoder:
    def __init__(self): ...
    def get(self, object: typing.Any) -> typing.Any: ...
    def getExceptionListener(self) -> 'ExceptionListener': ...
    def getPersistenceDelegate(self, class_: typing.Type[typing.Any]) -> 'PersistenceDelegate': ...
    def remove(self, object: typing.Any) -> typing.Any: ...
    def setExceptionListener(self, exceptionListener: 'ExceptionListener') -> None: ...
    def setPersistenceDelegate(self, class_: typing.Type[typing.Any], persistenceDelegate: 'PersistenceDelegate') -> None: ...
    def writeExpression(self, expression: 'Expression') -> None: ...
    def writeStatement(self, statement: 'Statement') -> None: ...

class EventHandler(java.lang.reflect.InvocationHandler):
    def __init__(self, object: typing.Any, string: str, string2: str, string3: str): ...
    _create_0__T = typing.TypeVar('_create_0__T')  # <T>
    _create_1__T = typing.TypeVar('_create_1__T')  # <T>
    _create_2__T = typing.TypeVar('_create_2__T')  # <T>
    @typing.overload
    @staticmethod
    def create(class_: typing.Type[_create_0__T], object: typing.Any, string: str) -> _create_0__T: ...
    @typing.overload
    @staticmethod
    def create(class_: typing.Type[_create_1__T], object: typing.Any, string: str, string2: str) -> _create_1__T: ...
    @typing.overload
    @staticmethod
    def create(class_: typing.Type[_create_2__T], object: typing.Any, string: str, string2: str, string3: str) -> _create_2__T: ...
    def getAction(self) -> str: ...
    def getEventPropertyName(self) -> str: ...
    def getListenerMethodName(self) -> str: ...
    def getTarget(self) -> typing.Any: ...
    def invoke(self, object: typing.Any, method: java.lang.reflect.Method, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> typing.Any: ...

class ExceptionListener:
    def exceptionThrown(self, exception: java.lang.Exception) -> None: ...

class FeatureDescriptor:
    def __init__(self): ...
    def attributeNames(self) -> java.util.Enumeration[str]: ...
    def getDisplayName(self) -> str: ...
    def getName(self) -> str: ...
    def getShortDescription(self) -> str: ...
    def getValue(self, string: str) -> typing.Any: ...
    def isExpert(self) -> bool: ...
    def isHidden(self) -> bool: ...
    def isPreferred(self) -> bool: ...
    def setDisplayName(self, string: str) -> None: ...
    def setExpert(self, boolean: bool) -> None: ...
    def setHidden(self, boolean: bool) -> None: ...
    def setName(self, string: str) -> None: ...
    def setPreferred(self, boolean: bool) -> None: ...
    def setShortDescription(self, string: str) -> None: ...
    def setValue(self, string: str, object: typing.Any) -> None: ...
    def toString(self) -> str: ...

class IntrospectionException(java.lang.Exception):
    def __init__(self, string: str): ...

class Introspector:
    USE_ALL_BEANINFO: typing.ClassVar[int] = ...
    IGNORE_IMMEDIATE_BEANINFO: typing.ClassVar[int] = ...
    IGNORE_ALL_BEANINFO: typing.ClassVar[int] = ...
    @staticmethod
    def decapitalize(string: str) -> str: ...
    @staticmethod
    def flushCaches() -> None: ...
    @staticmethod
    def flushFromCaches(class_: typing.Type[typing.Any]) -> None: ...
    @typing.overload
    @staticmethod
    def getBeanInfo(class_: typing.Type[typing.Any]) -> BeanInfo: ...
    @typing.overload
    @staticmethod
    def getBeanInfo(class_: typing.Type[typing.Any], int: int) -> BeanInfo: ...
    @typing.overload
    @staticmethod
    def getBeanInfo(class_: typing.Type[typing.Any], class2: typing.Type[typing.Any]) -> BeanInfo: ...
    @typing.overload
    @staticmethod
    def getBeanInfo(class_: typing.Type[typing.Any], class2: typing.Type[typing.Any], int: int) -> BeanInfo: ...
    @staticmethod
    def getBeanInfoSearchPath() -> typing.MutableSequence[str]: ...
    @staticmethod
    def setBeanInfoSearchPath(stringArray: typing.Union[typing.List[str], jpype.JArray]) -> None: ...

class JavaBean(java.lang.annotation.Annotation):
    def defaultEventSet(self) -> str: ...
    def defaultProperty(self) -> str: ...
    def description(self) -> str: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class PersistenceDelegate:
    def __init__(self): ...
    def writeObject(self, object: typing.Any, encoder: Encoder) -> None: ...

class PropertyChangeEvent(java.util.EventObject):
    def __init__(self, object: typing.Any, string: str, object2: typing.Any, object3: typing.Any): ...
    def getNewValue(self) -> typing.Any: ...
    def getOldValue(self) -> typing.Any: ...
    def getPropagationId(self) -> typing.Any: ...
    def getPropertyName(self) -> str: ...
    def setPropagationId(self, object: typing.Any) -> None: ...
    def toString(self) -> str: ...

class PropertyChangeListener(java.util.EventListener):
    def propertyChange(self, propertyChangeEvent: PropertyChangeEvent) -> None: ...

class PropertyChangeSupport(java.io.Serializable):
    def __init__(self, object: typing.Any): ...
    @typing.overload
    def addPropertyChangeListener(self, propertyChangeListener: PropertyChangeListener) -> None: ...
    @typing.overload
    def addPropertyChangeListener(self, string: str, propertyChangeListener: PropertyChangeListener) -> None: ...
    @typing.overload
    def fireIndexedPropertyChange(self, string: str, int: int, boolean: bool, boolean2: bool) -> None: ...
    @typing.overload
    def fireIndexedPropertyChange(self, string: str, int: int, int2: int, int3: int) -> None: ...
    @typing.overload
    def fireIndexedPropertyChange(self, string: str, int: int, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    def firePropertyChange(self, propertyChangeEvent: PropertyChangeEvent) -> None: ...
    @typing.overload
    def firePropertyChange(self, string: str, boolean: bool, boolean2: bool) -> None: ...
    @typing.overload
    def firePropertyChange(self, string: str, int: int, int2: int) -> None: ...
    @typing.overload
    def firePropertyChange(self, string: str, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    def getPropertyChangeListeners(self) -> typing.MutableSequence[PropertyChangeListener]: ...
    @typing.overload
    def getPropertyChangeListeners(self, string: str) -> typing.MutableSequence[PropertyChangeListener]: ...
    def hasListeners(self, string: str) -> bool: ...
    @typing.overload
    def removePropertyChangeListener(self, propertyChangeListener: PropertyChangeListener) -> None: ...
    @typing.overload
    def removePropertyChangeListener(self, string: str, propertyChangeListener: PropertyChangeListener) -> None: ...

class PropertyEditor:
    def addPropertyChangeListener(self, propertyChangeListener: PropertyChangeListener) -> None: ...
    def getAsText(self) -> str: ...
    def getCustomEditor(self) -> java.awt.Component: ...
    def getJavaInitializationString(self) -> str: ...
    def getTags(self) -> typing.MutableSequence[str]: ...
    def getValue(self) -> typing.Any: ...
    def isPaintable(self) -> bool: ...
    def paintValue(self, graphics: java.awt.Graphics, rectangle: java.awt.Rectangle) -> None: ...
    def removePropertyChangeListener(self, propertyChangeListener: PropertyChangeListener) -> None: ...
    def setAsText(self, string: str) -> None: ...
    def setValue(self, object: typing.Any) -> None: ...
    def supportsCustomEditor(self) -> bool: ...

class PropertyEditorManager:
    def __init__(self): ...
    @staticmethod
    def findEditor(class_: typing.Type[typing.Any]) -> PropertyEditor: ...
    @staticmethod
    def getEditorSearchPath() -> typing.MutableSequence[str]: ...
    @staticmethod
    def registerEditor(class_: typing.Type[typing.Any], class2: typing.Type[typing.Any]) -> None: ...
    @staticmethod
    def setEditorSearchPath(stringArray: typing.Union[typing.List[str], jpype.JArray]) -> None: ...

class PropertyVetoException(java.lang.Exception):
    def __init__(self, string: str, propertyChangeEvent: PropertyChangeEvent): ...
    def getPropertyChangeEvent(self) -> PropertyChangeEvent: ...

class Statement:
    def __init__(self, object: typing.Any, string: str, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]): ...
    def execute(self) -> None: ...
    def getArguments(self) -> typing.MutableSequence[typing.Any]: ...
    def getMethodName(self) -> str: ...
    def getTarget(self) -> typing.Any: ...
    def toString(self) -> str: ...

class Transient(java.lang.annotation.Annotation):
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    def value(self) -> bool: ...

class VetoableChangeListener(java.util.EventListener):
    def vetoableChange(self, propertyChangeEvent: PropertyChangeEvent) -> None: ...

class VetoableChangeSupport(java.io.Serializable):
    def __init__(self, object: typing.Any): ...
    @typing.overload
    def addVetoableChangeListener(self, vetoableChangeListener: VetoableChangeListener) -> None: ...
    @typing.overload
    def addVetoableChangeListener(self, string: str, vetoableChangeListener: VetoableChangeListener) -> None: ...
    @typing.overload
    def fireVetoableChange(self, propertyChangeEvent: PropertyChangeEvent) -> None: ...
    @typing.overload
    def fireVetoableChange(self, string: str, boolean: bool, boolean2: bool) -> None: ...
    @typing.overload
    def fireVetoableChange(self, string: str, int: int, int2: int) -> None: ...
    @typing.overload
    def fireVetoableChange(self, string: str, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    def getVetoableChangeListeners(self) -> typing.MutableSequence[VetoableChangeListener]: ...
    @typing.overload
    def getVetoableChangeListeners(self, string: str) -> typing.MutableSequence[VetoableChangeListener]: ...
    def hasListeners(self, string: str) -> bool: ...
    @typing.overload
    def removeVetoableChangeListener(self, vetoableChangeListener: VetoableChangeListener) -> None: ...
    @typing.overload
    def removeVetoableChangeListener(self, string: str, vetoableChangeListener: VetoableChangeListener) -> None: ...

class Visibility:
    def avoidingGui(self) -> bool: ...
    def dontUseGui(self) -> None: ...
    def needsGui(self) -> bool: ...
    def okToUseGui(self) -> None: ...

class XMLDecoder(java.lang.AutoCloseable):
    @typing.overload
    def __init__(self, inputStream: java.io.InputStream): ...
    @typing.overload
    def __init__(self, inputStream: java.io.InputStream, object: typing.Any): ...
    @typing.overload
    def __init__(self, inputStream: java.io.InputStream, object: typing.Any, exceptionListener: ExceptionListener): ...
    @typing.overload
    def __init__(self, inputStream: java.io.InputStream, object: typing.Any, exceptionListener: ExceptionListener, classLoader: java.lang.ClassLoader): ...
    @typing.overload
    def __init__(self, inputSource: org.xml.sax.InputSource): ...
    def close(self) -> None: ...
    @staticmethod
    def createHandler(object: typing.Any, exceptionListener: ExceptionListener, classLoader: java.lang.ClassLoader) -> org.xml.sax.helpers.DefaultHandler: ...
    def getExceptionListener(self) -> ExceptionListener: ...
    def getOwner(self) -> typing.Any: ...
    def readObject(self) -> typing.Any: ...
    def setExceptionListener(self, exceptionListener: ExceptionListener) -> None: ...
    def setOwner(self, object: typing.Any) -> None: ...

class BeanDescriptor(FeatureDescriptor):
    @typing.overload
    def __init__(self, class_: typing.Type[typing.Any]): ...
    @typing.overload
    def __init__(self, class_: typing.Type[typing.Any], class2: typing.Type[typing.Any]): ...
    def getBeanClass(self) -> typing.Type[typing.Any]: ...
    def getCustomizerClass(self) -> typing.Type[typing.Any]: ...

class DefaultPersistenceDelegate(PersistenceDelegate):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, stringArray: typing.Union[typing.List[str], jpype.JArray]): ...

class EventSetDescriptor(FeatureDescriptor):
    @typing.overload
    def __init__(self, class_: typing.Type[typing.Any], string: str, class2: typing.Type[typing.Any], string2: str): ...
    @typing.overload
    def __init__(self, class_: typing.Type[typing.Any], string: str, class2: typing.Type[typing.Any], stringArray: typing.Union[typing.List[str], jpype.JArray], string3: str, string4: str): ...
    @typing.overload
    def __init__(self, class_: typing.Type[typing.Any], string: str, class2: typing.Type[typing.Any], stringArray: typing.Union[typing.List[str], jpype.JArray], string3: str, string4: str, string5: str): ...
    @typing.overload
    def __init__(self, string: str, class_: typing.Type[typing.Any], methodDescriptorArray: typing.Union[typing.List['MethodDescriptor'], jpype.JArray], method2: java.lang.reflect.Method, method3: java.lang.reflect.Method): ...
    @typing.overload
    def __init__(self, string: str, class_: typing.Type[typing.Any], methodArray: typing.Union[typing.List[java.lang.reflect.Method], jpype.JArray], method2: java.lang.reflect.Method, method3: java.lang.reflect.Method): ...
    @typing.overload
    def __init__(self, string: str, class_: typing.Type[typing.Any], methodArray: typing.Union[typing.List[java.lang.reflect.Method], jpype.JArray], method2: java.lang.reflect.Method, method3: java.lang.reflect.Method, method4: java.lang.reflect.Method): ...
    def getAddListenerMethod(self) -> java.lang.reflect.Method: ...
    def getGetListenerMethod(self) -> java.lang.reflect.Method: ...
    def getListenerMethodDescriptors(self) -> typing.MutableSequence['MethodDescriptor']: ...
    def getListenerMethods(self) -> typing.MutableSequence[java.lang.reflect.Method]: ...
    def getListenerType(self) -> typing.Type[typing.Any]: ...
    def getRemoveListenerMethod(self) -> java.lang.reflect.Method: ...
    def isInDefaultEventSet(self) -> bool: ...
    def isUnicast(self) -> bool: ...
    def setInDefaultEventSet(self, boolean: bool) -> None: ...
    def setUnicast(self, boolean: bool) -> None: ...

class Expression(Statement):
    @typing.overload
    def __init__(self, object: typing.Any, object2: typing.Any, string: str, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]): ...
    @typing.overload
    def __init__(self, object: typing.Any, string: str, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]): ...
    def execute(self) -> None: ...
    def getValue(self) -> typing.Any: ...
    def setValue(self, object: typing.Any) -> None: ...
    def toString(self) -> str: ...

class IndexedPropertyChangeEvent(PropertyChangeEvent):
    def __init__(self, object: typing.Any, string: str, object2: typing.Any, object3: typing.Any, int: int): ...
    def getIndex(self) -> int: ...

class MethodDescriptor(FeatureDescriptor):
    @typing.overload
    def __init__(self, method: java.lang.reflect.Method): ...
    @typing.overload
    def __init__(self, method: java.lang.reflect.Method, parameterDescriptorArray: typing.Union[typing.List['ParameterDescriptor'], jpype.JArray]): ...
    def getMethod(self) -> java.lang.reflect.Method: ...
    def getParameterDescriptors(self) -> typing.MutableSequence['ParameterDescriptor']: ...

class ParameterDescriptor(FeatureDescriptor):
    def __init__(self): ...

class PropertyChangeListenerProxy(java.util.EventListenerProxy[PropertyChangeListener], PropertyChangeListener):
    def __init__(self, string: str, propertyChangeListener: PropertyChangeListener): ...
    def getPropertyName(self) -> str: ...
    def propertyChange(self, propertyChangeEvent: PropertyChangeEvent) -> None: ...

class PropertyDescriptor(FeatureDescriptor):
    @typing.overload
    def __init__(self, string: str, class_: typing.Type[typing.Any]): ...
    @typing.overload
    def __init__(self, string: str, class_: typing.Type[typing.Any], string2: str, string3: str): ...
    @typing.overload
    def __init__(self, string: str, method: java.lang.reflect.Method, method2: java.lang.reflect.Method): ...
    def createPropertyEditor(self, object: typing.Any) -> PropertyEditor: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getPropertyEditorClass(self) -> typing.Type[typing.Any]: ...
    def getPropertyType(self) -> typing.Type[typing.Any]: ...
    def getReadMethod(self) -> java.lang.reflect.Method: ...
    def getWriteMethod(self) -> java.lang.reflect.Method: ...
    def hashCode(self) -> int: ...
    def isBound(self) -> bool: ...
    def isConstrained(self) -> bool: ...
    def setBound(self, boolean: bool) -> None: ...
    def setConstrained(self, boolean: bool) -> None: ...
    def setPropertyEditorClass(self, class_: typing.Type[typing.Any]) -> None: ...
    def setReadMethod(self, method: java.lang.reflect.Method) -> None: ...
    def setWriteMethod(self, method: java.lang.reflect.Method) -> None: ...

class PropertyEditorSupport(PropertyEditor):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, object: typing.Any): ...
    def addPropertyChangeListener(self, propertyChangeListener: PropertyChangeListener) -> None: ...
    def firePropertyChange(self) -> None: ...
    def getAsText(self) -> str: ...
    def getCustomEditor(self) -> java.awt.Component: ...
    def getJavaInitializationString(self) -> str: ...
    def getSource(self) -> typing.Any: ...
    def getTags(self) -> typing.MutableSequence[str]: ...
    def getValue(self) -> typing.Any: ...
    def isPaintable(self) -> bool: ...
    def paintValue(self, graphics: java.awt.Graphics, rectangle: java.awt.Rectangle) -> None: ...
    def removePropertyChangeListener(self, propertyChangeListener: PropertyChangeListener) -> None: ...
    def setAsText(self, string: str) -> None: ...
    def setSource(self, object: typing.Any) -> None: ...
    def setValue(self, object: typing.Any) -> None: ...
    def supportsCustomEditor(self) -> bool: ...

class SimpleBeanInfo(BeanInfo):
    def __init__(self): ...
    def getAdditionalBeanInfo(self) -> typing.MutableSequence[BeanInfo]: ...
    def getBeanDescriptor(self) -> BeanDescriptor: ...
    def getDefaultEventIndex(self) -> int: ...
    def getDefaultPropertyIndex(self) -> int: ...
    def getEventSetDescriptors(self) -> typing.MutableSequence[EventSetDescriptor]: ...
    def getIcon(self, int: int) -> java.awt.Image: ...
    def getMethodDescriptors(self) -> typing.MutableSequence[MethodDescriptor]: ...
    def getPropertyDescriptors(self) -> typing.MutableSequence[PropertyDescriptor]: ...
    def loadImage(self, string: str) -> java.awt.Image: ...

class VetoableChangeListenerProxy(java.util.EventListenerProxy[VetoableChangeListener], VetoableChangeListener):
    def __init__(self, string: str, vetoableChangeListener: VetoableChangeListener): ...
    def getPropertyName(self) -> str: ...
    def vetoableChange(self, propertyChangeEvent: PropertyChangeEvent) -> None: ...

class XMLEncoder(Encoder, java.lang.AutoCloseable):
    @typing.overload
    def __init__(self, outputStream: java.io.OutputStream): ...
    @typing.overload
    def __init__(self, outputStream: java.io.OutputStream, string: str, boolean: bool, int: int): ...
    def close(self) -> None: ...
    def flush(self) -> None: ...
    def getOwner(self) -> typing.Any: ...
    def setOwner(self, object: typing.Any) -> None: ...
    def writeExpression(self, expression: Expression) -> None: ...
    def writeObject(self, object: typing.Any) -> None: ...
    def writeStatement(self, statement: Statement) -> None: ...

class IndexedPropertyDescriptor(PropertyDescriptor):
    @typing.overload
    def __init__(self, string: str, class_: typing.Type[typing.Any]): ...
    @typing.overload
    def __init__(self, string: str, class_: typing.Type[typing.Any], string2: str, string3: str, string4: str, string5: str): ...
    @typing.overload
    def __init__(self, string: str, method: java.lang.reflect.Method, method2: java.lang.reflect.Method, method3: java.lang.reflect.Method, method4: java.lang.reflect.Method): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getIndexedPropertyType(self) -> typing.Type[typing.Any]: ...
    def getIndexedReadMethod(self) -> java.lang.reflect.Method: ...
    def getIndexedWriteMethod(self) -> java.lang.reflect.Method: ...
    def hashCode(self) -> int: ...
    def setIndexedReadMethod(self, method: java.lang.reflect.Method) -> None: ...
    def setIndexedWriteMethod(self, method: java.lang.reflect.Method) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.beans")``.

    AppletInitializer: typing.Type[AppletInitializer]
    BeanDescriptor: typing.Type[BeanDescriptor]
    BeanInfo: typing.Type[BeanInfo]
    BeanProperty: typing.Type[BeanProperty]
    Beans: typing.Type[Beans]
    ConstructorProperties: typing.Type[ConstructorProperties]
    Customizer: typing.Type[Customizer]
    DefaultPersistenceDelegate: typing.Type[DefaultPersistenceDelegate]
    DesignMode: typing.Type[DesignMode]
    Encoder: typing.Type[Encoder]
    EventHandler: typing.Type[EventHandler]
    EventSetDescriptor: typing.Type[EventSetDescriptor]
    ExceptionListener: typing.Type[ExceptionListener]
    Expression: typing.Type[Expression]
    FeatureDescriptor: typing.Type[FeatureDescriptor]
    IndexedPropertyChangeEvent: typing.Type[IndexedPropertyChangeEvent]
    IndexedPropertyDescriptor: typing.Type[IndexedPropertyDescriptor]
    IntrospectionException: typing.Type[IntrospectionException]
    Introspector: typing.Type[Introspector]
    JavaBean: typing.Type[JavaBean]
    MethodDescriptor: typing.Type[MethodDescriptor]
    ParameterDescriptor: typing.Type[ParameterDescriptor]
    PersistenceDelegate: typing.Type[PersistenceDelegate]
    PropertyChangeEvent: typing.Type[PropertyChangeEvent]
    PropertyChangeListener: typing.Type[PropertyChangeListener]
    PropertyChangeListenerProxy: typing.Type[PropertyChangeListenerProxy]
    PropertyChangeSupport: typing.Type[PropertyChangeSupport]
    PropertyDescriptor: typing.Type[PropertyDescriptor]
    PropertyEditor: typing.Type[PropertyEditor]
    PropertyEditorManager: typing.Type[PropertyEditorManager]
    PropertyEditorSupport: typing.Type[PropertyEditorSupport]
    PropertyVetoException: typing.Type[PropertyVetoException]
    SimpleBeanInfo: typing.Type[SimpleBeanInfo]
    Statement: typing.Type[Statement]
    Transient: typing.Type[Transient]
    VetoableChangeListener: typing.Type[VetoableChangeListener]
    VetoableChangeListenerProxy: typing.Type[VetoableChangeListenerProxy]
    VetoableChangeSupport: typing.Type[VetoableChangeSupport]
    Visibility: typing.Type[Visibility]
    XMLDecoder: typing.Type[XMLDecoder]
    XMLEncoder: typing.Type[XMLEncoder]
    beancontext: java.beans.beancontext.__module_protocol__
