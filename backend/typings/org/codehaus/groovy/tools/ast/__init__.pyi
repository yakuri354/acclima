
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import groovy.lang
import java.io
import jpype.protocol
import org.codehaus.groovy.control
import org.codehaus.groovy.transform
import typing



class TransformTestHelper(groovy.lang.GroovyObject):
    def __init__(self, aSTTransformation: org.codehaus.groovy.transform.ASTTransformation, compilePhase: org.codehaus.groovy.control.CompilePhase): ...
    @typing.overload
    def parse(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> typing.Type: ...
    @typing.overload
    def parse(self, string: str) -> typing.Type: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.tools.ast")``.

    TransformTestHelper: typing.Type[TransformTestHelper]
