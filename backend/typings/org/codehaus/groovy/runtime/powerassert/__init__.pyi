
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import org.codehaus.groovy.ast.stmt
import org.codehaus.groovy.control
import typing



class AssertionRenderer:
    @staticmethod
    def render(string: str, valueRecorder: 'ValueRecorder') -> str: ...

class PowerAssertionError(java.lang.AssertionError):
    def __init__(self, string: str): ...
    def toString(self) -> str: ...

class SourceText:
    def __init__(self, assertStatement: org.codehaus.groovy.ast.stmt.AssertStatement, sourceUnit: org.codehaus.groovy.control.SourceUnit, janitor: org.codehaus.groovy.control.Janitor): ...
    def getNormalizedColumn(self, int: int, int2: int) -> int: ...
    def getNormalizedText(self) -> str: ...

class SourceTextNotAvailableException(java.lang.RuntimeException):
    def __init__(self, assertStatement: org.codehaus.groovy.ast.stmt.AssertStatement, sourceUnit: org.codehaus.groovy.control.SourceUnit, string: str): ...

class Value:
    def __init__(self, object: typing.Any, int: int): ...
    def getColumn(self) -> int: ...
    def getValue(self) -> typing.Any: ...

class ValueRecorder:
    def __init__(self): ...
    def clear(self) -> None: ...
    def getValues(self) -> java.util.List[Value]: ...
    def record(self, object: typing.Any, int: int) -> typing.Any: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.runtime.powerassert")``.

    AssertionRenderer: typing.Type[AssertionRenderer]
    PowerAssertionError: typing.Type[PowerAssertionError]
    SourceText: typing.Type[SourceText]
    SourceTextNotAvailableException: typing.Type[SourceTextNotAvailableException]
    Value: typing.Type[Value]
    ValueRecorder: typing.Type[ValueRecorder]
