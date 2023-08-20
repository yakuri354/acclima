
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import groovyjarjarasm.asm
import org.codehaus.groovy.ast
import org.codehaus.groovy.ast.expr
import org.codehaus.groovy.ast.stmt
import org.codehaus.groovy.classgen.asm.sc
import org.codehaus.groovy.control
import org.codehaus.groovy.transform.stc
import typing



class BinaryExpressionTransformer:
    def __init__(self, staticCompilationTransformer: 'StaticCompilationTransformer'): ...

class BooleanExpressionTransformer:
    def __init__(self, staticCompilationTransformer: 'StaticCompilationTransformer'): ...

class CastExpressionOptimizer:
    def __init__(self, staticCompilationTransformer: 'StaticCompilationTransformer'): ...
    def transformCastExpression(self, castExpression: org.codehaus.groovy.ast.expr.CastExpression) -> org.codehaus.groovy.ast.expr.Expression: ...

class ClosureExpressionTransformer:
    def __init__(self, staticCompilationTransformer: 'StaticCompilationTransformer'): ...

class CompareIdentityExpression(org.codehaus.groovy.ast.expr.BinaryExpression, groovyjarjarasm.asm.Opcodes):
    def __init__(self, expression: org.codehaus.groovy.ast.expr.Expression, expression2: org.codehaus.groovy.ast.expr.Expression): ...
    def transformExpression(self, expressionTransformer: org.codehaus.groovy.ast.expr.ExpressionTransformer) -> org.codehaus.groovy.ast.expr.Expression: ...
    def visit(self, groovyCodeVisitor: org.codehaus.groovy.ast.GroovyCodeVisitor) -> None: ...

class CompareToNullExpression(org.codehaus.groovy.ast.expr.BinaryExpression, groovyjarjarasm.asm.Opcodes):
    def __init__(self, expression: org.codehaus.groovy.ast.expr.Expression, boolean: bool): ...
    def getObjectExpression(self) -> org.codehaus.groovy.ast.expr.Expression: ...
    def transformExpression(self, expressionTransformer: org.codehaus.groovy.ast.expr.ExpressionTransformer) -> org.codehaus.groovy.ast.expr.Expression: ...
    def visit(self, groovyCodeVisitor: org.codehaus.groovy.ast.GroovyCodeVisitor) -> None: ...

class ConstructorCallTransformer:
    def __init__(self, staticCompilationTransformer: 'StaticCompilationTransformer'): ...

class ListExpressionTransformer:
    def __init__(self, staticCompilationTransformer: 'StaticCompilationTransformer'): ...

class MethodCallExpressionTransformer:
    def __init__(self, staticCompilationTransformer: 'StaticCompilationTransformer'): ...

class RangeExpressionTransformer:
    def __init__(self, staticCompilationTransformer: 'StaticCompilationTransformer'): ...
    def transformRangeExpression(self, rangeExpression: org.codehaus.groovy.ast.expr.RangeExpression) -> org.codehaus.groovy.ast.expr.Expression: ...

class StaticCompilationTransformer(org.codehaus.groovy.ast.ClassCodeExpressionTransformer):
    def __init__(self, sourceUnit: org.codehaus.groovy.control.SourceUnit, staticTypeCheckingVisitor: org.codehaus.groovy.transform.stc.StaticTypeCheckingVisitor): ...
    def getClassNode(self) -> org.codehaus.groovy.ast.ClassNode: ...
    def getTypeChooser(self) -> org.codehaus.groovy.classgen.asm.sc.StaticTypesTypeChooser: ...
    def transform(self, expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.Expression: ...
    def visitClass(self, classNode: org.codehaus.groovy.ast.ClassNode) -> None: ...
    def visitClassCodeContainer(self, statement: org.codehaus.groovy.ast.stmt.Statement) -> None: ...

class StaticMethodCallExpressionTransformer:
    def __init__(self, staticCompilationTransformer: StaticCompilationTransformer): ...

class VariableExpressionTransformer:
    def __init__(self): ...
    def transformVariableExpression(self, variableExpression: org.codehaus.groovy.ast.expr.VariableExpression) -> org.codehaus.groovy.ast.expr.Expression: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.transform.sc.transformers")``.

    BinaryExpressionTransformer: typing.Type[BinaryExpressionTransformer]
    BooleanExpressionTransformer: typing.Type[BooleanExpressionTransformer]
    CastExpressionOptimizer: typing.Type[CastExpressionOptimizer]
    ClosureExpressionTransformer: typing.Type[ClosureExpressionTransformer]
    CompareIdentityExpression: typing.Type[CompareIdentityExpression]
    CompareToNullExpression: typing.Type[CompareToNullExpression]
    ConstructorCallTransformer: typing.Type[ConstructorCallTransformer]
    ListExpressionTransformer: typing.Type[ListExpressionTransformer]
    MethodCallExpressionTransformer: typing.Type[MethodCallExpressionTransformer]
    RangeExpressionTransformer: typing.Type[RangeExpressionTransformer]
    StaticCompilationTransformer: typing.Type[StaticCompilationTransformer]
    StaticMethodCallExpressionTransformer: typing.Type[StaticMethodCallExpressionTransformer]
    VariableExpressionTransformer: typing.Type[VariableExpressionTransformer]
