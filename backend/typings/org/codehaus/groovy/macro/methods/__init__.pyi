
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import groovy.lang
import org.codehaus.groovy.ast
import org.codehaus.groovy.ast.expr
import org.codehaus.groovy.control
import org.codehaus.groovy.macro.runtime
import typing



class MacroGroovyMethods:
    DOLLAR_VALUE: typing.ClassVar[str] = ...
    def __init__(self): ...
    @staticmethod
    def buildSubstitutions(sourceUnit: org.codehaus.groovy.control.SourceUnit, aSTNode: org.codehaus.groovy.ast.ASTNode) -> org.codehaus.groovy.ast.expr.ListExpression: ...
    _macro_0__T = typing.TypeVar('_macro_0__T')  # <T>
    _macro_1__T = typing.TypeVar('_macro_1__T')  # <T>
    _macro_2__T = typing.TypeVar('_macro_2__T')  # <T>
    _macro_3__T = typing.TypeVar('_macro_3__T')  # <T>
    @typing.overload
    @staticmethod
    def macro(object: typing.Any, boolean: bool, closure: groovy.lang.Closure) -> _macro_0__T: ...
    @typing.overload
    @staticmethod
    def macro(object: typing.Any, closure: groovy.lang.Closure) -> _macro_1__T: ...
    @typing.overload
    @staticmethod
    def macro(object: typing.Any, compilePhase: org.codehaus.groovy.control.CompilePhase, boolean: bool, closure: groovy.lang.Closure) -> _macro_2__T: ...
    @typing.overload
    @staticmethod
    def macro(object: typing.Any, compilePhase: org.codehaus.groovy.control.CompilePhase, closure: groovy.lang.Closure) -> _macro_3__T: ...
    @typing.overload
    @staticmethod
    def macro(macroContext: org.codehaus.groovy.macro.runtime.MacroContext, closureExpression: org.codehaus.groovy.ast.expr.ClosureExpression) -> org.codehaus.groovy.ast.expr.Expression: ...
    @typing.overload
    @staticmethod
    def macro(macroContext: org.codehaus.groovy.macro.runtime.MacroContext, constantExpression: org.codehaus.groovy.ast.expr.ConstantExpression, closureExpression: org.codehaus.groovy.ast.expr.ClosureExpression) -> org.codehaus.groovy.ast.expr.Expression: ...
    @typing.overload
    @staticmethod
    def macro(macroContext: org.codehaus.groovy.macro.runtime.MacroContext, propertyExpression: org.codehaus.groovy.ast.expr.PropertyExpression, closureExpression: org.codehaus.groovy.ast.expr.ClosureExpression) -> org.codehaus.groovy.ast.expr.Expression: ...
    @typing.overload
    @staticmethod
    def macro(macroContext: org.codehaus.groovy.macro.runtime.MacroContext, propertyExpression: org.codehaus.groovy.ast.expr.PropertyExpression, constantExpression: org.codehaus.groovy.ast.expr.ConstantExpression, closureExpression: org.codehaus.groovy.ast.expr.ClosureExpression) -> org.codehaus.groovy.ast.expr.Expression: ...
    class MacroValuePlaceholder:
        def __init__(self): ...
        @staticmethod
        def $v(closure: groovy.lang.Closure) -> typing.Any: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.macro.methods")``.

    MacroGroovyMethods: typing.Type[MacroGroovyMethods]
