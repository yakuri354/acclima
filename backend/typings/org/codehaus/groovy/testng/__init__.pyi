
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.apache.groovy.plugin.testng
import org.codehaus.groovy.plugin
import typing



class TestNgRunner(org.apache.groovy.plugin.testng.TestNgRunner, org.codehaus.groovy.plugin.GroovyRunner):
    def __init__(self): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.testng")``.

    TestNgRunner: typing.Type[TestNgRunner]
