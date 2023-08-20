
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.h2gis.api
import org.locationtech.jts.geom
import typing



class ST_Azimuth(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    @staticmethod
    def azimuth(geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry) -> float: ...
    def getJavaStaticMethod(self) -> str: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.functions.spatial.trigonometry")``.

    ST_Azimuth: typing.Type[ST_Azimuth]
