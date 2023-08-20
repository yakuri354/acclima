
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org.locationtech.jts.planargraph
import typing



class ConnectedSubgraphFinder:
    def __init__(self, planarGraph: org.locationtech.jts.planargraph.PlanarGraph): ...
    def getConnectedSubgraphs(self) -> java.util.List: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.locationtech.jts.planargraph.algorithm")``.

    ConnectedSubgraphFinder: typing.Type[ConnectedSubgraphFinder]
