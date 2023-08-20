
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang.reflect
import jpype
import org.codehaus.groovy.ast
import org.codehaus.groovy.vmplugin.v5
import org.codehaus.groovy.vmplugin.v6
import org.codehaus.groovy.vmplugin.v7
import org.codehaus.groovy.vmplugin.v8
import org.codehaus.groovy.vmplugin.v9
import typing



class VMPlugin:
    def configureAnnotation(self, annotationNode: org.codehaus.groovy.ast.AnnotationNode) -> None: ...
    def configureAnnotationNodeFromDefinition(self, annotationNode: org.codehaus.groovy.ast.AnnotationNode, annotationNode2: org.codehaus.groovy.ast.AnnotationNode) -> None: ...
    def configureClassNode(self, compileUnit: org.codehaus.groovy.ast.CompileUnit, classNode: org.codehaus.groovy.ast.ClassNode) -> None: ...
    def getInvokeSpecialHandle(self, method: java.lang.reflect.Method, object: typing.Any) -> typing.Any: ...
    def getPluginDefaultGroovyMethods(self) -> typing.MutableSequence[typing.Type]: ...
    def getPluginStaticGroovyMethods(self) -> typing.MutableSequence[typing.Type]: ...
    def getVersion(self) -> int: ...
    def invalidateCallSites(self) -> None: ...
    def invokeHandle(self, object: typing.Any, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]) -> typing.Any: ...
    def setAdditionalClassInformation(self, classNode: org.codehaus.groovy.ast.ClassNode) -> None: ...

class VMPluginFactory:
    def __init__(self): ...
    @staticmethod
    def getPlugin() -> VMPlugin: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.vmplugin")``.

    VMPlugin: typing.Type[VMPlugin]
    VMPluginFactory: typing.Type[VMPluginFactory]
    v5: org.codehaus.groovy.vmplugin.v5.__module_protocol__
    v6: org.codehaus.groovy.vmplugin.v6.__module_protocol__
    v7: org.codehaus.groovy.vmplugin.v7.__module_protocol__
    v8: org.codehaus.groovy.vmplugin.v8.__module_protocol__
    v9: org.codehaus.groovy.vmplugin.v9.__module_protocol__
