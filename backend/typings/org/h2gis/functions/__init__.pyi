
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.h2gis.functions.factory
import org.h2gis.functions.io
import org.h2gis.functions.spatial
import org.h2gis.functions.string
import org.h2gis.functions.system
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.functions")``.

    factory: org.h2gis.functions.factory.__module_protocol__
    io: org.h2gis.functions.io.__module_protocol__
    spatial: org.h2gis.functions.spatial.__module_protocol__
    string: org.h2gis.functions.string.__module_protocol__
    system: org.h2gis.functions.system.__module_protocol__
