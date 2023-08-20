
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import groovyjarjarasm.asm
import groovyjarjarasm.asm.util
import jpype
import org.codehaus.groovy.ast
import typing



class LoggableClassVisitor(groovyjarjarasm.asm.ClassVisitor):
    def __init__(self, classVisitor: groovyjarjarasm.asm.ClassVisitor): ...

class LoggableTextifier(groovyjarjarasm.asm.util.Textifier):
    def __init__(self): ...
    @typing.overload
    def visit(self, int: int, int2: int, string: str, string2: str, string3: str, stringArray: typing.Union[typing.List[str], jpype.JArray]) -> None: ...
    @typing.overload
    def visit(self, string: str, object: typing.Any) -> None: ...
    @typing.overload
    def visitAnnotation(self, string: str, boolean: bool) -> groovyjarjarasm.asm.util.Textifier: ...
    @typing.overload
    def visitAnnotation(self, string: str, string2: str) -> groovyjarjarasm.asm.util.Textifier: ...
    def visitAnnotationDefault(self) -> groovyjarjarasm.asm.util.Textifier: ...
    def visitAnnotationEnd(self) -> None: ...
    def visitArray(self, string: str) -> groovyjarjarasm.asm.util.Textifier: ...
    def visitAttribute(self, attribute: groovyjarjarasm.asm.Attribute) -> None: ...
    def visitClassAnnotation(self, string: str, boolean: bool) -> groovyjarjarasm.asm.util.Textifier: ...
    def visitClassAttribute(self, attribute: groovyjarjarasm.asm.Attribute) -> None: ...
    def visitClassEnd(self) -> None: ...
    def visitClassTypeAnnotation(self, int: int, typePath: groovyjarjarasm.asm.TypePath, string: str, boolean: bool) -> groovyjarjarasm.asm.util.Printer: ...
    def visitCode(self) -> None: ...
    def visitEnum(self, string: str, string2: str, string3: str) -> None: ...
    def visitExport(self, string: str, int: int, *string2: str) -> None: ...
    def visitField(self, int: int, string: str, string2: str, string3: str, object: typing.Any) -> groovyjarjarasm.asm.util.Textifier: ...
    def visitFieldAnnotation(self, string: str, boolean: bool) -> groovyjarjarasm.asm.util.Textifier: ...
    def visitFieldAttribute(self, attribute: groovyjarjarasm.asm.Attribute) -> None: ...
    def visitFieldEnd(self) -> None: ...
    def visitFieldInsn(self, int: int, string: str, string2: str, string3: str) -> None: ...
    def visitFieldTypeAnnotation(self, int: int, typePath: groovyjarjarasm.asm.TypePath, string: str, boolean: bool) -> groovyjarjarasm.asm.util.Printer: ...
    def visitFrame(self, int: int, int2: int, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray], int3: int, objectArray2: typing.Union[typing.List[typing.Any], jpype.JArray]) -> None: ...
    def visitIincInsn(self, int: int, int2: int) -> None: ...
    def visitInnerClass(self, string: str, string2: str, string3: str, int: int) -> None: ...
    def visitInsn(self, int: int) -> None: ...
    def visitInsnAnnotation(self, int: int, typePath: groovyjarjarasm.asm.TypePath, string: str, boolean: bool) -> groovyjarjarasm.asm.util.Printer: ...
    def visitIntInsn(self, int: int, int2: int) -> None: ...
    def visitInvokeDynamicInsn(self, string: str, string2: str, handle: groovyjarjarasm.asm.Handle, *object: typing.Any) -> None: ...
    def visitJumpInsn(self, int: int, label: groovyjarjarasm.asm.Label) -> None: ...
    def visitLabel(self, label: groovyjarjarasm.asm.Label) -> None: ...
    def visitLdcInsn(self, object: typing.Any) -> None: ...
    def visitLineNumber(self, int: int, label: groovyjarjarasm.asm.Label) -> None: ...
    def visitLocalVariable(self, string: str, string2: str, string3: str, label: groovyjarjarasm.asm.Label, label2: groovyjarjarasm.asm.Label, int: int) -> None: ...
    def visitLocalVariableAnnotation(self, int: int, typePath: groovyjarjarasm.asm.TypePath, labelArray: typing.Union[typing.List[groovyjarjarasm.asm.Label], jpype.JArray], labelArray2: typing.Union[typing.List[groovyjarjarasm.asm.Label], jpype.JArray], intArray: typing.Union[typing.List[int], jpype.JArray], string: str, boolean: bool) -> groovyjarjarasm.asm.util.Printer: ...
    def visitLookupSwitchInsn(self, label: groovyjarjarasm.asm.Label, intArray: typing.Union[typing.List[int], jpype.JArray], labelArray: typing.Union[typing.List[groovyjarjarasm.asm.Label], jpype.JArray]) -> None: ...
    def visitMaxs(self, int: int, int2: int) -> None: ...
    def visitMethod(self, int: int, string: str, string2: str, string3: str, stringArray: typing.Union[typing.List[str], jpype.JArray]) -> groovyjarjarasm.asm.util.Textifier: ...
    def visitMethodAnnotation(self, string: str, boolean: bool) -> groovyjarjarasm.asm.util.Textifier: ...
    def visitMethodAttribute(self, attribute: groovyjarjarasm.asm.Attribute) -> None: ...
    def visitMethodEnd(self) -> None: ...
    @typing.overload
    def visitMethodInsn(self, int: int, string: str, string2: str, string3: str) -> None: ...
    @typing.overload
    def visitMethodInsn(self, int: int, string: str, string2: str, string3: str, boolean: bool) -> None: ...
    def visitMethodTypeAnnotation(self, int: int, typePath: groovyjarjarasm.asm.TypePath, string: str, boolean: bool) -> groovyjarjarasm.asm.util.Printer: ...
    def visitModule(self, string: str, int: int, string2: str) -> groovyjarjarasm.asm.util.Printer: ...
    def visitModuleEnd(self) -> None: ...
    def visitMultiANewArrayInsn(self, string: str, int: int) -> None: ...
    def visitOuterClass(self, string: str, string2: str, string3: str) -> None: ...
    def visitParameter(self, string: str, int: int) -> None: ...
    def visitParameterAnnotation(self, int: int, string: str, boolean: bool) -> groovyjarjarasm.asm.util.Textifier: ...
    def visitProvide(self, string: str, *string2: str) -> None: ...
    def visitRequire(self, string: str, int: int, string2: str) -> None: ...
    def visitSource(self, string: str, string2: str) -> None: ...
    def visitTableSwitchInsn(self, int: int, int2: int, label: groovyjarjarasm.asm.Label, *label2: groovyjarjarasm.asm.Label) -> None: ...
    def visitTryCatchAnnotation(self, int: int, typePath: groovyjarjarasm.asm.TypePath, string: str, boolean: bool) -> groovyjarjarasm.asm.util.Printer: ...
    def visitTryCatchBlock(self, label: groovyjarjarasm.asm.Label, label2: groovyjarjarasm.asm.Label, label3: groovyjarjarasm.asm.Label, string: str) -> None: ...
    def visitTypeAnnotation(self, int: int, typePath: groovyjarjarasm.asm.TypePath, string: str, boolean: bool) -> groovyjarjarasm.asm.util.Textifier: ...
    def visitTypeInsn(self, int: int, string: str) -> None: ...
    def visitUse(self, string: str) -> None: ...
    def visitVarInsn(self, int: int, int2: int) -> None: ...

class TypeUtil:
    def __init__(self): ...
    @staticmethod
    def autoboxType(class_: typing.Type) -> typing.Type: ...
    @staticmethod
    def getDescriptionByName(string: str) -> str: ...
    @staticmethod
    def getDescriptionByType(classNode: org.codehaus.groovy.ast.ClassNode) -> str: ...
    @staticmethod
    def getLoadInsnByType(type: groovyjarjarasm.asm.Type) -> int: ...
    @staticmethod
    def getReturnInsnByType(type: groovyjarjarasm.asm.Type) -> int: ...
    @staticmethod
    def getWrappedClassDescriptor(type: groovyjarjarasm.asm.Type) -> str: ...
    @typing.overload
    @staticmethod
    def isPrimitiveType(type: groovyjarjarasm.asm.Type) -> bool: ...
    @typing.overload
    @staticmethod
    def isPrimitiveType(string: str) -> bool: ...
    @typing.overload
    @staticmethod
    def isPrimitiveType(classNode: org.codehaus.groovy.ast.ClassNode) -> bool: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.classgen.asm.util")``.

    LoggableClassVisitor: typing.Type[LoggableClassVisitor]
    LoggableTextifier: typing.Type[LoggableTextifier]
    TypeUtil: typing.Type[TypeUtil]
