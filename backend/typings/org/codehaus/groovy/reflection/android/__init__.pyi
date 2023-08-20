
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import typing



class AndroidSupport:
    def __init__(self): ...
    @staticmethod
    def isRunningAndroid() -> bool: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.reflection.android")``.

    AndroidSupport: typing.Type[AndroidSupport]
