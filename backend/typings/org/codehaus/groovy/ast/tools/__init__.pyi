
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import groovy.lang
import java.util
import jpype
import org.codehaus.groovy.ast
import org.codehaus.groovy.ast.expr
import org.codehaus.groovy.ast.stmt
import org.codehaus.groovy.control
import org.codehaus.groovy.control.io
import org.codehaus.groovy.syntax
import typing



class BeanUtils:
    def __init__(self): ...
    @staticmethod
    def addPseudoProperties(classNode: org.codehaus.groovy.ast.ClassNode, classNode2: org.codehaus.groovy.ast.ClassNode, list: java.util.List[org.codehaus.groovy.ast.PropertyNode], set: java.util.Set[str], boolean: bool, boolean2: bool, boolean3: bool) -> None: ...
    @typing.overload
    @staticmethod
    def getAllProperties(classNode: org.codehaus.groovy.ast.ClassNode, boolean: bool, boolean2: bool, boolean3: bool) -> java.util.List[org.codehaus.groovy.ast.PropertyNode]: ...
    @typing.overload
    @staticmethod
    def getAllProperties(classNode: org.codehaus.groovy.ast.ClassNode, boolean: bool, boolean2: bool, boolean3: bool, boolean4: bool, boolean5: bool) -> java.util.List[org.codehaus.groovy.ast.PropertyNode]: ...

class ClassNodeUtils:
    def __init__(self): ...
    @staticmethod
    def addDeclaredMethodMapsFromSuperInterfaces(classNode: org.codehaus.groovy.ast.ClassNode, map: typing.Union[java.util.Map[str, org.codehaus.groovy.ast.MethodNode], typing.Mapping[str, org.codehaus.groovy.ast.MethodNode]]) -> None: ...
    @staticmethod
    def addInterfaceMethods(classNode: org.codehaus.groovy.ast.ClassNode, map: typing.Union[java.util.Map[str, org.codehaus.groovy.ast.MethodNode], typing.Mapping[str, org.codehaus.groovy.ast.MethodNode]]) -> None: ...
    @staticmethod
    def getDeclaredMethodMapsFromInterfaces(classNode: org.codehaus.groovy.ast.ClassNode) -> java.util.Map[str, org.codehaus.groovy.ast.MethodNode]: ...
    @staticmethod
    def getPropNameForAccessor(string: str) -> str: ...
    @staticmethod
    def getStaticProperty(classNode: org.codehaus.groovy.ast.ClassNode, string: str) -> org.codehaus.groovy.ast.PropertyNode: ...
    @staticmethod
    def hasPossibleStaticMethod(classNode: org.codehaus.groovy.ast.ClassNode, string: str, expression: org.codehaus.groovy.ast.expr.Expression, boolean: bool) -> bool: ...
    @staticmethod
    def hasPossibleStaticProperty(classNode: org.codehaus.groovy.ast.ClassNode, string: str) -> bool: ...
    @staticmethod
    def hasStaticProperty(classNode: org.codehaus.groovy.ast.ClassNode, string: str) -> bool: ...
    @staticmethod
    def isInnerClass(classNode: org.codehaus.groovy.ast.ClassNode) -> bool: ...
    @staticmethod
    def isValidAccessorName(string: str) -> bool: ...

class ClosureUtils:
    def __init__(self): ...
    @staticmethod
    def convertClosureToSource(readerSource: org.codehaus.groovy.control.io.ReaderSource, closureExpression: org.codehaus.groovy.ast.expr.ClosureExpression) -> str: ...
    @staticmethod
    def hasSingleCharacterArg(closure: groovy.lang.Closure) -> bool: ...
    @staticmethod
    def hasSingleStringArg(closure: groovy.lang.Closure) -> bool: ...

class GeneralUtils:
    ASSIGN: typing.ClassVar[org.codehaus.groovy.syntax.Token] = ...
    EQ: typing.ClassVar[org.codehaus.groovy.syntax.Token] = ...
    NE: typing.ClassVar[org.codehaus.groovy.syntax.Token] = ...
    LT: typing.ClassVar[org.codehaus.groovy.syntax.Token] = ...
    AND: typing.ClassVar[org.codehaus.groovy.syntax.Token] = ...
    OR: typing.ClassVar[org.codehaus.groovy.syntax.Token] = ...
    CMP: typing.ClassVar[org.codehaus.groovy.syntax.Token] = ...
    def __init__(self): ...
    @staticmethod
    def andX(expression: org.codehaus.groovy.ast.expr.Expression, expression2: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.BinaryExpression: ...
    @typing.overload
    @staticmethod
    def args(*string: str) -> org.codehaus.groovy.ast.expr.ArgumentListExpression: ...
    @typing.overload
    @staticmethod
    def args(list: java.util.List[org.codehaus.groovy.ast.expr.Expression]) -> org.codehaus.groovy.ast.expr.ArgumentListExpression: ...
    @typing.overload
    @staticmethod
    def args(parameterArray: typing.Union[typing.List[org.codehaus.groovy.ast.Parameter], jpype.JArray]) -> org.codehaus.groovy.ast.expr.ArgumentListExpression: ...
    @typing.overload
    @staticmethod
    def args(*expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.ArgumentListExpression: ...
    @staticmethod
    def assignS(expression: org.codehaus.groovy.ast.expr.Expression, expression2: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.stmt.Statement: ...
    @staticmethod
    def assignX(expression: org.codehaus.groovy.ast.expr.Expression, expression2: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.Expression: ...
    @staticmethod
    def attrX(expression: org.codehaus.groovy.ast.expr.Expression, expression2: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.Expression: ...
    @staticmethod
    def binX(expression: org.codehaus.groovy.ast.expr.Expression, token: org.codehaus.groovy.syntax.Token, expression2: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.BinaryExpression: ...
    @typing.overload
    @staticmethod
    def block(variableScope: org.codehaus.groovy.ast.VariableScope, list: java.util.List[org.codehaus.groovy.ast.stmt.Statement]) -> org.codehaus.groovy.ast.stmt.BlockStatement: ...
    @typing.overload
    @staticmethod
    def block(variableScope: org.codehaus.groovy.ast.VariableScope, *statement: org.codehaus.groovy.ast.stmt.Statement) -> org.codehaus.groovy.ast.stmt.BlockStatement: ...
    @typing.overload
    @staticmethod
    def block(*statement: org.codehaus.groovy.ast.stmt.Statement) -> org.codehaus.groovy.ast.stmt.BlockStatement: ...
    @staticmethod
    def boolX(expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.BooleanExpression: ...
    @typing.overload
    @staticmethod
    def callSuperX(string: str) -> org.codehaus.groovy.ast.expr.MethodCallExpression: ...
    @typing.overload
    @staticmethod
    def callSuperX(string: str, expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.MethodCallExpression: ...
    @typing.overload
    @staticmethod
    def callThisX(string: str) -> org.codehaus.groovy.ast.expr.MethodCallExpression: ...
    @typing.overload
    @staticmethod
    def callThisX(string: str, expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.MethodCallExpression: ...
    @typing.overload
    @staticmethod
    def callX(expression: org.codehaus.groovy.ast.expr.Expression, string: str) -> org.codehaus.groovy.ast.expr.MethodCallExpression: ...
    @typing.overload
    @staticmethod
    def callX(expression: org.codehaus.groovy.ast.expr.Expression, string: str, expression2: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.MethodCallExpression: ...
    @typing.overload
    @staticmethod
    def callX(expression: org.codehaus.groovy.ast.expr.Expression, expression2: org.codehaus.groovy.ast.expr.Expression, expression3: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.MethodCallExpression: ...
    @typing.overload
    @staticmethod
    def callX(classNode: org.codehaus.groovy.ast.ClassNode, string: str) -> org.codehaus.groovy.ast.expr.StaticMethodCallExpression: ...
    @typing.overload
    @staticmethod
    def callX(classNode: org.codehaus.groovy.ast.ClassNode, string: str, expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.StaticMethodCallExpression: ...
    @typing.overload
    @staticmethod
    def castX(classNode: org.codehaus.groovy.ast.ClassNode, expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.CastExpression: ...
    @typing.overload
    @staticmethod
    def castX(classNode: org.codehaus.groovy.ast.ClassNode, expression: org.codehaus.groovy.ast.expr.Expression, boolean: bool) -> org.codehaus.groovy.ast.expr.CastExpression: ...
    @staticmethod
    def catchS(parameter: org.codehaus.groovy.ast.Parameter, statement: org.codehaus.groovy.ast.stmt.Statement) -> org.codehaus.groovy.ast.stmt.CatchStatement: ...
    @staticmethod
    def classList2args(list: java.util.List[str]) -> org.codehaus.groovy.ast.expr.ListExpression: ...
    @typing.overload
    @staticmethod
    def classX(class_: typing.Type) -> org.codehaus.groovy.ast.expr.ClassExpression: ...
    @typing.overload
    @staticmethod
    def classX(classNode: org.codehaus.groovy.ast.ClassNode) -> org.codehaus.groovy.ast.expr.ClassExpression: ...
    @staticmethod
    def cloneParams(parameterArray: typing.Union[typing.List[org.codehaus.groovy.ast.Parameter], jpype.JArray]) -> typing.MutableSequence[org.codehaus.groovy.ast.Parameter]: ...
    @typing.overload
    @staticmethod
    def closureX(parameterArray: typing.Union[typing.List[org.codehaus.groovy.ast.Parameter], jpype.JArray], statement: org.codehaus.groovy.ast.stmt.Statement) -> org.codehaus.groovy.ast.expr.ClosureExpression: ...
    @typing.overload
    @staticmethod
    def closureX(statement: org.codehaus.groovy.ast.stmt.Statement) -> org.codehaus.groovy.ast.expr.ClosureExpression: ...
    @staticmethod
    def cmpX(expression: org.codehaus.groovy.ast.expr.Expression, expression2: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.BinaryExpression: ...
    @typing.overload
    @staticmethod
    def constX(object: typing.Any) -> org.codehaus.groovy.ast.expr.ConstantExpression: ...
    @typing.overload
    @staticmethod
    def constX(object: typing.Any, boolean: bool) -> org.codehaus.groovy.ast.expr.ConstantExpression: ...
    @staticmethod
    def convertASTToSource(readerSource: org.codehaus.groovy.control.io.ReaderSource, aSTNode: org.codehaus.groovy.ast.ASTNode) -> str: ...
    @staticmethod
    def copyAnnotatedNodeAnnotations(annotatedNode: org.codehaus.groovy.ast.AnnotatedNode, list: java.util.List[org.codehaus.groovy.ast.AnnotationNode], list2: java.util.List[org.codehaus.groovy.ast.AnnotationNode]) -> None: ...
    @staticmethod
    def copyStatementsWithSuperAdjustment(closureExpression: org.codehaus.groovy.ast.expr.ClosureExpression, blockStatement: org.codehaus.groovy.ast.stmt.BlockStatement) -> bool: ...
    @staticmethod
    def createConstructorStatementDefault(fieldNode: org.codehaus.groovy.ast.FieldNode) -> org.codehaus.groovy.ast.stmt.Statement: ...
    @typing.overload
    @staticmethod
    def ctorSuperS() -> org.codehaus.groovy.ast.stmt.Statement: ...
    @typing.overload
    @staticmethod
    def ctorSuperS(expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.stmt.Statement: ...
    @typing.overload
    @staticmethod
    def ctorThisS() -> org.codehaus.groovy.ast.stmt.Statement: ...
    @typing.overload
    @staticmethod
    def ctorThisS(expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.stmt.Statement: ...
    @typing.overload
    @staticmethod
    def ctorX(classNode: org.codehaus.groovy.ast.ClassNode) -> org.codehaus.groovy.ast.expr.ConstructorCallExpression: ...
    @typing.overload
    @staticmethod
    def ctorX(classNode: org.codehaus.groovy.ast.ClassNode, expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.ConstructorCallExpression: ...
    @staticmethod
    def declS(expression: org.codehaus.groovy.ast.expr.Expression, expression2: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.stmt.Statement: ...
    @staticmethod
    def entryX(expression: org.codehaus.groovy.ast.expr.Expression, expression2: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.MapEntryExpression: ...
    @staticmethod
    def eqX(expression: org.codehaus.groovy.ast.expr.Expression, expression2: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.BinaryExpression: ...
    @staticmethod
    def equalsNullX(expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.BooleanExpression: ...
    @typing.overload
    @staticmethod
    def fieldX(classNode: org.codehaus.groovy.ast.ClassNode, string: str) -> org.codehaus.groovy.ast.expr.FieldExpression: ...
    @typing.overload
    @staticmethod
    def fieldX(fieldNode: org.codehaus.groovy.ast.FieldNode) -> org.codehaus.groovy.ast.expr.FieldExpression: ...
    @staticmethod
    def findArg(string: str) -> org.codehaus.groovy.ast.expr.Expression: ...
    @staticmethod
    def getAllMethods(classNode: org.codehaus.groovy.ast.ClassNode) -> java.util.List[org.codehaus.groovy.ast.MethodNode]: ...
    @typing.overload
    @staticmethod
    def getAllProperties(set: java.util.Set[str], classNode: org.codehaus.groovy.ast.ClassNode, boolean: bool, boolean2: bool, boolean3: bool, boolean4: bool, boolean5: bool, boolean6: bool) -> java.util.List[org.codehaus.groovy.ast.PropertyNode]: ...
    @typing.overload
    @staticmethod
    def getAllProperties(set: java.util.Set[str], classNode: org.codehaus.groovy.ast.ClassNode, classNode2: org.codehaus.groovy.ast.ClassNode, boolean: bool, boolean2: bool, boolean3: bool, boolean4: bool, boolean5: bool, boolean6: bool) -> java.util.List[org.codehaus.groovy.ast.PropertyNode]: ...
    @typing.overload
    @staticmethod
    def getAllProperties(set: java.util.Set[str], classNode: org.codehaus.groovy.ast.ClassNode, classNode2: org.codehaus.groovy.ast.ClassNode, boolean: bool, boolean2: bool, boolean3: bool, boolean4: bool, boolean5: bool, boolean6: bool, boolean7: bool, boolean8: bool, boolean9: bool) -> java.util.List[org.codehaus.groovy.ast.PropertyNode]: ...
    @typing.overload
    @staticmethod
    def getAllProperties(classNode: org.codehaus.groovy.ast.ClassNode) -> java.util.List[org.codehaus.groovy.ast.PropertyNode]: ...
    @staticmethod
    def getGetterName(propertyNode: org.codehaus.groovy.ast.PropertyNode) -> str: ...
    @staticmethod
    def getInstanceNonPropertyFieldNames(classNode: org.codehaus.groovy.ast.ClassNode) -> java.util.List[str]: ...
    @staticmethod
    def getInstanceNonPropertyFields(classNode: org.codehaus.groovy.ast.ClassNode) -> java.util.List[org.codehaus.groovy.ast.FieldNode]: ...
    @staticmethod
    def getInstanceProperties(classNode: org.codehaus.groovy.ast.ClassNode) -> java.util.List[org.codehaus.groovy.ast.PropertyNode]: ...
    @staticmethod
    def getInstancePropertyFields(classNode: org.codehaus.groovy.ast.ClassNode) -> java.util.List[org.codehaus.groovy.ast.FieldNode]: ...
    @staticmethod
    def getInstancePropertyNames(classNode: org.codehaus.groovy.ast.ClassNode) -> java.util.List[str]: ...
    @staticmethod
    def getInterfacesAndSuperInterfaces(classNode: org.codehaus.groovy.ast.ClassNode) -> java.util.Set[org.codehaus.groovy.ast.ClassNode]: ...
    @staticmethod
    def getSetterName(string: str) -> str: ...
    @staticmethod
    def getSuperNonPropertyFields(classNode: org.codehaus.groovy.ast.ClassNode) -> java.util.List[org.codehaus.groovy.ast.FieldNode]: ...
    @staticmethod
    def getSuperPropertyFields(classNode: org.codehaus.groovy.ast.ClassNode) -> java.util.List[org.codehaus.groovy.ast.FieldNode]: ...
    @staticmethod
    def getterThisX(classNode: org.codehaus.groovy.ast.ClassNode, propertyNode: org.codehaus.groovy.ast.PropertyNode) -> org.codehaus.groovy.ast.expr.Expression: ...
    @staticmethod
    def getterX(classNode: org.codehaus.groovy.ast.ClassNode, expression: org.codehaus.groovy.ast.expr.Expression, propertyNode: org.codehaus.groovy.ast.PropertyNode) -> org.codehaus.groovy.ast.expr.Expression: ...
    @staticmethod
    def hasClassX(expression: org.codehaus.groovy.ast.expr.Expression, classNode: org.codehaus.groovy.ast.ClassNode) -> org.codehaus.groovy.ast.expr.BinaryExpression: ...
    @staticmethod
    def hasDeclaredMethod(classNode: org.codehaus.groovy.ast.ClassNode, string: str, int: int) -> bool: ...
    @staticmethod
    def hasEqualFieldX(fieldNode: org.codehaus.groovy.ast.FieldNode, expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.BinaryExpression: ...
    @typing.overload
    @staticmethod
    def hasEqualPropertyX(classNode: org.codehaus.groovy.ast.ClassNode, propertyNode: org.codehaus.groovy.ast.PropertyNode, variableExpression: org.codehaus.groovy.ast.expr.VariableExpression) -> org.codehaus.groovy.ast.expr.BinaryExpression: ...
    @typing.overload
    @staticmethod
    def hasEqualPropertyX(propertyNode: org.codehaus.groovy.ast.PropertyNode, expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.BinaryExpression: ...
    @staticmethod
    def hasSameFieldX(fieldNode: org.codehaus.groovy.ast.FieldNode, expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.BooleanExpression: ...
    @staticmethod
    def hasSamePropertyX(propertyNode: org.codehaus.groovy.ast.PropertyNode, expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.BooleanExpression: ...
    @staticmethod
    def ifElseS(expression: org.codehaus.groovy.ast.expr.Expression, statement: org.codehaus.groovy.ast.stmt.Statement, statement2: org.codehaus.groovy.ast.stmt.Statement) -> org.codehaus.groovy.ast.stmt.Statement: ...
    @typing.overload
    @staticmethod
    def ifS(expression: org.codehaus.groovy.ast.expr.Expression, expression2: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.stmt.Statement: ...
    @typing.overload
    @staticmethod
    def ifS(expression: org.codehaus.groovy.ast.expr.Expression, statement: org.codehaus.groovy.ast.stmt.Statement) -> org.codehaus.groovy.ast.stmt.Statement: ...
    @typing.overload
    @staticmethod
    def inSamePackage(class_: typing.Type, class2: typing.Type) -> bool: ...
    @typing.overload
    @staticmethod
    def inSamePackage(classNode: org.codehaus.groovy.ast.ClassNode, classNode2: org.codehaus.groovy.ast.ClassNode) -> bool: ...
    @staticmethod
    def indexX(expression: org.codehaus.groovy.ast.expr.Expression, expression2: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.Expression: ...
    @staticmethod
    def isDefaultVisibility(int: int) -> bool: ...
    @staticmethod
    def isInstanceOfX(expression: org.codehaus.groovy.ast.expr.Expression, classNode: org.codehaus.groovy.ast.ClassNode) -> org.codehaus.groovy.ast.expr.BooleanExpression: ...
    @staticmethod
    def isOneX(expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.BooleanExpression: ...
    @staticmethod
    def isOrImplements(classNode: org.codehaus.groovy.ast.ClassNode, classNode2: org.codehaus.groovy.ast.ClassNode) -> bool: ...
    @staticmethod
    def isTrueX(expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.BooleanExpression: ...
    @staticmethod
    def isZeroX(expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.BooleanExpression: ...
    @staticmethod
    def list2args(list: java.util.List) -> org.codehaus.groovy.ast.expr.ListExpression: ...
    @staticmethod
    def listX(list: java.util.List[org.codehaus.groovy.ast.expr.Expression]) -> org.codehaus.groovy.ast.expr.ListExpression: ...
    @staticmethod
    def localVarX(string: str) -> org.codehaus.groovy.ast.expr.VariableExpression: ...
    @staticmethod
    def ltX(expression: org.codehaus.groovy.ast.expr.Expression, expression2: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.BinaryExpression: ...
    @staticmethod
    def makeDescriptorWithoutReturnType(methodNode: org.codehaus.groovy.ast.MethodNode) -> str: ...
    @staticmethod
    def mapX(list: java.util.List[org.codehaus.groovy.ast.expr.MapEntryExpression]) -> org.codehaus.groovy.ast.expr.MapExpression: ...
    @staticmethod
    def neX(expression: org.codehaus.groovy.ast.expr.Expression, expression2: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.BinaryExpression: ...
    @staticmethod
    def notNullX(expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.BooleanExpression: ...
    @staticmethod
    def notX(expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.NotExpression: ...
    @staticmethod
    def orX(expression: org.codehaus.groovy.ast.expr.Expression, expression2: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.BinaryExpression: ...
    @typing.overload
    @staticmethod
    def param(classNode: org.codehaus.groovy.ast.ClassNode, string: str) -> org.codehaus.groovy.ast.Parameter: ...
    @typing.overload
    @staticmethod
    def param(classNode: org.codehaus.groovy.ast.ClassNode, string: str, expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.Parameter: ...
    @staticmethod
    def params(*parameter: org.codehaus.groovy.ast.Parameter) -> typing.MutableSequence[org.codehaus.groovy.ast.Parameter]: ...
    @staticmethod
    def plusX(expression: org.codehaus.groovy.ast.expr.Expression, expression2: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.BinaryExpression: ...
    @typing.overload
    @staticmethod
    def propX(expression: org.codehaus.groovy.ast.expr.Expression, string: str) -> org.codehaus.groovy.ast.expr.Expression: ...
    @typing.overload
    @staticmethod
    def propX(expression: org.codehaus.groovy.ast.expr.Expression, expression2: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.Expression: ...
    @staticmethod
    def returnS(expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.stmt.Statement: ...
    @staticmethod
    def safeExpression(expression: org.codehaus.groovy.ast.expr.Expression, expression2: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.stmt.Statement: ...
    @staticmethod
    def sameX(expression: org.codehaus.groovy.ast.expr.Expression, expression2: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.BooleanExpression: ...
    @staticmethod
    def stmt(expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.stmt.Statement: ...
    @staticmethod
    def ternaryX(expression: org.codehaus.groovy.ast.expr.Expression, expression2: org.codehaus.groovy.ast.expr.Expression, expression3: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.TernaryExpression: ...
    @staticmethod
    def throwS(expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.stmt.ThrowStatement: ...
    @typing.overload
    @staticmethod
    def varX(string: str) -> org.codehaus.groovy.ast.expr.VariableExpression: ...
    @typing.overload
    @staticmethod
    def varX(string: str, classNode: org.codehaus.groovy.ast.ClassNode) -> org.codehaus.groovy.ast.expr.VariableExpression: ...
    @typing.overload
    @staticmethod
    def varX(variable: org.codehaus.groovy.ast.Variable) -> org.codehaus.groovy.ast.expr.VariableExpression: ...

class GenericsUtils:
    EMPTY_GENERICS_ARRAY: typing.ClassVar[typing.MutableSequence[org.codehaus.groovy.ast.GenericsType]] = ...
    JAVA_LANG_OBJECT: typing.ClassVar[str] = ...
    def __init__(self): ...
    @staticmethod
    def addMethodGenerics(methodNode: org.codehaus.groovy.ast.MethodNode, map: typing.Union[java.util.Map[str, org.codehaus.groovy.ast.ClassNode], typing.Mapping[str, org.codehaus.groovy.ast.ClassNode]]) -> java.util.Map[str, org.codehaus.groovy.ast.ClassNode]: ...
    @staticmethod
    def alignGenericTypes(genericsTypeArray: typing.Union[typing.List[org.codehaus.groovy.ast.GenericsType], jpype.JArray], genericsTypeArray2: typing.Union[typing.List[org.codehaus.groovy.ast.GenericsType], jpype.JArray], genericsTypeArray3: typing.Union[typing.List[org.codehaus.groovy.ast.GenericsType], jpype.JArray]) -> typing.MutableSequence[org.codehaus.groovy.ast.GenericsType]: ...
    @staticmethod
    def applyGenericsContextToPlaceHolders(map: typing.Union[java.util.Map[str, org.codehaus.groovy.ast.ClassNode], typing.Mapping[str, org.codehaus.groovy.ast.ClassNode]], genericsTypeArray: typing.Union[typing.List[org.codehaus.groovy.ast.GenericsType], jpype.JArray]) -> typing.MutableSequence[org.codehaus.groovy.ast.GenericsType]: ...
    @staticmethod
    def buildWildcardType(*classNode: org.codehaus.groovy.ast.ClassNode) -> org.codehaus.groovy.ast.GenericsType: ...
    @staticmethod
    def clearParameterizedTypeCache() -> None: ...
    @typing.overload
    @staticmethod
    def correctToGenericsSpec(map: typing.Union[java.util.Map[str, org.codehaus.groovy.ast.ClassNode], typing.Mapping[str, org.codehaus.groovy.ast.ClassNode]], classNode: org.codehaus.groovy.ast.ClassNode) -> org.codehaus.groovy.ast.ClassNode: ...
    @typing.overload
    @staticmethod
    def correctToGenericsSpec(map: typing.Union[java.util.Map[str, org.codehaus.groovy.ast.ClassNode], typing.Mapping[str, org.codehaus.groovy.ast.ClassNode]], genericsType: org.codehaus.groovy.ast.GenericsType) -> org.codehaus.groovy.ast.ClassNode: ...
    @typing.overload
    @staticmethod
    def correctToGenericsSpec(map: typing.Union[java.util.Map[str, org.codehaus.groovy.ast.ClassNode], typing.Mapping[str, org.codehaus.groovy.ast.ClassNode]], methodNode: org.codehaus.groovy.ast.MethodNode) -> org.codehaus.groovy.ast.MethodNode: ...
    @typing.overload
    @staticmethod
    def correctToGenericsSpecRecurse(map: typing.Union[java.util.Map[str, org.codehaus.groovy.ast.ClassNode], typing.Mapping[str, org.codehaus.groovy.ast.ClassNode]], classNode: org.codehaus.groovy.ast.ClassNode) -> org.codehaus.groovy.ast.ClassNode: ...
    @typing.overload
    @staticmethod
    def correctToGenericsSpecRecurse(map: typing.Union[java.util.Map[str, org.codehaus.groovy.ast.ClassNode], typing.Mapping[str, org.codehaus.groovy.ast.ClassNode]], classNode: org.codehaus.groovy.ast.ClassNode, list: java.util.List[str]) -> org.codehaus.groovy.ast.ClassNode: ...
    @typing.overload
    @staticmethod
    def correctToGenericsSpecRecurse(map: typing.Union[java.util.Map[str, org.codehaus.groovy.ast.ClassNode], typing.Mapping[str, org.codehaus.groovy.ast.ClassNode]], classNodeArray: typing.Union[typing.List[org.codehaus.groovy.ast.ClassNode], jpype.JArray]) -> typing.MutableSequence[org.codehaus.groovy.ast.ClassNode]: ...
    @typing.overload
    @staticmethod
    def createGenericsSpec(classNode: org.codehaus.groovy.ast.ClassNode) -> java.util.Map[str, org.codehaus.groovy.ast.ClassNode]: ...
    @typing.overload
    @staticmethod
    def createGenericsSpec(classNode: org.codehaus.groovy.ast.ClassNode, map: typing.Union[java.util.Map[str, org.codehaus.groovy.ast.ClassNode], typing.Mapping[str, org.codehaus.groovy.ast.ClassNode]]) -> java.util.Map[str, org.codehaus.groovy.ast.ClassNode]: ...
    @typing.overload
    @staticmethod
    def extractPlaceholders(classNode: org.codehaus.groovy.ast.ClassNode) -> java.util.Map[org.codehaus.groovy.ast.GenericsType.GenericsTypeName, org.codehaus.groovy.ast.GenericsType]: ...
    @typing.overload
    @staticmethod
    def extractPlaceholders(classNode: org.codehaus.groovy.ast.ClassNode, map: typing.Union[java.util.Map[org.codehaus.groovy.ast.GenericsType.GenericsTypeName, org.codehaus.groovy.ast.GenericsType], typing.Mapping[org.codehaus.groovy.ast.GenericsType.GenericsTypeName, org.codehaus.groovy.ast.GenericsType]]) -> None: ...
    @staticmethod
    def extractSuperClassGenerics(classNode: org.codehaus.groovy.ast.ClassNode, classNode2: org.codehaus.groovy.ast.ClassNode, map: typing.Union[java.util.Map[str, org.codehaus.groovy.ast.ClassNode], typing.Mapping[str, org.codehaus.groovy.ast.ClassNode]]) -> None: ...
    @staticmethod
    def findActualTypeByGenericsPlaceholderName(string: str, map: typing.Union[java.util.Map[org.codehaus.groovy.ast.GenericsType, org.codehaus.groovy.ast.GenericsType], typing.Mapping[org.codehaus.groovy.ast.GenericsType, org.codehaus.groovy.ast.GenericsType]]) -> org.codehaus.groovy.ast.ClassNode: ...
    @staticmethod
    def findParameterizedType(classNode: org.codehaus.groovy.ast.ClassNode, classNode2: org.codehaus.groovy.ast.ClassNode) -> org.codehaus.groovy.ast.ClassNode: ...
    @staticmethod
    def findParameterizedTypeFromCache(classNode: org.codehaus.groovy.ast.ClassNode, classNode2: org.codehaus.groovy.ast.ClassNode) -> org.codehaus.groovy.ast.ClassNode: ...
    @staticmethod
    def getSuperClass(classNode: org.codehaus.groovy.ast.ClassNode, classNode2: org.codehaus.groovy.ast.ClassNode) -> org.codehaus.groovy.ast.ClassNode: ...
    @staticmethod
    def makeClassSafe(class_: typing.Type) -> org.codehaus.groovy.ast.ClassNode: ...
    @staticmethod
    def makeClassSafe0(classNode: org.codehaus.groovy.ast.ClassNode, *genericsType: org.codehaus.groovy.ast.GenericsType) -> org.codehaus.groovy.ast.ClassNode: ...
    @typing.overload
    @staticmethod
    def makeClassSafeWithGenerics(class_: typing.Type, classNode: org.codehaus.groovy.ast.ClassNode) -> org.codehaus.groovy.ast.ClassNode: ...
    @typing.overload
    @staticmethod
    def makeClassSafeWithGenerics(classNode: org.codehaus.groovy.ast.ClassNode, *genericsType: org.codehaus.groovy.ast.GenericsType) -> org.codehaus.groovy.ast.ClassNode: ...
    @staticmethod
    def makeDeclaringAndActualGenericsTypeMap(classNode: org.codehaus.groovy.ast.ClassNode, classNode2: org.codehaus.groovy.ast.ClassNode) -> java.util.Map[org.codehaus.groovy.ast.GenericsType, org.codehaus.groovy.ast.GenericsType]: ...
    @staticmethod
    def newClass(classNode: org.codehaus.groovy.ast.ClassNode) -> org.codehaus.groovy.ast.ClassNode: ...
    @staticmethod
    def nonGeneric(classNode: org.codehaus.groovy.ast.ClassNode) -> org.codehaus.groovy.ast.ClassNode: ...
    @staticmethod
    def parameterizeInterfaceGenerics(classNode: org.codehaus.groovy.ast.ClassNode, classNode2: org.codehaus.groovy.ast.ClassNode) -> org.codehaus.groovy.ast.ClassNode: ...
    @staticmethod
    def parameterizeType(classNode: org.codehaus.groovy.ast.ClassNode, classNode2: org.codehaus.groovy.ast.ClassNode) -> org.codehaus.groovy.ast.ClassNode: ...
    @staticmethod
    def parseClassNodesFromString(string: str, sourceUnit: org.codehaus.groovy.control.SourceUnit, compilationUnit: org.codehaus.groovy.control.CompilationUnit, methodNode: org.codehaus.groovy.ast.MethodNode, aSTNode: org.codehaus.groovy.ast.ASTNode) -> typing.MutableSequence[org.codehaus.groovy.ast.ClassNode]: ...
    @staticmethod
    def toGenericTypesString(genericsTypeArray: typing.Union[typing.List[org.codehaus.groovy.ast.GenericsType], jpype.JArray]) -> str: ...

class ParameterUtils:
    def __init__(self): ...
    @staticmethod
    def parametersEqual(parameterArray: typing.Union[typing.List[org.codehaus.groovy.ast.Parameter], jpype.JArray], parameterArray2: typing.Union[typing.List[org.codehaus.groovy.ast.Parameter], jpype.JArray]) -> bool: ...

class PropertyNodeUtils:
    def __init__(self): ...
    @staticmethod
    def adjustPropertyModifiersForMethod(propertyNode: org.codehaus.groovy.ast.PropertyNode) -> int: ...

class WideningCategories:
    def __init__(self): ...
    @staticmethod
    def implementsInterfaceOrSubclassOf(classNode: org.codehaus.groovy.ast.ClassNode, classNode2: org.codehaus.groovy.ast.ClassNode) -> bool: ...
    @staticmethod
    def isBigDecCategory(classNode: org.codehaus.groovy.ast.ClassNode) -> bool: ...
    @staticmethod
    def isBigIntCategory(classNode: org.codehaus.groovy.ast.ClassNode) -> bool: ...
    @staticmethod
    def isDouble(classNode: org.codehaus.groovy.ast.ClassNode) -> bool: ...
    @staticmethod
    def isDoubleCategory(classNode: org.codehaus.groovy.ast.ClassNode) -> bool: ...
    @staticmethod
    def isFloat(classNode: org.codehaus.groovy.ast.ClassNode) -> bool: ...
    @staticmethod
    def isFloatingCategory(classNode: org.codehaus.groovy.ast.ClassNode) -> bool: ...
    @staticmethod
    def isInt(classNode: org.codehaus.groovy.ast.ClassNode) -> bool: ...
    @staticmethod
    def isIntCategory(classNode: org.codehaus.groovy.ast.ClassNode) -> bool: ...
    @staticmethod
    def isLongCategory(classNode: org.codehaus.groovy.ast.ClassNode) -> bool: ...
    @staticmethod
    def isNumberCategory(classNode: org.codehaus.groovy.ast.ClassNode) -> bool: ...
    @typing.overload
    @staticmethod
    def lowestUpperBound(list: java.util.List[org.codehaus.groovy.ast.ClassNode]) -> org.codehaus.groovy.ast.ClassNode: ...
    @typing.overload
    @staticmethod
    def lowestUpperBound(classNode: org.codehaus.groovy.ast.ClassNode, classNode2: org.codehaus.groovy.ast.ClassNode) -> org.codehaus.groovy.ast.ClassNode: ...
    class LowestUpperBoundClassNode(org.codehaus.groovy.ast.ClassNode):
        def __init__(self, string: str, classNode: org.codehaus.groovy.ast.ClassNode, *classNode2: org.codehaus.groovy.ast.ClassNode): ...
        def getLubName(self) -> str: ...
        def getName(self) -> str: ...
        def getPlainNodeReference(self) -> org.codehaus.groovy.ast.ClassNode: ...
        def getText(self) -> str: ...
        def getTypeClass(self) -> typing.Type: ...
        def hashCode(self) -> int: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.ast.tools")``.

    BeanUtils: typing.Type[BeanUtils]
    ClassNodeUtils: typing.Type[ClassNodeUtils]
    ClosureUtils: typing.Type[ClosureUtils]
    GeneralUtils: typing.Type[GeneralUtils]
    GenericsUtils: typing.Type[GenericsUtils]
    ParameterUtils: typing.Type[ParameterUtils]
    PropertyNodeUtils: typing.Type[PropertyNodeUtils]
    WideningCategories: typing.Type[WideningCategories]