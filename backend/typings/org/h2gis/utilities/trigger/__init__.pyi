
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.sql
import jpype
import org.h2.api
import typing



class UpdateTrigger(org.h2.api.Trigger):
    TRIGGER_SCHEMA: typing.ClassVar[str] = ...
    TRIGGER_TABLE: typing.ClassVar[str] = ...
    NOTIFICATION_TABLE: typing.ClassVar[str] = ...
    def __init__(self): ...
    def close(self) -> None: ...
    def fire(self, connection: java.sql.Connection, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray], objectArray2: typing.Union[typing.List[typing.Any], jpype.JArray]) -> None: ...
    def init(self, connection: java.sql.Connection, string: str, string2: str, string3: str, boolean: bool, int: int) -> None: ...
    def remove(self) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.utilities.trigger")``.

    UpdateTrigger: typing.Type[UpdateTrigger]
