
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import groovy.lang
import java.lang
import java.net
import java.util
import jline.console.completer
import org.codehaus.groovy.runtime
import org.codehaus.groovy.tools.shell
import org.codehaus.groovy.tools.shell.util
import typing



class AliasCommand(org.codehaus.groovy.tools.shell.CommandSupport):
    COMMAND_NAME: typing.ClassVar[str] = ...
    def __init__(self, groovysh: org.codehaus.groovy.tools.shell.Groovysh): ...
    def execute(self, list: java.util.List[str]) -> typing.Any: ...

class AliasTargetProxyCommand(org.codehaus.groovy.tools.shell.CommandSupport, org.codehaus.groovy.tools.shell.Command):
    def __init__(self, groovysh: org.codehaus.groovy.tools.shell.Groovysh, string: str, list: java.util.List): ...
    def execute(self, list: java.util.List[str]) -> typing.Any: ...
    def getArgs(self) -> java.util.List[str]: ...
    def getDescription(self) -> str: ...
    def getHelp(self) -> str: ...
    def getUsage(self) -> str: ...

class ClearCommand(org.codehaus.groovy.tools.shell.CommandSupport):
    COMMAND_NAME: typing.ClassVar[str] = ...
    def __init__(self, groovysh: org.codehaus.groovy.tools.shell.Groovysh): ...
    def execute(self, list: java.util.List[str]) -> typing.Any: ...

class DisplayCommand(org.codehaus.groovy.tools.shell.CommandSupport):
    COMMAND_NAME: typing.ClassVar[str] = ...
    def __init__(self, groovysh: org.codehaus.groovy.tools.shell.Groovysh): ...
    def execute(self, list: java.util.List[str]) -> typing.Any: ...

class DocCommand(org.codehaus.groovy.tools.shell.CommandSupport):
    COMMAND_NAME: typing.ClassVar[str] = ...
    def __init__(self, groovysh: org.codehaus.groovy.tools.shell.Groovysh): ...
    def doc(self, string: str) -> None: ...
    def execute(self, list: java.util.List[str]) -> typing.Any: ...

class EditCommand(org.codehaus.groovy.tools.shell.CommandSupport):
    COMMAND_NAME: typing.ClassVar[str] = ...
    def __init__(self, groovysh: org.codehaus.groovy.tools.shell.Groovysh): ...
    def execute(self, list: java.util.List[str]) -> typing.Any: ...
    def getEditorProcessBuilder(self, string: str, string2: str) -> java.lang.ProcessBuilder: ...
    def replaceCurrentBuffer(self, list: java.util.List[str]) -> None: ...

class ExitCommand(org.codehaus.groovy.tools.shell.CommandSupport):
    COMMAND_NAME: typing.ClassVar[str] = ...
    def __init__(self, groovysh: org.codehaus.groovy.tools.shell.Groovysh): ...
    def execute(self, list: java.util.List[str]) -> typing.Any: ...

class GrabCommand(org.codehaus.groovy.tools.shell.CommandSupport):
    COMMAND_NAME: typing.ClassVar[str] = ...
    def __init__(self, groovysh: org.codehaus.groovy.tools.shell.Groovysh): ...
    def execute(self, list: java.util.List[str]) -> typing.Any: ...

class HelpCommand(org.codehaus.groovy.tools.shell.CommandSupport):
    COMMAND_NAME: typing.ClassVar[str] = ...
    def __init__(self, groovysh: org.codehaus.groovy.tools.shell.Groovysh): ...
    def execute(self, list: java.util.List[str]) -> typing.Any: ...

class HistoryCommand(org.codehaus.groovy.tools.shell.ComplexCommandSupport):
    COMMAND_NAME: typing.ClassVar[str] = ...
    def __init__(self, groovysh: org.codehaus.groovy.tools.shell.Groovysh): ...
    def execute(self, list: java.util.List[str]) -> typing.Any: ...
    def getDo_clear(self) -> typing.Any: ...
    def getDo_flush(self) -> typing.Any: ...
    def getDo_recall(self) -> typing.Any: ...
    def getDo_show(self) -> typing.Any: ...
    def setDo_clear(self, object: typing.Any) -> None: ...
    def setDo_flush(self, object: typing.Any) -> None: ...
    def setDo_recall(self, object: typing.Any) -> None: ...
    def setDo_show(self, object: typing.Any) -> None: ...
    class _closure1(groovy.lang.Closure, org.codehaus.groovy.runtime.GeneratedClosure):
        def __init__(self, object: typing.Any, object2: typing.Any): ...
        @typing.overload
        def doCall(self) -> typing.Any: ...
        @typing.overload
        def doCall(self, object: typing.Any) -> typing.Any: ...
    class _closure2(groovy.lang.Closure, org.codehaus.groovy.runtime.GeneratedClosure):
        def __init__(self, object: typing.Any, object2: typing.Any): ...
        @typing.overload
        def doCall(self) -> typing.Any: ...
        @typing.overload
        def doCall(self, object: typing.Any) -> typing.Any: ...
    class _closure3(groovy.lang.Closure, org.codehaus.groovy.runtime.GeneratedClosure):
        def __init__(self, object: typing.Any, object2: typing.Any): ...
        @typing.overload
        def doCall(self) -> typing.Any: ...
        @typing.overload
        def doCall(self, object: typing.Any) -> typing.Any: ...
    class _closure4(groovy.lang.Closure, org.codehaus.groovy.runtime.GeneratedClosure):
        def __init__(self, object: typing.Any, object2: typing.Any): ...
        def doCall(self, object: typing.Any) -> typing.Any: ...

class ImportCommand(org.codehaus.groovy.tools.shell.CommandSupport):
    def __init__(self, groovysh: org.codehaus.groovy.tools.shell.Groovysh): ...
    def execute(self, list: java.util.List[str]) -> typing.Any: ...
    def getCompleter(self) -> jline.console.completer.Completer: ...

class ImportCompleter(jline.console.completer.Completer, groovy.lang.GroovyObject):
    def __init__(self, packageHelper: org.codehaus.groovy.tools.shell.util.PackageHelper, evaluator: org.codehaus.groovy.tools.shell.Evaluator, boolean: bool): ...
    def complete(self, string: str, int: int, list: java.util.List[typing.Union[java.lang.CharSequence, str]]) -> int: ...
    def getInterpreter(self) -> org.codehaus.groovy.tools.shell.Evaluator: ...
    def getPackageHelper(self) -> org.codehaus.groovy.tools.shell.util.PackageHelper: ...
    def getShell(self) -> org.codehaus.groovy.tools.shell.Groovysh: ...
    def getStaticImport(self) -> bool: ...
    def isStaticImport(self) -> bool: ...
    def setPackageHelper(self, packageHelper: org.codehaus.groovy.tools.shell.util.PackageHelper) -> None: ...
    def setShell(self, groovysh: org.codehaus.groovy.tools.shell.Groovysh) -> None: ...

class InspectCommand(org.codehaus.groovy.tools.shell.CommandSupport):
    COMMAND_NAME: typing.ClassVar[str] = ...
    def __init__(self, groovysh: org.codehaus.groovy.tools.shell.Groovysh): ...
    def execute(self, list: java.util.List[str]) -> typing.Any: ...
    def getHeadless(self) -> typing.Any: ...
    def getLafInitialized(self) -> typing.Any: ...
    def setHeadless(self, object: typing.Any) -> None: ...
    def setLafInitialized(self, object: typing.Any) -> None: ...

class InspectCommandCompletor(org.codehaus.groovy.tools.shell.util.SimpleCompletor):
    def __init__(self, binding: groovy.lang.Binding): ...
    def getCandidates(self) -> java.util.SortedSet[str]: ...

class LoadCommand(org.codehaus.groovy.tools.shell.CommandSupport):
    COMMAND_NAME: typing.ClassVar[str] = ...
    def __init__(self, groovysh: org.codehaus.groovy.tools.shell.Groovysh): ...
    def execute(self, list: java.util.List[str]) -> typing.Any: ...
    def load(self, uRL: java.net.URL) -> None: ...

class PurgeCommand(org.codehaus.groovy.tools.shell.ComplexCommandSupport):
    COMMAND_NAME: typing.ClassVar[str] = ...
    def __init__(self, groovysh: org.codehaus.groovy.tools.shell.Groovysh): ...
    def getDo_classes(self) -> typing.Any: ...
    def getDo_imports(self) -> typing.Any: ...
    def getDo_preferences(self) -> typing.Any: ...
    def getDo_variables(self) -> typing.Any: ...
    def setDo_classes(self, object: typing.Any) -> None: ...
    def setDo_imports(self, object: typing.Any) -> None: ...
    def setDo_preferences(self, object: typing.Any) -> None: ...
    def setDo_variables(self, object: typing.Any) -> None: ...
    class _closure1(groovy.lang.Closure, org.codehaus.groovy.runtime.GeneratedClosure):
        def __init__(self, object: typing.Any, object2: typing.Any): ...
        @typing.overload
        def doCall(self) -> typing.Any: ...
        @typing.overload
        def doCall(self, object: typing.Any) -> typing.Any: ...
    class _closure2(groovy.lang.Closure, org.codehaus.groovy.runtime.GeneratedClosure):
        def __init__(self, object: typing.Any, object2: typing.Any): ...
        @typing.overload
        def doCall(self) -> typing.Any: ...
        @typing.overload
        def doCall(self, object: typing.Any) -> typing.Any: ...
    class _closure3(groovy.lang.Closure, org.codehaus.groovy.runtime.GeneratedClosure):
        def __init__(self, object: typing.Any, object2: typing.Any): ...
        @typing.overload
        def doCall(self) -> typing.Any: ...
        @typing.overload
        def doCall(self, object: typing.Any) -> typing.Any: ...
    class _closure4(groovy.lang.Closure, org.codehaus.groovy.runtime.GeneratedClosure):
        def __init__(self, object: typing.Any, object2: typing.Any): ...
        @typing.overload
        def doCall(self) -> typing.Any: ...
        @typing.overload
        def doCall(self, object: typing.Any) -> typing.Any: ...

class RecordCommand(org.codehaus.groovy.tools.shell.ComplexCommandSupport):
    COMMAND_NAME: typing.ClassVar[str] = ...
    def __init__(self, groovysh: org.codehaus.groovy.tools.shell.Groovysh): ...
    def getDo_start(self) -> typing.Any: ...
    def getDo_status(self) -> typing.Any: ...
    def getDo_stop(self) -> typing.Any: ...
    def isRecording(self) -> bool: ...
    def recordError(self, throwable: java.lang.Throwable) -> typing.Any: ...
    def recordInput(self, string: str) -> typing.Any: ...
    def recordResult(self, object: typing.Any) -> typing.Any: ...
    def setDo_start(self, object: typing.Any) -> None: ...
    def setDo_status(self, object: typing.Any) -> None: ...
    def setDo_stop(self, object: typing.Any) -> None: ...
    class _closure1(groovy.lang.Closure, org.codehaus.groovy.runtime.GeneratedClosure):
        def __init__(self, object: typing.Any, object2: typing.Any): ...
        @typing.overload
        def call(self) -> typing.Any: ...
        @typing.overload
        def call(self, object: typing.Any) -> typing.Any: ...
        @typing.overload
        def call(self, *object: typing.Any) -> typing.Any: ...
        @typing.overload
        def call(self, list: java.util.List[str]) -> typing.Any: ...
        def doCall(self, list: java.util.List[str]) -> typing.Any: ...
    class _closure2(groovy.lang.Closure, org.codehaus.groovy.runtime.GeneratedClosure):
        def __init__(self, object: typing.Any, object2: typing.Any): ...
        @typing.overload
        def doCall(self) -> typing.Any: ...
        @typing.overload
        def doCall(self, object: typing.Any) -> typing.Any: ...
    class _closure3(groovy.lang.Closure, org.codehaus.groovy.runtime.GeneratedClosure):
        def __init__(self, object: typing.Any, object2: typing.Any): ...
        @typing.overload
        def doCall(self) -> typing.Any: ...
        @typing.overload
        def doCall(self, object: typing.Any) -> typing.Any: ...
    class _closure4(groovy.lang.Closure, org.codehaus.groovy.runtime.GeneratedClosure):
        def __init__(self, object: typing.Any, object2: typing.Any): ...
        @typing.overload
        def doCall(self) -> typing.Any: ...
        @typing.overload
        def doCall(self, object: typing.Any) -> typing.Any: ...

class RegisterCommand(org.codehaus.groovy.tools.shell.CommandSupport):
    def __init__(self, groovysh: org.codehaus.groovy.tools.shell.Groovysh): ...
    def execute(self, list: java.util.List[str]) -> typing.Any: ...
    @staticmethod
    def getCOMMAND_NAME() -> str: ...

class SaveCommand(org.codehaus.groovy.tools.shell.CommandSupport):
    COMMAND_NAME: typing.ClassVar[str] = ...
    def __init__(self, groovysh: org.codehaus.groovy.tools.shell.Groovysh): ...
    def execute(self, list: java.util.List[str]) -> typing.Any: ...

class SetCommand(org.codehaus.groovy.tools.shell.CommandSupport):
    COMMAND_NAME: typing.ClassVar[str] = ...
    def __init__(self, groovysh: org.codehaus.groovy.tools.shell.Groovysh): ...
    def execute(self, list: java.util.List[str]) -> typing.Any: ...

class ShadowCommand(org.codehaus.groovy.tools.shell.ComplexCommandSupport):
    COMMAND_NAME: typing.ClassVar[str] = ...
    def __init__(self, groovysh: org.codehaus.groovy.tools.shell.Groovysh): ...
    def getDo_debug(self) -> typing.Any: ...
    def getDo_info(self) -> typing.Any: ...
    def getDo_this(self) -> typing.Any: ...
    def getDo_verbose(self) -> typing.Any: ...
    def setDo_debug(self, object: typing.Any) -> None: ...
    def setDo_info(self, object: typing.Any) -> None: ...
    def setDo_this(self, object: typing.Any) -> None: ...
    def setDo_verbose(self, object: typing.Any) -> None: ...
    class _closure1(groovy.lang.Closure, org.codehaus.groovy.runtime.GeneratedClosure):
        def __init__(self, object: typing.Any, object2: typing.Any): ...
        @typing.overload
        def doCall(self) -> typing.Any: ...
        @typing.overload
        def doCall(self, object: typing.Any) -> typing.Any: ...
    class _closure2(groovy.lang.Closure, org.codehaus.groovy.runtime.GeneratedClosure):
        def __init__(self, object: typing.Any, object2: typing.Any): ...
        @typing.overload
        def doCall(self) -> typing.Any: ...
        @typing.overload
        def doCall(self, object: typing.Any) -> typing.Any: ...
    class _closure3(groovy.lang.Closure, org.codehaus.groovy.runtime.GeneratedClosure):
        def __init__(self, object: typing.Any, object2: typing.Any): ...
        @typing.overload
        def doCall(self) -> typing.Any: ...
        @typing.overload
        def doCall(self, object: typing.Any) -> typing.Any: ...
    class _closure4(groovy.lang.Closure, org.codehaus.groovy.runtime.GeneratedClosure):
        def __init__(self, object: typing.Any, object2: typing.Any): ...
        @typing.overload
        def doCall(self) -> typing.Any: ...
        @typing.overload
        def doCall(self, object: typing.Any) -> typing.Any: ...

class ShowCommand(org.codehaus.groovy.tools.shell.ComplexCommandSupport):
    COMMAND_NAME: typing.ClassVar[str] = ...
    def __init__(self, groovysh: org.codehaus.groovy.tools.shell.Groovysh): ...
    def getDo_classes(self) -> typing.Any: ...
    def getDo_imports(self) -> typing.Any: ...
    def getDo_preferences(self) -> typing.Any: ...
    def getDo_variables(self) -> typing.Any: ...
    def setDo_classes(self, object: typing.Any) -> None: ...
    def setDo_imports(self, object: typing.Any) -> None: ...
    def setDo_preferences(self, object: typing.Any) -> None: ...
    def setDo_variables(self, object: typing.Any) -> None: ...
    class _closure1(groovy.lang.Closure, org.codehaus.groovy.runtime.GeneratedClosure):
        def __init__(self, object: typing.Any, object2: typing.Any): ...
        @typing.overload
        def doCall(self) -> typing.Any: ...
        @typing.overload
        def doCall(self, object: typing.Any) -> typing.Any: ...
    class _closure2(groovy.lang.Closure, org.codehaus.groovy.runtime.GeneratedClosure):
        def __init__(self, object: typing.Any, object2: typing.Any): ...
        @typing.overload
        def doCall(self) -> typing.Any: ...
        @typing.overload
        def doCall(self, object: typing.Any) -> typing.Any: ...
    class _closure3(groovy.lang.Closure, org.codehaus.groovy.runtime.GeneratedClosure):
        def __init__(self, object: typing.Any, object2: typing.Any): ...
        @typing.overload
        def doCall(self) -> typing.Any: ...
        @typing.overload
        def doCall(self, object: typing.Any) -> typing.Any: ...
    class _closure4(groovy.lang.Closure, org.codehaus.groovy.runtime.GeneratedClosure):
        def __init__(self, object: typing.Any, object2: typing.Any): ...
        @typing.overload
        def doCall(self) -> typing.Any: ...
        @typing.overload
        def doCall(self, object: typing.Any) -> typing.Any: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.tools.shell.commands")``.

    AliasCommand: typing.Type[AliasCommand]
    AliasTargetProxyCommand: typing.Type[AliasTargetProxyCommand]
    ClearCommand: typing.Type[ClearCommand]
    DisplayCommand: typing.Type[DisplayCommand]
    DocCommand: typing.Type[DocCommand]
    EditCommand: typing.Type[EditCommand]
    ExitCommand: typing.Type[ExitCommand]
    GrabCommand: typing.Type[GrabCommand]
    HelpCommand: typing.Type[HelpCommand]
    HistoryCommand: typing.Type[HistoryCommand]
    ImportCommand: typing.Type[ImportCommand]
    ImportCompleter: typing.Type[ImportCompleter]
    InspectCommand: typing.Type[InspectCommand]
    InspectCommandCompletor: typing.Type[InspectCommandCompletor]
    LoadCommand: typing.Type[LoadCommand]
    PurgeCommand: typing.Type[PurgeCommand]
    RecordCommand: typing.Type[RecordCommand]
    RegisterCommand: typing.Type[RegisterCommand]
    SaveCommand: typing.Type[SaveCommand]
    SetCommand: typing.Type[SetCommand]
    ShadowCommand: typing.Type[ShadowCommand]
    ShowCommand: typing.Type[ShowCommand]
