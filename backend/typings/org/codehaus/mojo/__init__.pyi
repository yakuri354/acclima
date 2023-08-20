
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.codehaus.mojo.animal_sniffer
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.mojo")``.

    animal_sniffer: org.codehaus.mojo.animal_sniffer.__module_protocol__
