
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org.codehaus.groovy.ast
import org.codehaus.groovy.ast.expr
import org.codehaus.groovy.ast.stmt
import org.codehaus.groovy.control
import typing



class DependencyTracker(org.codehaus.groovy.ast.ClassCodeVisitorSupport):
    @typing.overload
    def __init__(self, sourceUnit: org.codehaus.groovy.control.SourceUnit, stringSetMap: 'StringSetMap'): ...
    @typing.overload
    def __init__(self, sourceUnit: org.codehaus.groovy.control.SourceUnit, stringSetMap: 'StringSetMap', map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]): ...
    def visitAnnotations(self, annotatedNode: org.codehaus.groovy.ast.AnnotatedNode) -> None: ...
    def visitArrayExpression(self, arrayExpression: org.codehaus.groovy.ast.expr.ArrayExpression) -> None: ...
    def visitCastExpression(self, castExpression: org.codehaus.groovy.ast.expr.CastExpression) -> None: ...
    def visitCatchStatement(self, catchStatement: org.codehaus.groovy.ast.stmt.CatchStatement) -> None: ...
    def visitClass(self, classNode: org.codehaus.groovy.ast.ClassNode) -> None: ...
    def visitClassExpression(self, classExpression: org.codehaus.groovy.ast.expr.ClassExpression) -> None: ...
    def visitConstructorCallExpression(self, constructorCallExpression: org.codehaus.groovy.ast.expr.ConstructorCallExpression) -> None: ...
    def visitField(self, fieldNode: org.codehaus.groovy.ast.FieldNode) -> None: ...
    def visitMethod(self, methodNode: org.codehaus.groovy.ast.MethodNode) -> None: ...
    def visitVariableExpression(self, variableExpression: org.codehaus.groovy.ast.expr.VariableExpression) -> None: ...

class StringSetMap(java.util.LinkedHashMap[str, java.util.Set[str]]):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, stringSetMap: 'StringSetMap'): ...
    def get(self, object: typing.Any) -> java.util.Set[str]: ...
    def makeTransitiveHull(self) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.tools.gse")``.

    DependencyTracker: typing.Type[DependencyTracker]
    StringSetMap: typing.Type[StringSetMap]
