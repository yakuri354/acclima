
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import org.h2gis.api
import org.locationtech.jts.geom
import typing



class ST_Rotate(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @typing.overload
    @staticmethod
    def rotate(geometry: org.locationtech.jts.geom.Geometry, double: float) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def rotate(geometry: org.locationtech.jts.geom.Geometry, double: float, double2: float, double3: float) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def rotate(geometry: org.locationtech.jts.geom.Geometry, double: float, point: org.locationtech.jts.geom.Point) -> org.locationtech.jts.geom.Geometry: ...

class ST_Scale(org.h2gis.api.DeterministicScalarFunction):
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @typing.overload
    @staticmethod
    def scale(geometry: org.locationtech.jts.geom.Geometry, double: float, double2: float) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def scale(geometry: org.locationtech.jts.geom.Geometry, double: float, double2: float, double3: float) -> org.locationtech.jts.geom.Geometry: ...

class ST_Translate(org.h2gis.api.DeterministicScalarFunction):
    MIXED_DIM_ERROR: typing.ClassVar[str] = ...
    def __init__(self): ...
    def getJavaStaticMethod(self) -> str: ...
    @typing.overload
    @staticmethod
    def translate(geometry: org.locationtech.jts.geom.Geometry, double: float, double2: float) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def translate(geometry: org.locationtech.jts.geom.Geometry, double: float, double2: float, double3: float) -> org.locationtech.jts.geom.Geometry: ...

class ZAffineTransformation(java.lang.Cloneable, org.locationtech.jts.geom.CoordinateSequenceFilter):
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, double11: float, double12: float): ...
    def filter(self, coordinateSequence: org.locationtech.jts.geom.CoordinateSequence, int: int) -> None: ...
    def isDone(self) -> bool: ...
    def isGeometryChanged(self) -> bool: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.h2gis.functions.spatial.affine_transformations")``.

    ST_Rotate: typing.Type[ST_Rotate]
    ST_Scale: typing.Type[ST_Scale]
    ST_Translate: typing.Type[ST_Translate]
    ZAffineTransformation: typing.Type[ZAffineTransformation]
