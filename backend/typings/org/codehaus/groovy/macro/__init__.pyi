
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.codehaus.groovy.macro.matcher
import org.codehaus.groovy.macro.methods
import org.codehaus.groovy.macro.runtime
import org.codehaus.groovy.macro.transform
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.macro")``.

    matcher: org.codehaus.groovy.macro.matcher.__module_protocol__
    methods: org.codehaus.groovy.macro.methods.__module_protocol__
    runtime: org.codehaus.groovy.macro.runtime.__module_protocol__
    transform: org.codehaus.groovy.macro.transform.__module_protocol__
