
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import groovy.util
import java.io
import jpype
import jpype.protocol
import org.w3c.dom
import typing



class DomToGroovy:
    @typing.overload
    def __init__(self, indentPrinter: groovy.util.IndentPrinter): ...
    @typing.overload
    def __init__(self, printWriter: java.io.PrintWriter): ...
    @staticmethod
    def main(stringArray: typing.Union[typing.List[str], jpype.JArray]) -> None: ...
    @typing.overload
    @staticmethod
    def parse(file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> org.w3c.dom.Document: ...
    @typing.overload
    @staticmethod
    def parse(inputStream: java.io.InputStream) -> org.w3c.dom.Document: ...
    @typing.overload
    @staticmethod
    def parse(reader: java.io.Reader) -> org.w3c.dom.Document: ...
    def print_(self, document: org.w3c.dom.Document) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.tools.xml")``.

    DomToGroovy: typing.Type[DomToGroovy]
