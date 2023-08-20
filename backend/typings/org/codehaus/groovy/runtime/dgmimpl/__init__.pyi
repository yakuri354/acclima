
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import _jpype
import groovy.lang
import java.lang
import jpype
import org.codehaus.groovy.reflection
import org.codehaus.groovy.runtime.callsite
import org.codehaus.groovy.runtime.dgmimpl.arrays
import typing



class NumberNumberMetaMethod(org.codehaus.groovy.runtime.callsite.CallSiteAwareMetaMethod):
    def createDoubleDouble(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createDoubleFloat(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createDoubleInteger(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createDoubleLong(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createFloatDouble(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createFloatFloat(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createFloatInteger(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createFloatLong(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createIntegerDouble(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createIntegerFloat(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createIntegerInteger(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createIntegerLong(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createLongDouble(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createLongFloat(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createLongInteger(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createLongLong(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createNumberNumber(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createPojoCallSite(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def getDeclaringClass(self) -> org.codehaus.groovy.reflection.CachedClass: ...
    def getModifiers(self) -> int: ...
    def getReturnType(self) -> typing.Type: ...
    class NumberNumberCallSite(org.codehaus.groovy.runtime.callsite.PojoMetaMethodSite):
        def __init__(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], number: typing.Union[_jpype._JNumberLong, _jpype._JNumberFloat, typing.SupportsIndex, typing.SupportsFloat], number2: typing.Union[_jpype._JNumberLong, _jpype._JNumberFloat, typing.SupportsIndex, typing.SupportsFloat]): ...

class NumberNumberDiv(NumberNumberMetaMethod):
    def __init__(self): ...
    def createDoubleDouble(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createDoubleFloat(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createDoubleInteger(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createDoubleLong(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createFloatDouble(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createFloatFloat(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createFloatInteger(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createFloatLong(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createIntegerDouble(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createIntegerFloat(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createIntegerInteger(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createIntegerLong(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createLongDouble(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createLongFloat(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createLongInteger(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createLongLong(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createNumberNumber(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    @staticmethod
    def div(number: typing.Union[_jpype._JNumberLong, _jpype._JNumberFloat, typing.SupportsIndex, typing.SupportsFloat], number2: typing.Union[_jpype._JNumberLong, _jpype._JNumberFloat, typing.SupportsIndex, typing.SupportsFloat]) -> java.lang.Number: ...
    def getName(self) -> str: ...
    def invoke(self, object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> typing.Any: ...

class NumberNumberMinus(NumberNumberMetaMethod):
    def __init__(self): ...
    def createDoubleDouble(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createDoubleFloat(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createDoubleInteger(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createDoubleLong(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createFloatDouble(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createFloatFloat(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createFloatInteger(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createFloatLong(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createIntegerDouble(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createIntegerFloat(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createIntegerInteger(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createIntegerLong(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createLongDouble(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createLongFloat(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createLongInteger(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createLongLong(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createNumberNumber(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def getName(self) -> str: ...
    def invoke(self, object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> typing.Any: ...
    @staticmethod
    def minus(number: typing.Union[_jpype._JNumberLong, _jpype._JNumberFloat, typing.SupportsIndex, typing.SupportsFloat], number2: typing.Union[_jpype._JNumberLong, _jpype._JNumberFloat, typing.SupportsIndex, typing.SupportsFloat]) -> java.lang.Number: ...

class NumberNumberMultiply(NumberNumberMetaMethod):
    def __init__(self): ...
    def createDoubleDouble(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createDoubleFloat(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createDoubleInteger(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createDoubleLong(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createFloatDouble(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createFloatFloat(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createFloatInteger(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createFloatLong(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createIntegerDouble(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createIntegerFloat(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createIntegerInteger(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createIntegerLong(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createLongDouble(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createLongFloat(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createLongInteger(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createLongLong(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createNumberNumber(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def getName(self) -> str: ...
    def invoke(self, object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> typing.Any: ...
    @staticmethod
    def multiply(number: typing.Union[_jpype._JNumberLong, _jpype._JNumberFloat, typing.SupportsIndex, typing.SupportsFloat], number2: typing.Union[_jpype._JNumberLong, _jpype._JNumberFloat, typing.SupportsIndex, typing.SupportsFloat]) -> java.lang.Number: ...

class NumberNumberPlus(NumberNumberMetaMethod):
    def __init__(self): ...
    def createDoubleDouble(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createDoubleFloat(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createDoubleInteger(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createDoubleLong(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createFloatDouble(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createFloatFloat(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createFloatInteger(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createFloatLong(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createIntegerDouble(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createIntegerFloat(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createIntegerInteger(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createIntegerLong(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createLongDouble(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createLongFloat(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createLongInteger(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createLongLong(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def createNumberNumber(self, callSite: org.codehaus.groovy.runtime.callsite.CallSite, metaClassImpl: groovy.lang.MetaClassImpl, metaMethod: groovy.lang.MetaMethod, classArray: typing.Union[typing.List[typing.Type], jpype.JArray], object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> org.codehaus.groovy.runtime.callsite.CallSite: ...
    def getName(self) -> str: ...
    def invoke(self, object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> typing.Any: ...
    @staticmethod
    def plus(number: typing.Union[_jpype._JNumberLong, _jpype._JNumberFloat, typing.SupportsIndex, typing.SupportsFloat], number2: typing.Union[_jpype._JNumberLong, _jpype._JNumberFloat, typing.SupportsIndex, typing.SupportsFloat]) -> java.lang.Number: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.runtime.dgmimpl")``.

    NumberNumberDiv: typing.Type[NumberNumberDiv]
    NumberNumberMetaMethod: typing.Type[NumberNumberMetaMethod]
    NumberNumberMinus: typing.Type[NumberNumberMinus]
    NumberNumberMultiply: typing.Type[NumberNumberMultiply]
    NumberNumberPlus: typing.Type[NumberNumberPlus]
    arrays: org.codehaus.groovy.runtime.dgmimpl.arrays.__module_protocol__