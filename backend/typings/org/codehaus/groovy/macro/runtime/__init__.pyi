
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import groovy.lang
import java.lang
import java.lang.annotation
import java.util
import org.codehaus.groovy.ast
import org.codehaus.groovy.ast.expr
import org.codehaus.groovy.ast.stmt
import org.codehaus.groovy.control
import typing



class Macro(java.lang.annotation.Annotation):
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class MacroBuilder(java.lang.Enum['MacroBuilder']):
    INSTANCE: typing.ClassVar['MacroBuilder'] = ...
    @staticmethod
    def getMacroValue(blockStatement: org.codehaus.groovy.ast.stmt.BlockStatement, boolean: bool) -> org.codehaus.groovy.ast.ASTNode: ...
    _macro_0__T = typing.TypeVar('_macro_0__T')  # <T>
    _macro_1__T = typing.TypeVar('_macro_1__T')  # <T>
    _macro_2__T = typing.TypeVar('_macro_2__T')  # <T>
    _macro_3__T = typing.TypeVar('_macro_3__T')  # <T>
    @typing.overload
    def macro(self, boolean: bool, string: str, list: java.util.List[groovy.lang.Closure[org.codehaus.groovy.ast.expr.Expression]], class_: typing.Type[_macro_0__T]) -> _macro_0__T: ...
    @typing.overload
    def macro(self, string: str, list: java.util.List[groovy.lang.Closure[org.codehaus.groovy.ast.expr.Expression]], class_: typing.Type[_macro_1__T]) -> _macro_1__T: ...
    @typing.overload
    def macro(self, compilePhase: org.codehaus.groovy.control.CompilePhase, boolean: bool, string: str, list: java.util.List[groovy.lang.Closure[org.codehaus.groovy.ast.expr.Expression]], class_: typing.Type[_macro_2__T]) -> _macro_2__T: ...
    @typing.overload
    def macro(self, compilePhase: org.codehaus.groovy.control.CompilePhase, string: str, list: java.util.List[groovy.lang.Closure[org.codehaus.groovy.ast.expr.Expression]], class_: typing.Type[_macro_3__T]) -> _macro_3__T: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'MacroBuilder': ...
    @staticmethod
    def values() -> typing.MutableSequence['MacroBuilder']: ...

class MacroContext:
    def __init__(self, compilationUnit: org.codehaus.groovy.control.CompilationUnit, sourceUnit: org.codehaus.groovy.control.SourceUnit, methodCallExpression: org.codehaus.groovy.ast.expr.MethodCallExpression): ...
    def getCall(self) -> org.codehaus.groovy.ast.expr.MethodCallExpression: ...
    def getCompilationUnit(self) -> org.codehaus.groovy.control.CompilationUnit: ...
    def getSourceUnit(self) -> org.codehaus.groovy.control.SourceUnit: ...

class MacroStub(java.lang.Enum['MacroStub']):
    INSTANCE: typing.ClassVar['MacroStub'] = ...
    _macroMethod__T = typing.TypeVar('_macroMethod__T')  # <T>
    def macroMethod(self, t: _macroMethod__T) -> _macroMethod__T: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'MacroStub': ...
    @staticmethod
    def values() -> typing.MutableSequence['MacroStub']: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.macro.runtime")``.

    Macro: typing.Type[Macro]
    MacroBuilder: typing.Type[MacroBuilder]
    MacroContext: typing.Type[MacroContext]
    MacroStub: typing.Type[MacroStub]
