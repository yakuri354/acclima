
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import groovy.lang
import java.util
import org.codehaus.groovy.ast
import org.codehaus.groovy.ast.expr
import org.codehaus.groovy.ast.stmt
import org.codehaus.groovy.classgen
import org.codehaus.groovy.macro.matcher.internal
import org.codehaus.groovy.syntax
import typing



class ASTNodePredicate:
    def matches(self, aSTNode: org.codehaus.groovy.ast.ASTNode) -> bool: ...

class ContextualClassCodeVisitor(org.codehaus.groovy.ast.ClassCodeVisitorSupport):
    def __init__(self): ...
    def getLastContext(self) -> 'TreeContext': ...
    def getTreeContext(self) -> 'TreeContext': ...
    def getTreePath(self) -> java.util.List['TreeContext']: ...
    @staticmethod
    def matchByClass(*class_: typing.Type[org.codehaus.groovy.ast.ASTNode]) -> java.util.List[ASTNodePredicate]: ...
    def pathMatches(self, list: java.util.List[ASTNodePredicate]) -> java.util.List['TreeContext']: ...
    @typing.overload
    def pathUpTo(self, class_: typing.Type[org.codehaus.groovy.ast.ASTNode]) -> java.util.List['TreeContext']: ...
    @typing.overload
    def pathUpTo(self, class_: typing.Type[org.codehaus.groovy.ast.ASTNode], aSTNodePredicate: ASTNodePredicate) -> java.util.List['TreeContext']: ...
    @typing.overload
    def pathUpTo(self, aSTNodePredicate: ASTNodePredicate) -> java.util.List['TreeContext']: ...
    def visitArrayExpression(self, arrayExpression: org.codehaus.groovy.ast.expr.ArrayExpression) -> None: ...
    def visitAssertStatement(self, assertStatement: org.codehaus.groovy.ast.stmt.AssertStatement) -> None: ...
    def visitAttributeExpression(self, attributeExpression: org.codehaus.groovy.ast.expr.AttributeExpression) -> None: ...
    def visitBinaryExpression(self, binaryExpression: org.codehaus.groovy.ast.expr.BinaryExpression) -> None: ...
    def visitBitwiseNegationExpression(self, bitwiseNegationExpression: org.codehaus.groovy.ast.expr.BitwiseNegationExpression) -> None: ...
    def visitBlockStatement(self, blockStatement: org.codehaus.groovy.ast.stmt.BlockStatement) -> None: ...
    def visitBooleanExpression(self, booleanExpression: org.codehaus.groovy.ast.expr.BooleanExpression) -> None: ...
    def visitBreakStatement(self, breakStatement: org.codehaus.groovy.ast.stmt.BreakStatement) -> None: ...
    def visitBytecodeExpression(self, bytecodeExpression: org.codehaus.groovy.classgen.BytecodeExpression) -> None: ...
    def visitCaseStatement(self, caseStatement: org.codehaus.groovy.ast.stmt.CaseStatement) -> None: ...
    def visitCastExpression(self, castExpression: org.codehaus.groovy.ast.expr.CastExpression) -> None: ...
    def visitCatchStatement(self, catchStatement: org.codehaus.groovy.ast.stmt.CatchStatement) -> None: ...
    def visitClass(self, classNode: org.codehaus.groovy.ast.ClassNode) -> None: ...
    def visitClassExpression(self, classExpression: org.codehaus.groovy.ast.expr.ClassExpression) -> None: ...
    def visitClosureExpression(self, closureExpression: org.codehaus.groovy.ast.expr.ClosureExpression) -> None: ...
    def visitClosureListExpression(self, closureListExpression: org.codehaus.groovy.ast.expr.ClosureListExpression) -> None: ...
    def visitConstantExpression(self, constantExpression: org.codehaus.groovy.ast.expr.ConstantExpression) -> None: ...
    def visitConstructorCallExpression(self, constructorCallExpression: org.codehaus.groovy.ast.expr.ConstructorCallExpression) -> None: ...
    def visitContinueStatement(self, continueStatement: org.codehaus.groovy.ast.stmt.ContinueStatement) -> None: ...
    def visitDoWhileLoop(self, doWhileStatement: org.codehaus.groovy.ast.stmt.DoWhileStatement) -> None: ...
    def visitExpressionStatement(self, expressionStatement: org.codehaus.groovy.ast.stmt.ExpressionStatement) -> None: ...
    def visitField(self, fieldNode: org.codehaus.groovy.ast.FieldNode) -> None: ...
    def visitFieldExpression(self, fieldExpression: org.codehaus.groovy.ast.expr.FieldExpression) -> None: ...
    def visitForLoop(self, forStatement: org.codehaus.groovy.ast.stmt.ForStatement) -> None: ...
    def visitGStringExpression(self, gStringExpression: org.codehaus.groovy.ast.expr.GStringExpression) -> None: ...
    def visitIfElse(self, ifStatement: org.codehaus.groovy.ast.stmt.IfStatement) -> None: ...
    def visitImports(self, moduleNode: org.codehaus.groovy.ast.ModuleNode) -> None: ...
    def visitListExpression(self, listExpression: org.codehaus.groovy.ast.expr.ListExpression) -> None: ...
    def visitMapEntryExpression(self, mapEntryExpression: org.codehaus.groovy.ast.expr.MapEntryExpression) -> None: ...
    def visitMapExpression(self, mapExpression: org.codehaus.groovy.ast.expr.MapExpression) -> None: ...
    def visitMethodCallExpression(self, methodCallExpression: org.codehaus.groovy.ast.expr.MethodCallExpression) -> None: ...
    def visitMethodPointerExpression(self, methodPointerExpression: org.codehaus.groovy.ast.expr.MethodPointerExpression) -> None: ...
    def visitNotExpression(self, notExpression: org.codehaus.groovy.ast.expr.NotExpression) -> None: ...
    def visitPackage(self, packageNode: org.codehaus.groovy.ast.PackageNode) -> None: ...
    def visitPostfixExpression(self, postfixExpression: org.codehaus.groovy.ast.expr.PostfixExpression) -> None: ...
    def visitPrefixExpression(self, prefixExpression: org.codehaus.groovy.ast.expr.PrefixExpression) -> None: ...
    def visitProperty(self, propertyNode: org.codehaus.groovy.ast.PropertyNode) -> None: ...
    def visitPropertyExpression(self, propertyExpression: org.codehaus.groovy.ast.expr.PropertyExpression) -> None: ...
    def visitRangeExpression(self, rangeExpression: org.codehaus.groovy.ast.expr.RangeExpression) -> None: ...
    def visitReturnStatement(self, returnStatement: org.codehaus.groovy.ast.stmt.ReturnStatement) -> None: ...
    def visitShortTernaryExpression(self, elvisOperatorExpression: org.codehaus.groovy.ast.expr.ElvisOperatorExpression) -> None: ...
    def visitSpreadExpression(self, spreadExpression: org.codehaus.groovy.ast.expr.SpreadExpression) -> None: ...
    def visitSpreadMapExpression(self, spreadMapExpression: org.codehaus.groovy.ast.expr.SpreadMapExpression) -> None: ...
    def visitStaticMethodCallExpression(self, staticMethodCallExpression: org.codehaus.groovy.ast.expr.StaticMethodCallExpression) -> None: ...
    def visitSwitch(self, switchStatement: org.codehaus.groovy.ast.stmt.SwitchStatement) -> None: ...
    def visitSynchronizedStatement(self, synchronizedStatement: org.codehaus.groovy.ast.stmt.SynchronizedStatement) -> None: ...
    def visitTernaryExpression(self, ternaryExpression: org.codehaus.groovy.ast.expr.TernaryExpression) -> None: ...
    def visitThrowStatement(self, throwStatement: org.codehaus.groovy.ast.stmt.ThrowStatement) -> None: ...
    def visitTryCatchFinally(self, tryCatchStatement: org.codehaus.groovy.ast.stmt.TryCatchStatement) -> None: ...
    def visitTupleExpression(self, tupleExpression: org.codehaus.groovy.ast.expr.TupleExpression) -> None: ...
    def visitUnaryMinusExpression(self, unaryMinusExpression: org.codehaus.groovy.ast.expr.UnaryMinusExpression) -> None: ...
    def visitUnaryPlusExpression(self, unaryPlusExpression: org.codehaus.groovy.ast.expr.UnaryPlusExpression) -> None: ...
    def visitVariableExpression(self, variableExpression: org.codehaus.groovy.ast.expr.VariableExpression) -> None: ...
    def visitWhileLoop(self, whileStatement: org.codehaus.groovy.ast.stmt.WhileStatement) -> None: ...

class MatchingConstraints(groovy.lang.GroovyObject):
    ANY_TOKEN: typing.ClassVar[org.codehaus.groovy.macro.matcher.internal.ConstraintPredicate] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, map: typing.Union[java.util.Map, typing.Mapping]): ...
    @typing.overload
    def __init__(self, set: java.util.Set[str], constraintPredicate: org.codehaus.groovy.macro.matcher.internal.ConstraintPredicate[org.codehaus.groovy.syntax.Token], constraintPredicate2: org.codehaus.groovy.macro.matcher.internal.ConstraintPredicate['TreeContext']): ...
    def canEqual(self, object: typing.Any) -> bool: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getEventually(self) -> org.codehaus.groovy.macro.matcher.internal.ConstraintPredicate['TreeContext']: ...
    def getPlaceholders(self) -> java.util.Set[str]: ...
    def getTokenPredicate(self) -> org.codehaus.groovy.macro.matcher.internal.ConstraintPredicate[org.codehaus.groovy.syntax.Token]: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class NodeComparator:
    def equals(self, aSTNode: org.codehaus.groovy.ast.ASTNode, aSTNode2: org.codehaus.groovy.ast.ASTNode) -> bool: ...

class TreeContext:
    @typing.overload
    def afterVisit(self, closure: groovy.lang.Closure[typing.Any]) -> None: ...
    @typing.overload
    def afterVisit(self, treeContextAction: 'TreeContextAction') -> None: ...
    def fork(self, aSTNode: org.codehaus.groovy.ast.ASTNode) -> 'TreeContext': ...
    def getNode(self) -> org.codehaus.groovy.ast.ASTNode: ...
    def getOnPopHandlers(self) -> java.util.List['TreeContextAction']: ...
    def getParent(self) -> 'TreeContext': ...
    def getReplacement(self) -> org.codehaus.groovy.ast.expr.Expression: ...
    def getSiblings(self) -> java.util.List['TreeContext']: ...
    @typing.overload
    def getUserdata(self, object: typing.Any) -> java.util.List[typing.Any]: ...
    @typing.overload
    def getUserdata(self, object: typing.Any, boolean: bool) -> java.util.List[typing.Any]: ...
    @typing.overload
    def getUserdata(self) -> java.util.Map[typing.Any, java.util.List[typing.Any]]: ...
    @typing.overload
    def matches(self, closure: groovy.lang.Closure[bool]) -> bool: ...
    @typing.overload
    def matches(self, aSTNodePredicate: ASTNodePredicate) -> bool: ...
    def putUserdata(self, object: typing.Any, object2: typing.Any) -> None: ...
    def setReplacement(self, expression: org.codehaus.groovy.ast.expr.Expression) -> None: ...
    def toString(self) -> str: ...

class TreeContextAction:
    def call(self, treeContext: TreeContext) -> None: ...

class ASTMatcher(ContextualClassCodeVisitor, groovy.lang.GroovyObject):
    WILDCARD: typing.ClassVar[str] = ...
    @staticmethod
    def find(aSTNode: org.codehaus.groovy.ast.ASTNode, aSTNode2: org.codehaus.groovy.ast.ASTNode) -> java.util.List[TreeContext]: ...
    _ifConstraint__T = typing.TypeVar('_ifConstraint__T')  # <T>
    def ifConstraint(self, t: _ifConstraint__T, closure: groovy.lang.Closure[_ifConstraint__T]) -> _ifConstraint__T: ...
    @staticmethod
    def matches(aSTNode: org.codehaus.groovy.ast.ASTNode, aSTNode2: org.codehaus.groovy.ast.ASTNode) -> bool: ...
    def visitAnnotations(self, annotatedNode: org.codehaus.groovy.ast.AnnotatedNode) -> None: ...
    def visitArgumentlistExpression(self, argumentListExpression: org.codehaus.groovy.ast.expr.ArgumentListExpression) -> None: ...
    def visitArrayExpression(self, arrayExpression: org.codehaus.groovy.ast.expr.ArrayExpression) -> None: ...
    def visitAttributeExpression(self, attributeExpression: org.codehaus.groovy.ast.expr.AttributeExpression) -> None: ...
    def visitBinaryExpression(self, binaryExpression: org.codehaus.groovy.ast.expr.BinaryExpression) -> None: ...
    def visitBitwiseNegationExpression(self, bitwiseNegationExpression: org.codehaus.groovy.ast.expr.BitwiseNegationExpression) -> None: ...
    def visitBlockStatement(self, blockStatement: org.codehaus.groovy.ast.stmt.BlockStatement) -> None: ...
    def visitBooleanExpression(self, booleanExpression: org.codehaus.groovy.ast.expr.BooleanExpression) -> None: ...
    def visitBytecodeExpression(self, bytecodeExpression: org.codehaus.groovy.classgen.BytecodeExpression) -> None: ...
    def visitCastExpression(self, castExpression: org.codehaus.groovy.ast.expr.CastExpression) -> None: ...
    def visitClass(self, classNode: org.codehaus.groovy.ast.ClassNode) -> None: ...
    def visitClassExpression(self, classExpression: org.codehaus.groovy.ast.expr.ClassExpression) -> None: ...
    def visitClosureExpression(self, closureExpression: org.codehaus.groovy.ast.expr.ClosureExpression) -> None: ...
    def visitClosureListExpression(self, closureListExpression: org.codehaus.groovy.ast.expr.ClosureListExpression) -> None: ...
    def visitConstantExpression(self, constantExpression: org.codehaus.groovy.ast.expr.ConstantExpression) -> None: ...
    def visitConstructorCallExpression(self, constructorCallExpression: org.codehaus.groovy.ast.expr.ConstructorCallExpression) -> None: ...
    def visitDeclarationExpression(self, declarationExpression: org.codehaus.groovy.ast.expr.DeclarationExpression) -> None: ...
    def visitExpressionStatement(self, expressionStatement: org.codehaus.groovy.ast.stmt.ExpressionStatement) -> None: ...
    def visitField(self, fieldNode: org.codehaus.groovy.ast.FieldNode) -> None: ...
    def visitFieldExpression(self, fieldExpression: org.codehaus.groovy.ast.expr.FieldExpression) -> None: ...
    def visitForLoop(self, forStatement: org.codehaus.groovy.ast.stmt.ForStatement) -> None: ...
    def visitGStringExpression(self, gStringExpression: org.codehaus.groovy.ast.expr.GStringExpression) -> None: ...
    def visitIfElse(self, ifStatement: org.codehaus.groovy.ast.stmt.IfStatement) -> None: ...
    def visitImports(self, moduleNode: org.codehaus.groovy.ast.ModuleNode) -> None: ...
    def visitListExpression(self, listExpression: org.codehaus.groovy.ast.expr.ListExpression) -> None: ...
    def visitMapEntryExpression(self, mapEntryExpression: org.codehaus.groovy.ast.expr.MapEntryExpression) -> None: ...
    def visitMapExpression(self, mapExpression: org.codehaus.groovy.ast.expr.MapExpression) -> None: ...
    def visitMethodCallExpression(self, methodCallExpression: org.codehaus.groovy.ast.expr.MethodCallExpression) -> None: ...
    def visitMethodPointerExpression(self, methodPointerExpression: org.codehaus.groovy.ast.expr.MethodPointerExpression) -> None: ...
    def visitNotExpression(self, notExpression: org.codehaus.groovy.ast.expr.NotExpression) -> None: ...
    def visitPackage(self, packageNode: org.codehaus.groovy.ast.PackageNode) -> None: ...
    def visitPostfixExpression(self, postfixExpression: org.codehaus.groovy.ast.expr.PostfixExpression) -> None: ...
    def visitPrefixExpression(self, prefixExpression: org.codehaus.groovy.ast.expr.PrefixExpression) -> None: ...
    def visitProperty(self, propertyNode: org.codehaus.groovy.ast.PropertyNode) -> None: ...
    def visitPropertyExpression(self, propertyExpression: org.codehaus.groovy.ast.expr.PropertyExpression) -> None: ...
    def visitRangeExpression(self, rangeExpression: org.codehaus.groovy.ast.expr.RangeExpression) -> None: ...
    def visitSpreadExpression(self, spreadExpression: org.codehaus.groovy.ast.expr.SpreadExpression) -> None: ...
    def visitSpreadMapExpression(self, spreadMapExpression: org.codehaus.groovy.ast.expr.SpreadMapExpression) -> None: ...
    def visitStaticMethodCallExpression(self, staticMethodCallExpression: org.codehaus.groovy.ast.expr.StaticMethodCallExpression) -> None: ...
    def visitTernaryExpression(self, ternaryExpression: org.codehaus.groovy.ast.expr.TernaryExpression) -> None: ...
    def visitTupleExpression(self, tupleExpression: org.codehaus.groovy.ast.expr.TupleExpression) -> None: ...
    def visitUnaryMinusExpression(self, unaryMinusExpression: org.codehaus.groovy.ast.expr.UnaryMinusExpression) -> None: ...
    def visitUnaryPlusExpression(self, unaryPlusExpression: org.codehaus.groovy.ast.expr.UnaryPlusExpression) -> None: ...
    def visitVariableExpression(self, variableExpression: org.codehaus.groovy.ast.expr.VariableExpression) -> None: ...
    def visitWhileLoop(self, whileStatement: org.codehaus.groovy.ast.stmt.WhileStatement) -> None: ...
    @staticmethod
    def withConstraints(aSTNode: org.codehaus.groovy.ast.ASTNode, closure: groovy.lang.Closure) -> org.codehaus.groovy.ast.ASTNode: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.macro.matcher")``.

    ASTMatcher: typing.Type[ASTMatcher]
    ASTNodePredicate: typing.Type[ASTNodePredicate]
    ContextualClassCodeVisitor: typing.Type[ContextualClassCodeVisitor]
    MatchingConstraints: typing.Type[MatchingConstraints]
    NodeComparator: typing.Type[NodeComparator]
    TreeContext: typing.Type[TreeContext]
    TreeContextAction: typing.Type[TreeContextAction]
    internal: org.codehaus.groovy.macro.matcher.internal.__module_protocol__