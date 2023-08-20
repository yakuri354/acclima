
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import org.locationtech.jts.algorithm
import org.locationtech.jts.awt
import org.locationtech.jts.densify
import org.locationtech.jts.dissolve
import org.locationtech.jts.edgegraph
import org.locationtech.jts.geom
import org.locationtech.jts.geomgraph
import org.locationtech.jts.index
import org.locationtech.jts.io
import org.locationtech.jts.linearref
import org.locationtech.jts.math
import org.locationtech.jts.noding
import org.locationtech.jts.operation
import org.locationtech.jts.planargraph
import org.locationtech.jts.precision
import org.locationtech.jts.shape
import org.locationtech.jts.simplify
import org.locationtech.jts.triangulate
import org.locationtech.jts.util
import typing



class JTSVersion:
    CURRENT_VERSION: typing.ClassVar['JTSVersion'] = ...
    MAJOR: typing.ClassVar[int] = ...
    MINOR: typing.ClassVar[int] = ...
    PATCH: typing.ClassVar[int] = ...
    def getMajor(self) -> int: ...
    def getMinor(self) -> int: ...
    def getPatch(self) -> int: ...
    @staticmethod
    def main(stringArray: typing.Union[typing.List[str], jpype.JArray]) -> None: ...
    def toString(self) -> str: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.locationtech.jts")``.

    JTSVersion: typing.Type[JTSVersion]
    algorithm: org.locationtech.jts.algorithm.__module_protocol__
    awt: org.locationtech.jts.awt.__module_protocol__
    densify: org.locationtech.jts.densify.__module_protocol__
    dissolve: org.locationtech.jts.dissolve.__module_protocol__
    edgegraph: org.locationtech.jts.edgegraph.__module_protocol__
    geom: org.locationtech.jts.geom.__module_protocol__
    geomgraph: org.locationtech.jts.geomgraph.__module_protocol__
    index: org.locationtech.jts.index.__module_protocol__
    io: org.locationtech.jts.io.__module_protocol__
    linearref: org.locationtech.jts.linearref.__module_protocol__
    math: org.locationtech.jts.math.__module_protocol__
    noding: org.locationtech.jts.noding.__module_protocol__
    operation: org.locationtech.jts.operation.__module_protocol__
    planargraph: org.locationtech.jts.planargraph.__module_protocol__
    precision: org.locationtech.jts.precision.__module_protocol__
    shape: org.locationtech.jts.shape.__module_protocol__
    simplify: org.locationtech.jts.simplify.__module_protocol__
    triangulate: org.locationtech.jts.triangulate.__module_protocol__
    util: org.locationtech.jts.util.__module_protocol__
