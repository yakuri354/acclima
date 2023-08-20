
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import org.codehaus.groovy.ant
import org.codehaus.groovy.antlr
import org.codehaus.groovy.ast
import org.codehaus.groovy.binding
import org.codehaus.groovy.classgen
import org.codehaus.groovy.control
import org.codehaus.groovy.groovydoc
import org.codehaus.groovy.jsr223
import org.codehaus.groovy.macro
import org.codehaus.groovy.plugin
import org.codehaus.groovy.reflection
import org.codehaus.groovy.runtime
import org.codehaus.groovy.syntax
import org.codehaus.groovy.testng
import org.codehaus.groovy.tools
import org.codehaus.groovy.transform
import org.codehaus.groovy.util
import org.codehaus.groovy.vmplugin
import typing



class GroovyBugError(java.lang.AssertionError):
    @typing.overload
    def __init__(self, exception: java.lang.Exception): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...
    def getBugText(self) -> str: ...
    def getCause(self) -> java.lang.Throwable: ...
    def getMessage(self) -> str: ...
    def setBugText(self, string: str) -> None: ...
    def toString(self) -> str: ...

class GroovyExceptionInterface:
    def isFatal(self) -> bool: ...
    def setFatal(self, boolean: bool) -> None: ...

class GroovyException(java.lang.Exception, GroovyExceptionInterface):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, boolean: bool): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, boolean: bool): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    def isFatal(self) -> bool: ...
    def setFatal(self, boolean: bool) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy")``.

    GroovyBugError: typing.Type[GroovyBugError]
    GroovyException: typing.Type[GroovyException]
    GroovyExceptionInterface: typing.Type[GroovyExceptionInterface]
    ant: org.codehaus.groovy.ant.__module_protocol__
    antlr: org.codehaus.groovy.antlr.__module_protocol__
    ast: org.codehaus.groovy.ast.__module_protocol__
    binding: org.codehaus.groovy.binding.__module_protocol__
    classgen: org.codehaus.groovy.classgen.__module_protocol__
    control: org.codehaus.groovy.control.__module_protocol__
    groovydoc: org.codehaus.groovy.groovydoc.__module_protocol__
    jsr223: org.codehaus.groovy.jsr223.__module_protocol__
    macro: org.codehaus.groovy.macro.__module_protocol__
    plugin: org.codehaus.groovy.plugin.__module_protocol__
    reflection: org.codehaus.groovy.reflection.__module_protocol__
    runtime: org.codehaus.groovy.runtime.__module_protocol__
    syntax: org.codehaus.groovy.syntax.__module_protocol__
    testng: org.codehaus.groovy.testng.__module_protocol__
    tools: org.codehaus.groovy.tools.__module_protocol__
    transform: org.codehaus.groovy.transform.__module_protocol__
    util: org.codehaus.groovy.util.__module_protocol__
    vmplugin: org.codehaus.groovy.vmplugin.__module_protocol__
