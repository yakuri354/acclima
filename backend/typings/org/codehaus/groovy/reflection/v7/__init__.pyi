
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import org.codehaus.groovy.reflection
import typing



_GroovyClassValueJava7__T = typing.TypeVar('_GroovyClassValueJava7__T')  # <T>
class GroovyClassValueJava7(java.lang.ClassValue[_GroovyClassValueJava7__T], org.codehaus.groovy.reflection.GroovyClassValue[_GroovyClassValueJava7__T], typing.Generic[_GroovyClassValueJava7__T]):
    def __init__(self, computeValue: org.codehaus.groovy.reflection.GroovyClassValue.ComputeValue[_GroovyClassValueJava7__T]): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.reflection.v7")``.

    GroovyClassValueJava7: typing.Type[GroovyClassValueJava7]
