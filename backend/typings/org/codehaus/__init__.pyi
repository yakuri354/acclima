
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.codehaus.groovy
import org.codehaus.mojo
import org.codehaus.stax2
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus")``.

    groovy: org.codehaus.groovy.__module_protocol__
    mojo: org.codehaus.mojo.__module_protocol__
    stax2: org.codehaus.stax2.__module_protocol__
