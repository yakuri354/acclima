
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.h2gis.api
import org.h2gis.functions
import org.h2gis.utilities
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis")``.

    api: org.h2gis.api.__module_protocol__
    functions: org.h2gis.functions.__module_protocol__
    utilities: org.h2gis.utilities.__module_protocol__
