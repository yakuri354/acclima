
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.net
import jpype
import jpype.protocol
import org.codehaus.groovy.control
import typing



class NullWriter(java.io.Writer):
    DEFAULT: typing.ClassVar['NullWriter'] = ...
    def __init__(self): ...
    def close(self) -> None: ...
    def flush(self) -> None: ...
    @typing.overload
    def write(self, charArray: typing.Union[typing.List[str], jpype.JArray]) -> None: ...
    @typing.overload
    def write(self, int: int) -> None: ...
    @typing.overload
    def write(self, string: str) -> None: ...
    @typing.overload
    def write(self, string: str, int: int, int2: int) -> None: ...
    @typing.overload
    def write(self, charArray: typing.Union[typing.List[str], jpype.JArray], int: int, int2: int) -> None: ...

class ReaderSource(org.codehaus.groovy.control.HasCleanup):
    def canReopenSource(self) -> bool: ...
    def cleanup(self) -> None: ...
    def getLine(self, int: int, janitor: org.codehaus.groovy.control.Janitor) -> str: ...
    def getReader(self) -> java.io.Reader: ...
    def getURI(self) -> java.net.URI: ...

class AbstractReaderSource(ReaderSource):
    def __init__(self, compilerConfiguration: org.codehaus.groovy.control.CompilerConfiguration): ...
    def canReopenSource(self) -> bool: ...
    def cleanup(self) -> None: ...
    def getLine(self, int: int, janitor: org.codehaus.groovy.control.Janitor) -> str: ...

class FileReaderSource(AbstractReaderSource):
    def __init__(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath], compilerConfiguration: org.codehaus.groovy.control.CompilerConfiguration): ...
    def getFile(self) -> java.io.File: ...
    def getReader(self) -> java.io.Reader: ...
    def getURI(self) -> java.net.URI: ...

class InputStreamReaderSource(AbstractReaderSource):
    def __init__(self, inputStream: java.io.InputStream, compilerConfiguration: org.codehaus.groovy.control.CompilerConfiguration): ...
    def canReopenSource(self) -> bool: ...
    def getReader(self) -> java.io.Reader: ...
    def getURI(self) -> java.net.URI: ...

class StringReaderSource(AbstractReaderSource):
    def __init__(self, string: str, compilerConfiguration: org.codehaus.groovy.control.CompilerConfiguration): ...
    def getReader(self) -> java.io.Reader: ...
    def getURI(self) -> java.net.URI: ...

class URLReaderSource(AbstractReaderSource):
    def __init__(self, uRL: java.net.URL, compilerConfiguration: org.codehaus.groovy.control.CompilerConfiguration): ...
    def getReader(self) -> java.io.Reader: ...
    def getURI(self) -> java.net.URI: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.control.io")``.

    AbstractReaderSource: typing.Type[AbstractReaderSource]
    FileReaderSource: typing.Type[FileReaderSource]
    InputStreamReaderSource: typing.Type[InputStreamReaderSource]
    NullWriter: typing.Type[NullWriter]
    ReaderSource: typing.Type[ReaderSource]
    StringReaderSource: typing.Type[StringReaderSource]
    URLReaderSource: typing.Type[URLReaderSource]
