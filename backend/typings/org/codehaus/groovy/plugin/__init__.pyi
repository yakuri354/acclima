
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.apache.groovy.plugin
import typing



class GroovyRunner(org.apache.groovy.plugin.GroovyRunner): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.plugin")``.

    GroovyRunner: typing.Type[GroovyRunner]
