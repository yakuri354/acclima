
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.codehaus
import org.h2gis
import org.locationtech
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org")``.

    codehaus: org.codehaus.__module_protocol__
    h2gis: org.h2gis.__module_protocol__
    locationtech: org.locationtech.__module_protocol__
