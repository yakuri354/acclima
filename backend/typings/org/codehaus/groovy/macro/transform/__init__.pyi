
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import groovy.transform
import org.codehaus.groovy.ast
import org.codehaus.groovy.control
import typing



class MacroClass:
    def __init__(self): ...

class MacroClassTransformation(org.codehaus.groovy.ast.MethodCallTransformation):
    def __init__(self): ...

class MacroTransformation(org.codehaus.groovy.ast.MethodCallTransformation, groovy.transform.CompilationUnitAware):
    def __init__(self): ...
    def setCompilationUnit(self, compilationUnit: org.codehaus.groovy.control.CompilationUnit) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.macro.transform")``.

    MacroClass: typing.Type[MacroClass]
    MacroClassTransformation: typing.Type[MacroClassTransformation]
    MacroTransformation: typing.Type[MacroTransformation]
