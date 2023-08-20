
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.codehaus.groovy.vmplugin.v5
import typing



class Java6(org.codehaus.groovy.vmplugin.v5.Java5):
    def __init__(self): ...
    def getVersion(self) -> int: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.vmplugin.v6")``.

    Java6: typing.Type[Java6]
