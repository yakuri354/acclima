
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import groovyjarjarasm.asm
import java.io
import java.lang
import java.util
import jpype
import org.codehaus.groovy.ast
import org.codehaus.groovy.ast.expr
import org.codehaus.groovy.ast.stmt
import org.codehaus.groovy.classgen
import org.codehaus.groovy.classgen.asm.indy
import org.codehaus.groovy.classgen.asm.sc
import org.codehaus.groovy.classgen.asm.util
import org.codehaus.groovy.control
import org.codehaus.groovy.syntax
import typing



class AssertionWriter:
    def __init__(self, writerController: 'WriterController'): ...
    def disableTracker(self) -> None: ...
    @typing.overload
    def record(self, expression: org.codehaus.groovy.ast.expr.Expression) -> None: ...
    @typing.overload
    def record(self, token: org.codehaus.groovy.syntax.Token) -> None: ...
    def reenableTracker(self) -> None: ...
    def writeAssertStatement(self, assertStatement: org.codehaus.groovy.ast.stmt.AssertStatement) -> None: ...

class BinaryExpressionHelper:
    def __init__(self, writerController: 'WriterController'): ...
    def eval(self, binaryExpression: org.codehaus.groovy.ast.expr.BinaryExpression) -> None: ...
    def evaluateEqual(self, binaryExpression: org.codehaus.groovy.ast.expr.BinaryExpression, boolean: bool) -> None: ...
    def evaluatePostfixMethod(self, postfixExpression: org.codehaus.groovy.ast.expr.PostfixExpression) -> None: ...
    def evaluatePrefixMethod(self, prefixExpression: org.codehaus.groovy.ast.expr.PrefixExpression) -> None: ...
    def evaluateTernary(self, ternaryExpression: org.codehaus.groovy.ast.expr.TernaryExpression) -> None: ...
    def getController(self) -> 'WriterController': ...
    def getIsCaseMethod(self) -> 'MethodCaller': ...

class BinaryExpressionWriter:
    def __init__(self, writerController: 'WriterController', methodCaller: 'MethodCaller', methodCaller2: 'MethodCaller'): ...
    def arrayGet(self, int: int, boolean: bool) -> bool: ...
    def arraySet(self, boolean: bool) -> bool: ...
    def getController(self) -> 'WriterController': ...
    def setArraySetAndGet(self, methodCaller: 'MethodCaller', methodCaller2: 'MethodCaller') -> None: ...
    def write(self, int: int, boolean: bool) -> bool: ...
    def writePostOrPrefixMethod(self, int: int, boolean: bool) -> bool: ...

class BytecodeDumper(org.codehaus.groovy.control.BytecodeProcessor):
    STANDARD_ERR: typing.ClassVar['BytecodeDumper'] = ...
    def __init__(self, writer: java.io.Writer): ...
    def processBytecode(self, string: str, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> typing.MutableSequence[int]: ...

class BytecodeHelper(groovyjarjarasm.asm.Opcodes):
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def box(methodVisitor: groovyjarjarasm.asm.MethodVisitor, class_: typing.Type) -> bool: ...
    @typing.overload
    @staticmethod
    def box(methodVisitor: groovyjarjarasm.asm.MethodVisitor, classNode: org.codehaus.groovy.ast.ClassNode) -> bool: ...
    @staticmethod
    def convertPrimitiveToBoolean(methodVisitor: groovyjarjarasm.asm.MethodVisitor, classNode: org.codehaus.groovy.ast.ClassNode) -> None: ...
    @typing.overload
    @staticmethod
    def doCast(methodVisitor: groovyjarjarasm.asm.MethodVisitor, class_: typing.Type) -> None: ...
    @typing.overload
    @staticmethod
    def doCast(methodVisitor: groovyjarjarasm.asm.MethodVisitor, classNode: org.codehaus.groovy.ast.ClassNode) -> None: ...
    @staticmethod
    def doCastToPrimitive(methodVisitor: groovyjarjarasm.asm.MethodVisitor, classNode: org.codehaus.groovy.ast.ClassNode, classNode2: org.codehaus.groovy.ast.ClassNode) -> None: ...
    @staticmethod
    def doCastToWrappedType(methodVisitor: groovyjarjarasm.asm.MethodVisitor, classNode: org.codehaus.groovy.ast.ClassNode, classNode2: org.codehaus.groovy.ast.ClassNode) -> None: ...
    @staticmethod
    def doReturn(methodVisitor: groovyjarjarasm.asm.MethodVisitor, classNode: org.codehaus.groovy.ast.ClassNode) -> None: ...
    @staticmethod
    def formatNameForClassLoading(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def getClassInternalName(class_: typing.Type) -> str: ...
    @typing.overload
    @staticmethod
    def getClassInternalName(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def getClassInternalName(classNode: org.codehaus.groovy.ast.ClassNode) -> str: ...
    @staticmethod
    def getClassInternalNames(classNodeArray: typing.Union[typing.List[org.codehaus.groovy.ast.ClassNode], jpype.JArray]) -> typing.MutableSequence[str]: ...
    @staticmethod
    def getClassLoadingTypeDescription(classNode: org.codehaus.groovy.ast.ClassNode) -> str: ...
    @staticmethod
    def getGenericsBounds(classNode: org.codehaus.groovy.ast.ClassNode) -> str: ...
    @staticmethod
    def getGenericsMethodSignature(methodNode: org.codehaus.groovy.ast.MethodNode) -> str: ...
    @staticmethod
    def getGenericsSignature(classNode: org.codehaus.groovy.ast.ClassNode) -> str: ...
    @typing.overload
    @staticmethod
    def getMethodDescriptor(class_: typing.Type, classArray: typing.Union[typing.List[typing.Type], jpype.JArray]) -> str: ...
    @typing.overload
    @staticmethod
    def getMethodDescriptor(classNode: org.codehaus.groovy.ast.ClassNode, parameterArray: typing.Union[typing.List[org.codehaus.groovy.ast.Parameter], jpype.JArray]) -> str: ...
    @typing.overload
    @staticmethod
    def getMethodDescriptor(methodNode: org.codehaus.groovy.ast.MethodNode) -> str: ...
    @typing.overload
    @staticmethod
    def getTypeDescription(class_: typing.Type) -> str: ...
    @typing.overload
    @staticmethod
    def getTypeDescription(classNode: org.codehaus.groovy.ast.ClassNode) -> str: ...
    @typing.overload
    def hashCode(self) -> int: ...
    @typing.overload
    @staticmethod
    def hashCode(string: str) -> int: ...
    @staticmethod
    def isClassLiteralPossible(classNode: org.codehaus.groovy.ast.ClassNode) -> bool: ...
    @staticmethod
    def isSameCompilationUnit(classNode: org.codehaus.groovy.ast.ClassNode, classNode2: org.codehaus.groovy.ast.ClassNode) -> bool: ...
    @staticmethod
    def load(methodVisitor: groovyjarjarasm.asm.MethodVisitor, classNode: org.codehaus.groovy.ast.ClassNode, int: int) -> None: ...
    @staticmethod
    def negateBoolean(methodVisitor: groovyjarjarasm.asm.MethodVisitor) -> None: ...
    @staticmethod
    def pushConstant(methodVisitor: groovyjarjarasm.asm.MethodVisitor, int: int) -> None: ...
    @staticmethod
    def store(methodVisitor: groovyjarjarasm.asm.MethodVisitor, classNode: org.codehaus.groovy.ast.ClassNode, int: int) -> None: ...
    @typing.overload
    @staticmethod
    def unbox(methodVisitor: groovyjarjarasm.asm.MethodVisitor, class_: typing.Type) -> None: ...
    @typing.overload
    @staticmethod
    def unbox(methodVisitor: groovyjarjarasm.asm.MethodVisitor, classNode: org.codehaus.groovy.ast.ClassNode) -> None: ...
    @staticmethod
    def visitClassLiteral(methodVisitor: groovyjarjarasm.asm.MethodVisitor, classNode: org.codehaus.groovy.ast.ClassNode) -> None: ...

class BytecodeVariable:
    THIS_VARIABLE: typing.ClassVar['BytecodeVariable'] = ...
    SUPER_VARIABLE: typing.ClassVar['BytecodeVariable'] = ...
    def __init__(self, int: int, classNode: org.codehaus.groovy.ast.ClassNode, string: str, int2: int): ...
    def getEndLabel(self) -> groovyjarjarasm.asm.Label: ...
    def getIndex(self) -> int: ...
    def getName(self) -> str: ...
    def getPrevIndex(self) -> int: ...
    def getStartLabel(self) -> groovyjarjarasm.asm.Label: ...
    def getType(self) -> org.codehaus.groovy.ast.ClassNode: ...
    def isDynamicTyped(self) -> bool: ...
    def isHolder(self) -> bool: ...
    def setDynamicTyped(self, boolean: bool) -> None: ...
    def setEndLabel(self, label: groovyjarjarasm.asm.Label) -> None: ...
    def setHolder(self, boolean: bool) -> None: ...
    def setStartLabel(self, label: groovyjarjarasm.asm.Label) -> None: ...
    def setType(self, classNode: org.codehaus.groovy.ast.ClassNode) -> None: ...
    def toString(self) -> str: ...

class CallSiteWriter:
    CONSTRUCTOR: typing.ClassVar[str] = ...
    def __init__(self, writerController: 'WriterController'): ...
    def fallbackAttributeOrPropertySite(self, propertyExpression: org.codehaus.groovy.ast.expr.PropertyExpression, expression: org.codehaus.groovy.ast.expr.Expression, string: str, methodCallerMultiAdapter: 'MethodCallerMultiAdapter') -> None: ...
    def generateCallSiteArray(self) -> None: ...
    def getCallSites(self) -> java.util.List[str]: ...
    def hasCallSiteUse(self) -> bool: ...
    def makeCallSite(self, expression: org.codehaus.groovy.ast.expr.Expression, string: str, expression2: org.codehaus.groovy.ast.expr.Expression, boolean: bool, boolean2: bool, boolean3: bool, boolean4: bool) -> None: ...
    def makeCallSiteArrayInitializer(self) -> None: ...
    def makeGetPropertySite(self, expression: org.codehaus.groovy.ast.expr.Expression, string: str, boolean: bool, boolean2: bool) -> None: ...
    def makeGroovyObjectGetPropertySite(self, expression: org.codehaus.groovy.ast.expr.Expression, string: str, boolean: bool, boolean2: bool) -> None: ...
    def makeSingleArgumentCall(self, expression: org.codehaus.groovy.ast.expr.Expression, string: str, expression2: org.codehaus.groovy.ast.expr.Expression) -> None: ...
    def makeSiteEntry(self) -> None: ...
    def prepareCallSite(self, string: str) -> None: ...

class ClosureWriter:
    def __init__(self, writerController: 'WriterController'): ...
    def addGeneratedClosureConstructorCall(self, constructorCallExpression: org.codehaus.groovy.ast.expr.ConstructorCallExpression) -> bool: ...
    def getOrAddClosureClass(self, closureExpression: org.codehaus.groovy.ast.expr.ClosureExpression, int: int) -> org.codehaus.groovy.ast.ClassNode: ...
    @staticmethod
    def loadReference(string: str, writerController: 'WriterController') -> None: ...
    def writeClosure(self, closureExpression: org.codehaus.groovy.ast.expr.ClosureExpression) -> None: ...

class CompileStack(groovyjarjarasm.asm.Opcodes):
    def __init__(self, writerController: 'WriterController'): ...
    def addExceptionBlock(self, label: groovyjarjarasm.asm.Label, label2: groovyjarjarasm.asm.Label, label3: groovyjarjarasm.asm.Label, string: str) -> None: ...
    def applyBlockRecorder(self) -> None: ...
    def applyFinallyBlocks(self, label: groovyjarjarasm.asm.Label, boolean: bool) -> None: ...
    def clear(self) -> None: ...
    def containsVariable(self, string: str) -> bool: ...
    def createLocalLabel(self, string: str) -> groovyjarjarasm.asm.Label: ...
    @typing.overload
    def defineTemporaryVariable(self, string: str, boolean: bool) -> int: ...
    @typing.overload
    def defineTemporaryVariable(self, string: str, classNode: org.codehaus.groovy.ast.ClassNode, boolean: bool) -> int: ...
    @typing.overload
    def defineTemporaryVariable(self, variable: org.codehaus.groovy.ast.Variable, boolean: bool) -> int: ...
    @typing.overload
    def defineVariable(self, variable: org.codehaus.groovy.ast.Variable, boolean: bool) -> BytecodeVariable: ...
    @typing.overload
    def defineVariable(self, variable: org.codehaus.groovy.ast.Variable, classNode: org.codehaus.groovy.ast.ClassNode, boolean: bool) -> BytecodeVariable: ...
    def getBreakLabel(self) -> groovyjarjarasm.asm.Label: ...
    def getContinueLabel(self) -> groovyjarjarasm.asm.Label: ...
    def getLabel(self, string: str) -> groovyjarjarasm.asm.Label: ...
    def getNamedBreakLabel(self, string: str) -> groovyjarjarasm.asm.Label: ...
    def getNamedContinueLabel(self, string: str) -> groovyjarjarasm.asm.Label: ...
    def getScope(self) -> org.codehaus.groovy.ast.VariableScope: ...
    @typing.overload
    def getVariable(self, string: str) -> BytecodeVariable: ...
    @typing.overload
    def getVariable(self, string: str, boolean: bool) -> BytecodeVariable: ...
    def hasBlockRecorder(self) -> bool: ...
    def init(self, variableScope: org.codehaus.groovy.ast.VariableScope, parameterArray: typing.Union[typing.List[org.codehaus.groovy.ast.Parameter], jpype.JArray]) -> None: ...
    def isImplicitThis(self) -> bool: ...
    def isInSpecialConstructorCall(self) -> bool: ...
    def isLHS(self) -> bool: ...
    def pop(self) -> None: ...
    def popBlockRecorderVisit(self, blockRecorder: 'CompileStack.BlockRecorder') -> None: ...
    def popImplicitThis(self) -> None: ...
    def popLHS(self) -> None: ...
    def pushBlockRecorder(self, blockRecorder: 'CompileStack.BlockRecorder') -> None: ...
    def pushBlockRecorderVisit(self, blockRecorder: 'CompileStack.BlockRecorder') -> None: ...
    def pushBooleanExpression(self) -> None: ...
    def pushImplicitThis(self, boolean: bool) -> None: ...
    def pushInSpecialConstructorCall(self) -> None: ...
    def pushLHS(self, boolean: bool) -> None: ...
    @typing.overload
    def pushLoop(self, string: str) -> None: ...
    @typing.overload
    def pushLoop(self, list: java.util.List[str]) -> None: ...
    @typing.overload
    def pushLoop(self, variableScope: org.codehaus.groovy.ast.VariableScope, string: str) -> None: ...
    @typing.overload
    def pushLoop(self, variableScope: org.codehaus.groovy.ast.VariableScope, list: java.util.List[str]) -> None: ...
    def pushState(self) -> None: ...
    def pushSwitch(self) -> groovyjarjarasm.asm.Label: ...
    def pushVariableScope(self, variableScope: org.codehaus.groovy.ast.VariableScope) -> None: ...
    def removeVar(self, int: int) -> None: ...
    def writeExceptionTable(self, blockRecorder: 'CompileStack.BlockRecorder', label: groovyjarjarasm.asm.Label, string: str) -> None: ...
    class BlockRecorder:
        excludedStatement: java.lang.Runnable = ...
        ranges: java.util.LinkedList = ...
        @typing.overload
        def __init__(self): ...
        @typing.overload
        def __init__(self, runnable: typing.Union[java.lang.Runnable, typing.Callable]): ...
        def closeRange(self, label: groovyjarjarasm.asm.Label) -> None: ...
        def startRange(self, label: groovyjarjarasm.asm.Label) -> None: ...

class ExpressionAsVariableSlot(org.codehaus.groovy.classgen.BytecodeExpression):
    @typing.overload
    def __init__(self, writerController: 'WriterController', expression: org.codehaus.groovy.ast.expr.Expression): ...
    @typing.overload
    def __init__(self, writerController: 'WriterController', expression: org.codehaus.groovy.ast.expr.Expression, string: str): ...
    def getIndex(self) -> int: ...
    def getText(self) -> str: ...
    @typing.overload
    def visit(self, groovyCodeVisitor: org.codehaus.groovy.ast.GroovyCodeVisitor) -> None: ...
    @typing.overload
    def visit(self, methodVisitor: groovyjarjarasm.asm.MethodVisitor) -> None: ...

class InvocationWriter:
    invokeMethodOnCurrent: typing.ClassVar['MethodCallerMultiAdapter'] = ...
    invokeMethodOnSuper: typing.ClassVar['MethodCallerMultiAdapter'] = ...
    invokeMethod: typing.ClassVar['MethodCallerMultiAdapter'] = ...
    invokeStaticMethod: typing.ClassVar['MethodCallerMultiAdapter'] = ...
    invokeClosureMethod: typing.ClassVar['MethodCaller'] = ...
    castToVargsArray: typing.ClassVar['MethodCaller'] = ...
    def __init__(self, writerController: 'WriterController'): ...
    def castNonPrimitiveToBool(self, classNode: org.codehaus.groovy.ast.ClassNode) -> None: ...
    def castToNonPrimitiveIfNecessary(self, classNode: org.codehaus.groovy.ast.ClassNode, classNode2: org.codehaus.groovy.ast.ClassNode) -> None: ...
    def coerce(self, classNode: org.codehaus.groovy.ast.ClassNode, classNode2: org.codehaus.groovy.ast.ClassNode) -> None: ...
    @staticmethod
    def makeArgumentList(expression: org.codehaus.groovy.ast.expr.Expression) -> org.codehaus.groovy.ast.expr.ArgumentListExpression: ...
    def makeCall(self, expression: org.codehaus.groovy.ast.expr.Expression, expression2: org.codehaus.groovy.ast.expr.Expression, expression3: org.codehaus.groovy.ast.expr.Expression, expression4: org.codehaus.groovy.ast.expr.Expression, methodCallerMultiAdapter: 'MethodCallerMultiAdapter', boolean: bool, boolean2: bool, boolean3: bool) -> None: ...
    def makeSingleArgumentCall(self, expression: org.codehaus.groovy.ast.expr.Expression, string: str, expression2: org.codehaus.groovy.ast.expr.Expression) -> None: ...
    def writeInvokeConstructor(self, constructorCallExpression: org.codehaus.groovy.ast.expr.ConstructorCallExpression) -> None: ...
    def writeInvokeMethod(self, methodCallExpression: org.codehaus.groovy.ast.expr.MethodCallExpression) -> None: ...
    def writeInvokeStaticMethod(self, staticMethodCallExpression: org.codehaus.groovy.ast.expr.StaticMethodCallExpression) -> None: ...
    def writeSpecialConstructorCall(self, constructorCallExpression: org.codehaus.groovy.ast.expr.ConstructorCallExpression) -> None: ...

class MethodCaller(groovyjarjarasm.asm.Opcodes):
    def __init__(self, int: int, class_: typing.Type, string: str): ...
    def call(self, methodVisitor: groovyjarjarasm.asm.MethodVisitor) -> None: ...
    def getMethodDescriptor(self) -> str: ...
    @staticmethod
    def newInterface(class_: typing.Type, string: str) -> 'MethodCaller': ...
    @staticmethod
    def newStatic(class_: typing.Type, string: str) -> 'MethodCaller': ...
    @staticmethod
    def newVirtual(class_: typing.Type, string: str) -> 'MethodCaller': ...

class MethodCallerMultiAdapter:
    MAX_ARGS: typing.ClassVar[int] = ...
    def __init__(self): ...
    def call(self, methodVisitor: groovyjarjarasm.asm.MethodVisitor, int: int, boolean: bool, boolean2: bool) -> None: ...
    @staticmethod
    def newStatic(class_: typing.Type, string: str, boolean: bool, boolean2: bool) -> 'MethodCallerMultiAdapter': ...

class MopWriter:
    FACTORY: typing.ClassVar['MopWriter.Factory'] = ...
    def __init__(self, writerController: 'WriterController'): ...
    def createMopMethods(self) -> None: ...
    @staticmethod
    def equalParameterTypes(parameterArray: typing.Union[typing.List[org.codehaus.groovy.ast.Parameter], jpype.JArray], parameterArray2: typing.Union[typing.List[org.codehaus.groovy.ast.Parameter], jpype.JArray]) -> bool: ...
    @staticmethod
    def getMopMethodName(methodNode: org.codehaus.groovy.ast.MethodNode, boolean: bool) -> str: ...
    @staticmethod
    def isMopMethod(string: str) -> bool: ...
    class Factory:
        def create(self, writerController: 'WriterController') -> 'MopWriter': ...

class OperandStack:
    def __init__(self, writerController: 'WriterController'): ...
    def box(self) -> org.codehaus.groovy.ast.ClassNode: ...
    def castToBool(self, int: int, boolean: bool) -> None: ...
    def doAsType(self, classNode: org.codehaus.groovy.ast.ClassNode) -> None: ...
    @typing.overload
    def doGroovyCast(self, classNode: org.codehaus.groovy.ast.ClassNode) -> None: ...
    @typing.overload
    def doGroovyCast(self, variable: org.codehaus.groovy.ast.Variable) -> None: ...
    def dup(self) -> None: ...
    def getStackLength(self) -> int: ...
    def getTopOperand(self) -> org.codehaus.groovy.ast.ClassNode: ...
    @typing.overload
    def jump(self, int: int) -> groovyjarjarasm.asm.Label: ...
    @typing.overload
    def jump(self, int: int, label: groovyjarjarasm.asm.Label) -> None: ...
    def load(self, classNode: org.codehaus.groovy.ast.ClassNode, int: int) -> None: ...
    def loadOrStoreVariable(self, bytecodeVariable: BytecodeVariable, boolean: bool) -> None: ...
    def pop(self) -> None: ...
    def popDownTo(self, int: int) -> None: ...
    def push(self, classNode: org.codehaus.groovy.ast.ClassNode) -> None: ...
    def pushBool(self, boolean: bool) -> None: ...
    def pushConstant(self, constantExpression: org.codehaus.groovy.ast.expr.ConstantExpression) -> None: ...
    def pushDynamicName(self, expression: org.codehaus.groovy.ast.expr.Expression) -> None: ...
    def remove(self, int: int) -> None: ...
    @typing.overload
    def replace(self, classNode: org.codehaus.groovy.ast.ClassNode) -> None: ...
    @typing.overload
    def replace(self, classNode: org.codehaus.groovy.ast.ClassNode, int: int) -> None: ...
    def storeVar(self, bytecodeVariable: BytecodeVariable) -> None: ...
    def swap(self) -> None: ...
    def toString(self) -> str: ...

class StatementWriter:
    def __init__(self, writerController: 'WriterController'): ...
    def writeAssert(self, assertStatement: org.codehaus.groovy.ast.stmt.AssertStatement) -> None: ...
    def writeBlockStatement(self, blockStatement: org.codehaus.groovy.ast.stmt.BlockStatement) -> None: ...
    def writeBreak(self, breakStatement: org.codehaus.groovy.ast.stmt.BreakStatement) -> None: ...
    def writeContinue(self, continueStatement: org.codehaus.groovy.ast.stmt.ContinueStatement) -> None: ...
    def writeDoWhileLoop(self, doWhileStatement: org.codehaus.groovy.ast.stmt.DoWhileStatement) -> None: ...
    def writeExpressionStatement(self, expressionStatement: org.codehaus.groovy.ast.stmt.ExpressionStatement) -> None: ...
    def writeForStatement(self, forStatement: org.codehaus.groovy.ast.stmt.ForStatement) -> None: ...
    def writeIfElse(self, ifStatement: org.codehaus.groovy.ast.stmt.IfStatement) -> None: ...
    def writeReturn(self, returnStatement: org.codehaus.groovy.ast.stmt.ReturnStatement) -> None: ...
    def writeSwitch(self, switchStatement: org.codehaus.groovy.ast.stmt.SwitchStatement) -> None: ...
    def writeSynchronized(self, synchronizedStatement: org.codehaus.groovy.ast.stmt.SynchronizedStatement) -> None: ...
    def writeThrow(self, throwStatement: org.codehaus.groovy.ast.stmt.ThrowStatement) -> None: ...
    def writeTryCatchFinally(self, tryCatchStatement: org.codehaus.groovy.ast.stmt.TryCatchStatement) -> None: ...
    def writeWhileLoop(self, whileStatement: org.codehaus.groovy.ast.stmt.WhileStatement) -> None: ...

class TypeChooser:
    def resolveType(self, expression: org.codehaus.groovy.ast.expr.Expression, classNode: org.codehaus.groovy.ast.ClassNode) -> org.codehaus.groovy.ast.ClassNode: ...

class UnaryExpressionHelper:
    def __init__(self, writerController: 'WriterController'): ...
    def writeBitwiseNegate(self, bitwiseNegationExpression: org.codehaus.groovy.ast.expr.BitwiseNegationExpression) -> None: ...
    def writeNotExpression(self, notExpression: org.codehaus.groovy.ast.expr.NotExpression) -> None: ...
    def writeUnaryMinus(self, unaryMinusExpression: org.codehaus.groovy.ast.expr.UnaryMinusExpression) -> None: ...
    def writeUnaryPlus(self, unaryPlusExpression: org.codehaus.groovy.ast.expr.UnaryPlusExpression) -> None: ...

class VariableSlotLoader(org.codehaus.groovy.classgen.BytecodeExpression):
    @typing.overload
    def __init__(self, int: int, operandStack: OperandStack): ...
    @typing.overload
    def __init__(self, classNode: org.codehaus.groovy.ast.ClassNode, int: int, operandStack: OperandStack): ...
    def getIndex(self) -> int: ...
    @typing.overload
    def visit(self, groovyCodeVisitor: org.codehaus.groovy.ast.GroovyCodeVisitor) -> None: ...
    @typing.overload
    def visit(self, methodVisitor: groovyjarjarasm.asm.MethodVisitor) -> None: ...

class WriterController:
    optimizeForInt: bool = ...
    def __init__(self): ...
    def getAcg(self) -> org.codehaus.groovy.classgen.AsmClassGenerator: ...
    def getAssertionWriter(self) -> AssertionWriter: ...
    def getBinaryExpressionHelper(self) -> BinaryExpressionHelper: ...
    def getBytecodeVersion(self) -> int: ...
    def getCallSiteWriter(self) -> CallSiteWriter: ...
    def getClassName(self) -> str: ...
    def getClassNode(self) -> org.codehaus.groovy.ast.ClassNode: ...
    def getClassVisitor(self) -> groovyjarjarasm.asm.ClassVisitor: ...
    def getClosureWriter(self) -> ClosureWriter: ...
    def getCompileStack(self) -> CompileStack: ...
    def getConstructorNode(self) -> org.codehaus.groovy.ast.ConstructorNode: ...
    def getContext(self) -> org.codehaus.groovy.classgen.GeneratorContext: ...
    def getCv(self) -> groovyjarjarasm.asm.ClassVisitor: ...
    def getInterfaceClassLoadingClass(self) -> org.codehaus.groovy.ast.InterfaceHelperClassNode: ...
    def getInternalBaseClassName(self) -> str: ...
    def getInternalClassName(self) -> str: ...
    def getInvocationWriter(self) -> InvocationWriter: ...
    def getLineNumber(self) -> int: ...
    def getMethodNode(self) -> org.codehaus.groovy.ast.MethodNode: ...
    def getMethodVisitor(self) -> groovyjarjarasm.asm.MethodVisitor: ...
    def getNextHelperMethodIndex(self) -> int: ...
    def getOperandStack(self) -> OperandStack: ...
    def getOutermostClass(self) -> org.codehaus.groovy.ast.ClassNode: ...
    def getReturnType(self) -> org.codehaus.groovy.ast.ClassNode: ...
    def getSourceUnit(self) -> org.codehaus.groovy.control.SourceUnit: ...
    def getStatementWriter(self) -> StatementWriter: ...
    def getSuperMethodNames(self) -> java.util.List[str]: ...
    def getTypeChooser(self) -> TypeChooser: ...
    def getUnaryExpressionHelper(self) -> UnaryExpressionHelper: ...
    def init(self, asmClassGenerator: org.codehaus.groovy.classgen.AsmClassGenerator, generatorContext: org.codehaus.groovy.classgen.GeneratorContext, classVisitor: groovyjarjarasm.asm.ClassVisitor, classNode: org.codehaus.groovy.ast.ClassNode) -> None: ...
    def isConstructor(self) -> bool: ...
    def isFastPath(self) -> bool: ...
    def isInClosure(self) -> bool: ...
    def isInClosureConstructor(self) -> bool: ...
    def isInScriptBody(self) -> bool: ...
    def isNotClinit(self) -> bool: ...
    def isNotExplicitThisInClosure(self, boolean: bool) -> bool: ...
    def isStaticConstructor(self) -> bool: ...
    def isStaticContext(self) -> bool: ...
    def isStaticMethod(self) -> bool: ...
    def resetLineNumber(self) -> None: ...
    def setConstructorNode(self, constructorNode: org.codehaus.groovy.ast.ConstructorNode) -> None: ...
    def setInterfaceClassLoadingClass(self, interfaceHelperClassNode: org.codehaus.groovy.ast.InterfaceHelperClassNode) -> None: ...
    def setLineNumber(self, int: int) -> None: ...
    def setMethodNode(self, methodNode: org.codehaus.groovy.ast.MethodNode) -> None: ...
    def setMethodVisitor(self, methodVisitor: groovyjarjarasm.asm.MethodVisitor) -> None: ...
    def shouldOptimizeForInt(self) -> bool: ...
    def switchToFastPath(self) -> None: ...
    def switchToSlowPath(self) -> None: ...

class WriterControllerFactory:
    def makeController(self, writerController: WriterController) -> WriterController: ...

class BinaryExpressionMultiTypeDispatcher(BinaryExpressionHelper):
    typeMap: typing.ClassVar[java.util.Map] = ...
    typeMapKeyNames: typing.ClassVar[typing.MutableSequence[str]] = ...
    def __init__(self, writerController: WriterController): ...

class BinaryFloatExpressionHelper(BinaryExpressionWriter):
    def __init__(self, writerController: WriterController): ...

class BinaryIntExpressionHelper(BinaryExpressionWriter):
    @typing.overload
    def __init__(self, writerController: WriterController): ...
    @typing.overload
    def __init__(self, writerController: WriterController, methodCaller: MethodCaller, methodCaller2: MethodCaller): ...

class BinaryLongExpressionHelper(BinaryExpressionWriter):
    @typing.overload
    def __init__(self, writerController: WriterController): ...
    @typing.overload
    def __init__(self, writerController: WriterController, methodCaller: MethodCaller, methodCaller2: MethodCaller): ...

class BinaryObjectExpressionHelper(BinaryExpressionWriter):
    def __init__(self, writerController: WriterController): ...
    def write(self, int: int, boolean: bool) -> bool: ...
    def writePostOrPrefixMethod(self, int: int, boolean: bool) -> bool: ...

class DelegatingController(WriterController):
    def __init__(self, writerController: WriterController): ...
    def getAcg(self) -> org.codehaus.groovy.classgen.AsmClassGenerator: ...
    def getAssertionWriter(self) -> AssertionWriter: ...
    def getBinaryExpressionHelper(self) -> BinaryExpressionHelper: ...
    def getBytecodeVersion(self) -> int: ...
    def getCallSiteWriter(self) -> CallSiteWriter: ...
    def getClassName(self) -> str: ...
    def getClassNode(self) -> org.codehaus.groovy.ast.ClassNode: ...
    def getClassVisitor(self) -> groovyjarjarasm.asm.ClassVisitor: ...
    def getClosureWriter(self) -> ClosureWriter: ...
    def getCompileStack(self) -> CompileStack: ...
    def getConstructorNode(self) -> org.codehaus.groovy.ast.ConstructorNode: ...
    def getContext(self) -> org.codehaus.groovy.classgen.GeneratorContext: ...
    def getCv(self) -> groovyjarjarasm.asm.ClassVisitor: ...
    def getInterfaceClassLoadingClass(self) -> org.codehaus.groovy.ast.InterfaceHelperClassNode: ...
    def getInternalBaseClassName(self) -> str: ...
    def getInternalClassName(self) -> str: ...
    def getInvocationWriter(self) -> InvocationWriter: ...
    def getLineNumber(self) -> int: ...
    def getMethodNode(self) -> org.codehaus.groovy.ast.MethodNode: ...
    def getMethodVisitor(self) -> groovyjarjarasm.asm.MethodVisitor: ...
    def getOperandStack(self) -> OperandStack: ...
    def getOutermostClass(self) -> org.codehaus.groovy.ast.ClassNode: ...
    def getReturnType(self) -> org.codehaus.groovy.ast.ClassNode: ...
    def getSourceUnit(self) -> org.codehaus.groovy.control.SourceUnit: ...
    def getStatementWriter(self) -> StatementWriter: ...
    def getTypeChooser(self) -> TypeChooser: ...
    def getUnaryExpressionHelper(self) -> UnaryExpressionHelper: ...
    def init(self, asmClassGenerator: org.codehaus.groovy.classgen.AsmClassGenerator, generatorContext: org.codehaus.groovy.classgen.GeneratorContext, classVisitor: groovyjarjarasm.asm.ClassVisitor, classNode: org.codehaus.groovy.ast.ClassNode) -> None: ...
    def isConstructor(self) -> bool: ...
    def isFastPath(self) -> bool: ...
    def isInClosure(self) -> bool: ...
    def isInClosureConstructor(self) -> bool: ...
    def isInScriptBody(self) -> bool: ...
    def isNotClinit(self) -> bool: ...
    def isNotExplicitThisInClosure(self, boolean: bool) -> bool: ...
    def isStaticConstructor(self) -> bool: ...
    def isStaticContext(self) -> bool: ...
    def isStaticMethod(self) -> bool: ...
    def resetLineNumber(self) -> None: ...
    def setConstructorNode(self, constructorNode: org.codehaus.groovy.ast.ConstructorNode) -> None: ...
    def setInterfaceClassLoadingClass(self, interfaceHelperClassNode: org.codehaus.groovy.ast.InterfaceHelperClassNode) -> None: ...
    def setLineNumber(self, int: int) -> None: ...
    def setMethodNode(self, methodNode: org.codehaus.groovy.ast.MethodNode) -> None: ...
    def setMethodVisitor(self, methodVisitor: groovyjarjarasm.asm.MethodVisitor) -> None: ...
    def shouldOptimizeForInt(self) -> bool: ...
    def switchToFastPath(self) -> None: ...
    def switchToSlowPath(self) -> None: ...

class OptimizingStatementWriter(StatementWriter):
    def __init__(self, writerController: WriterController): ...
    @staticmethod
    def setNodeMeta(typeChooser: TypeChooser, classNode: org.codehaus.groovy.ast.ClassNode) -> None: ...
    def writeBlockStatement(self, blockStatement: org.codehaus.groovy.ast.stmt.BlockStatement) -> None: ...
    def writeDoWhileLoop(self, doWhileStatement: org.codehaus.groovy.ast.stmt.DoWhileStatement) -> None: ...
    def writeExpressionStatement(self, expressionStatement: org.codehaus.groovy.ast.stmt.ExpressionStatement) -> None: ...
    def writeIfElse(self, ifStatement: org.codehaus.groovy.ast.stmt.IfStatement) -> None: ...
    def writeReturn(self, returnStatement: org.codehaus.groovy.ast.stmt.ReturnStatement) -> None: ...
    def writeWhileLoop(self, whileStatement: org.codehaus.groovy.ast.stmt.WhileStatement) -> None: ...
    class ClassNodeSkip:
        def __init__(self): ...
    class StatementMeta:
        def __init__(self): ...
        def chainInvolvedTypes(self, optimizeFlagsCollector: 'OptimizingStatementWriter.OptimizeFlagsCollector') -> None: ...
        def toString(self) -> str: ...
    class OptimizeFlagsCollector: ...

class StatementMetaTypeChooser(TypeChooser):
    def __init__(self): ...
    def resolveType(self, expression: org.codehaus.groovy.ast.expr.Expression, classNode: org.codehaus.groovy.ast.ClassNode) -> org.codehaus.groovy.ast.ClassNode: ...

class BinaryBooleanExpressionHelper(BinaryIntExpressionHelper):
    def __init__(self, writerController: WriterController): ...
    def writePostOrPrefixMethod(self, int: int, boolean: bool) -> bool: ...

class BinaryDoubleExpressionHelper(BinaryLongExpressionHelper):
    def __init__(self, writerController: WriterController): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.classgen.asm")``.

    AssertionWriter: typing.Type[AssertionWriter]
    BinaryBooleanExpressionHelper: typing.Type[BinaryBooleanExpressionHelper]
    BinaryDoubleExpressionHelper: typing.Type[BinaryDoubleExpressionHelper]
    BinaryExpressionHelper: typing.Type[BinaryExpressionHelper]
    BinaryExpressionMultiTypeDispatcher: typing.Type[BinaryExpressionMultiTypeDispatcher]
    BinaryExpressionWriter: typing.Type[BinaryExpressionWriter]
    BinaryFloatExpressionHelper: typing.Type[BinaryFloatExpressionHelper]
    BinaryIntExpressionHelper: typing.Type[BinaryIntExpressionHelper]
    BinaryLongExpressionHelper: typing.Type[BinaryLongExpressionHelper]
    BinaryObjectExpressionHelper: typing.Type[BinaryObjectExpressionHelper]
    BytecodeDumper: typing.Type[BytecodeDumper]
    BytecodeHelper: typing.Type[BytecodeHelper]
    BytecodeVariable: typing.Type[BytecodeVariable]
    CallSiteWriter: typing.Type[CallSiteWriter]
    ClosureWriter: typing.Type[ClosureWriter]
    CompileStack: typing.Type[CompileStack]
    DelegatingController: typing.Type[DelegatingController]
    ExpressionAsVariableSlot: typing.Type[ExpressionAsVariableSlot]
    InvocationWriter: typing.Type[InvocationWriter]
    MethodCaller: typing.Type[MethodCaller]
    MethodCallerMultiAdapter: typing.Type[MethodCallerMultiAdapter]
    MopWriter: typing.Type[MopWriter]
    OperandStack: typing.Type[OperandStack]
    OptimizingStatementWriter: typing.Type[OptimizingStatementWriter]
    StatementMetaTypeChooser: typing.Type[StatementMetaTypeChooser]
    StatementWriter: typing.Type[StatementWriter]
    TypeChooser: typing.Type[TypeChooser]
    UnaryExpressionHelper: typing.Type[UnaryExpressionHelper]
    VariableSlotLoader: typing.Type[VariableSlotLoader]
    WriterController: typing.Type[WriterController]
    WriterControllerFactory: typing.Type[WriterControllerFactory]
    indy: org.codehaus.groovy.classgen.asm.indy.__module_protocol__
    sc: org.codehaus.groovy.classgen.asm.sc.__module_protocol__
    util: org.codehaus.groovy.classgen.asm.util.__module_protocol__
