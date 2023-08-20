
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.codehaus.groovy.classgen.asm
import org.codehaus.groovy.classgen.asm.sc
import typing



class IndyStaticTypesMultiTypeDispatcher(org.codehaus.groovy.classgen.asm.sc.StaticTypesBinaryExpressionMultiTypeDispatcher):
    def __init__(self, writerController: org.codehaus.groovy.classgen.asm.WriterController): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.classgen.asm.indy.sc")``.

    IndyStaticTypesMultiTypeDispatcher: typing.Type[IndyStaticTypesMultiTypeDispatcher]
