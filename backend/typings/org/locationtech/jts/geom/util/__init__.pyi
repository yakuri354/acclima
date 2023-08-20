
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import jpype
import org
import org.locationtech.jts.geom
import org.locationtech.jts.util
import typing



class AffineTransformation(java.lang.Cloneable, org.locationtech.jts.geom.CoordinateSequenceFilter):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, coordinate: org.locationtech.jts.geom.Coordinate, coordinate2: org.locationtech.jts.geom.Coordinate, coordinate3: org.locationtech.jts.geom.Coordinate, coordinate4: org.locationtech.jts.geom.Coordinate, coordinate5: org.locationtech.jts.geom.Coordinate, coordinate6: org.locationtech.jts.geom.Coordinate): ...
    @typing.overload
    def __init__(self, affineTransformation: 'AffineTransformation'): ...
    def clone(self) -> typing.Any: ...
    def compose(self, affineTransformation: 'AffineTransformation') -> 'AffineTransformation': ...
    def composeBefore(self, affineTransformation: 'AffineTransformation') -> 'AffineTransformation': ...
    def equals(self, object: typing.Any) -> bool: ...
    def filter(self, coordinateSequence: org.locationtech.jts.geom.CoordinateSequence, int: int) -> None: ...
    def getDeterminant(self) -> float: ...
    def getInverse(self) -> 'AffineTransformation': ...
    def getMatrixEntries(self) -> typing.MutableSequence[float]: ...
    def hashCode(self) -> int: ...
    def isDone(self) -> bool: ...
    def isGeometryChanged(self) -> bool: ...
    def isIdentity(self) -> bool: ...
    @typing.overload
    def reflect(self, double: float, double2: float) -> 'AffineTransformation': ...
    @typing.overload
    def reflect(self, double: float, double2: float, double3: float, double4: float) -> 'AffineTransformation': ...
    @typing.overload
    @staticmethod
    def reflectionInstance(double: float, double2: float) -> 'AffineTransformation': ...
    @typing.overload
    @staticmethod
    def reflectionInstance(double: float, double2: float, double3: float, double4: float) -> 'AffineTransformation': ...
    @typing.overload
    def rotate(self, double: float) -> 'AffineTransformation': ...
    @typing.overload
    def rotate(self, double: float, double2: float) -> 'AffineTransformation': ...
    @typing.overload
    def rotate(self, double: float, double2: float, double3: float) -> 'AffineTransformation': ...
    @typing.overload
    def rotate(self, double: float, double2: float, double3: float, double4: float) -> 'AffineTransformation': ...
    @typing.overload
    @staticmethod
    def rotationInstance(double: float) -> 'AffineTransformation': ...
    @typing.overload
    @staticmethod
    def rotationInstance(double: float, double2: float) -> 'AffineTransformation': ...
    @typing.overload
    @staticmethod
    def rotationInstance(double: float, double2: float, double3: float) -> 'AffineTransformation': ...
    @typing.overload
    @staticmethod
    def rotationInstance(double: float, double2: float, double3: float, double4: float) -> 'AffineTransformation': ...
    def scale(self, double: float, double2: float) -> 'AffineTransformation': ...
    @typing.overload
    @staticmethod
    def scaleInstance(double: float, double2: float) -> 'AffineTransformation': ...
    @typing.overload
    @staticmethod
    def scaleInstance(double: float, double2: float, double3: float, double4: float) -> 'AffineTransformation': ...
    def setToIdentity(self) -> 'AffineTransformation': ...
    @typing.overload
    def setToReflection(self, double: float, double2: float) -> 'AffineTransformation': ...
    @typing.overload
    def setToReflection(self, double: float, double2: float, double3: float, double4: float) -> 'AffineTransformation': ...
    def setToReflectionBasic(self, double: float, double2: float, double3: float, double4: float) -> 'AffineTransformation': ...
    @typing.overload
    def setToRotation(self, double: float) -> 'AffineTransformation': ...
    @typing.overload
    def setToRotation(self, double: float, double2: float) -> 'AffineTransformation': ...
    @typing.overload
    def setToRotation(self, double: float, double2: float, double3: float) -> 'AffineTransformation': ...
    @typing.overload
    def setToRotation(self, double: float, double2: float, double3: float, double4: float) -> 'AffineTransformation': ...
    def setToScale(self, double: float, double2: float) -> 'AffineTransformation': ...
    def setToShear(self, double: float, double2: float) -> 'AffineTransformation': ...
    def setToTranslation(self, double: float, double2: float) -> 'AffineTransformation': ...
    @typing.overload
    def setTransformation(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float) -> 'AffineTransformation': ...
    @typing.overload
    def setTransformation(self, affineTransformation: 'AffineTransformation') -> 'AffineTransformation': ...
    def shear(self, double: float, double2: float) -> 'AffineTransformation': ...
    @staticmethod
    def shearInstance(double: float, double2: float) -> 'AffineTransformation': ...
    def toString(self) -> str: ...
    @typing.overload
    def transform(self, coordinate: org.locationtech.jts.geom.Coordinate, coordinate2: org.locationtech.jts.geom.Coordinate) -> org.locationtech.jts.geom.Coordinate: ...
    @typing.overload
    def transform(self, geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    def transform(self, coordinateSequence: org.locationtech.jts.geom.CoordinateSequence, int: int) -> None: ...
    def translate(self, double: float, double2: float) -> 'AffineTransformation': ...
    @staticmethod
    def translationInstance(double: float, double2: float) -> 'AffineTransformation': ...

class AffineTransformationBuilder:
    def __init__(self, coordinate: org.locationtech.jts.geom.Coordinate, coordinate2: org.locationtech.jts.geom.Coordinate, coordinate3: org.locationtech.jts.geom.Coordinate, coordinate4: org.locationtech.jts.geom.Coordinate, coordinate5: org.locationtech.jts.geom.Coordinate, coordinate6: org.locationtech.jts.geom.Coordinate): ...
    def getTransformation(self) -> AffineTransformation: ...

class AffineTransformationFactory:
    def __init__(self): ...
    @staticmethod
    def createFromBaseLines(coordinate: org.locationtech.jts.geom.Coordinate, coordinate2: org.locationtech.jts.geom.Coordinate, coordinate3: org.locationtech.jts.geom.Coordinate, coordinate4: org.locationtech.jts.geom.Coordinate) -> AffineTransformation: ...
    @typing.overload
    @staticmethod
    def createFromControlVectors(coordinate: org.locationtech.jts.geom.Coordinate, coordinate2: org.locationtech.jts.geom.Coordinate) -> AffineTransformation: ...
    @typing.overload
    @staticmethod
    def createFromControlVectors(coordinate: org.locationtech.jts.geom.Coordinate, coordinate2: org.locationtech.jts.geom.Coordinate, coordinate3: org.locationtech.jts.geom.Coordinate, coordinate4: org.locationtech.jts.geom.Coordinate) -> AffineTransformation: ...
    @typing.overload
    @staticmethod
    def createFromControlVectors(coordinate: org.locationtech.jts.geom.Coordinate, coordinate2: org.locationtech.jts.geom.Coordinate, coordinate3: org.locationtech.jts.geom.Coordinate, coordinate4: org.locationtech.jts.geom.Coordinate, coordinate5: org.locationtech.jts.geom.Coordinate, coordinate6: org.locationtech.jts.geom.Coordinate) -> AffineTransformation: ...
    @typing.overload
    @staticmethod
    def createFromControlVectors(coordinateArray: typing.Union[typing.List[org.locationtech.jts.geom.Coordinate], jpype.JArray], coordinateArray2: typing.Union[typing.List[org.locationtech.jts.geom.Coordinate], jpype.JArray]) -> AffineTransformation: ...

class ComponentCoordinateExtracter(org.locationtech.jts.geom.GeometryComponentFilter):
    def __init__(self, list: java.util.List): ...
    def filter(self, geometry: org.locationtech.jts.geom.Geometry) -> None: ...
    @staticmethod
    def getCoordinates(geometry: org.locationtech.jts.geom.Geometry) -> java.util.List: ...

class GeometryCollectionMapper:
    def __init__(self, mapOp: 'GeometryMapper.MapOp'): ...
    @typing.overload
    def map(self, geometryCollection: org.locationtech.jts.geom.GeometryCollection) -> org.locationtech.jts.geom.GeometryCollection: ...
    @typing.overload
    @staticmethod
    def map(geometryCollection: org.locationtech.jts.geom.GeometryCollection, mapOp: 'GeometryMapper.MapOp') -> org.locationtech.jts.geom.GeometryCollection: ...

class GeometryCombiner:
    def __init__(self, collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set]): ...
    @typing.overload
    def combine(self) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def combine(collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set]) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def combine(geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def combine(geometry: org.locationtech.jts.geom.Geometry, geometry2: org.locationtech.jts.geom.Geometry, geometry3: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...
    @staticmethod
    def extractFactory(collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set]) -> org.locationtech.jts.geom.GeometryFactory: ...

class GeometryExtracter(org.locationtech.jts.geom.GeometryFilter):
    @typing.overload
    def __init__(self, class_: typing.Type, list: java.util.List): ...
    @typing.overload
    def __init__(self, string: str, list: java.util.List): ...
    @typing.overload
    @staticmethod
    def extract(geometry: org.locationtech.jts.geom.Geometry, class_: typing.Type) -> java.util.List: ...
    @typing.overload
    @staticmethod
    def extract(geometry: org.locationtech.jts.geom.Geometry, class_: typing.Type, list: java.util.List) -> java.util.List: ...
    @typing.overload
    @staticmethod
    def extract(geometry: org.locationtech.jts.geom.Geometry, string: str) -> java.util.List: ...
    @typing.overload
    @staticmethod
    def extract(geometry: org.locationtech.jts.geom.Geometry, string: str, list: java.util.List) -> java.util.List: ...
    def filter(self, geometry: org.locationtech.jts.geom.Geometry) -> None: ...

class GeometryFixer:
    def __init__(self, geometry: org.locationtech.jts.geom.Geometry): ...
    @typing.overload
    @staticmethod
    def fix(geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def fix(geometry: org.locationtech.jts.geom.Geometry, boolean: bool) -> org.locationtech.jts.geom.Geometry: ...
    def getResult(self) -> org.locationtech.jts.geom.Geometry: ...
    def setKeepCollapsed(self, boolean: bool) -> None: ...
    def setKeepMulti(self, boolean: bool) -> None: ...

class GeometryMapper:
    def __init__(self): ...
    @staticmethod
    def flatMap(geometry: org.locationtech.jts.geom.Geometry, int: int, mapOp: 'GeometryMapper.MapOp') -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def map(collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set], mapOp: 'GeometryMapper.MapOp') -> java.util.Collection: ...
    @typing.overload
    @staticmethod
    def map(geometry: org.locationtech.jts.geom.Geometry, mapOp: 'GeometryMapper.MapOp') -> org.locationtech.jts.geom.Geometry: ...
    class MapOp:
        def map(self, geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...

class GeometryTransformer:
    def __init__(self): ...
    def getInputGeometry(self) -> org.locationtech.jts.geom.Geometry: ...
    def transform(self, geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...

class LineStringExtracter(org.locationtech.jts.geom.GeometryFilter):
    def __init__(self, list: java.util.List): ...
    def filter(self, geometry: org.locationtech.jts.geom.Geometry) -> None: ...
    @staticmethod
    def getGeometry(geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def getLines(geometry: org.locationtech.jts.geom.Geometry) -> java.util.List: ...
    @typing.overload
    @staticmethod
    def getLines(geometry: org.locationtech.jts.geom.Geometry, list: java.util.List) -> java.util.List: ...

class LinearComponentExtracter(org.locationtech.jts.geom.GeometryComponentFilter):
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set]): ...
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set], boolean: bool): ...
    def filter(self, geometry: org.locationtech.jts.geom.Geometry) -> None: ...
    @typing.overload
    @staticmethod
    def getGeometry(geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def getGeometry(geometry: org.locationtech.jts.geom.Geometry, boolean: bool) -> org.locationtech.jts.geom.Geometry: ...
    @typing.overload
    @staticmethod
    def getLines(collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set], collection2: typing.Union[java.util.Collection, typing.Sequence, typing.Set]) -> java.util.Collection: ...
    @typing.overload
    @staticmethod
    def getLines(collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set], collection2: typing.Union[java.util.Collection, typing.Sequence, typing.Set], boolean: bool) -> java.util.Collection: ...
    @typing.overload
    @staticmethod
    def getLines(geometry: org.locationtech.jts.geom.Geometry, collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set]) -> java.util.Collection: ...
    @typing.overload
    @staticmethod
    def getLines(geometry: org.locationtech.jts.geom.Geometry, collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set], boolean: bool) -> java.util.Collection: ...
    @typing.overload
    @staticmethod
    def getLines(geometry: org.locationtech.jts.geom.Geometry) -> java.util.List: ...
    @typing.overload
    @staticmethod
    def getLines(geometry: org.locationtech.jts.geom.Geometry, boolean: bool) -> java.util.List: ...
    def setForceToLineString(self, boolean: bool) -> None: ...

class NoninvertibleTransformationException(java.lang.Exception):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class PointExtracter(org.locationtech.jts.geom.GeometryFilter):
    def __init__(self, list: java.util.List): ...
    def filter(self, geometry: org.locationtech.jts.geom.Geometry) -> None: ...
    @typing.overload
    @staticmethod
    def getPoints(geometry: org.locationtech.jts.geom.Geometry) -> java.util.List: ...
    @typing.overload
    @staticmethod
    def getPoints(geometry: org.locationtech.jts.geom.Geometry, list: java.util.List) -> java.util.List: ...

class PolygonExtracter(org.locationtech.jts.geom.GeometryFilter):
    def __init__(self, list: java.util.List): ...
    def filter(self, geometry: org.locationtech.jts.geom.Geometry) -> None: ...
    @typing.overload
    @staticmethod
    def getPolygons(geometry: org.locationtech.jts.geom.Geometry) -> java.util.List: ...
    @typing.overload
    @staticmethod
    def getPolygons(geometry: org.locationtech.jts.geom.Geometry, list: java.util.List) -> java.util.List: ...

class ShortCircuitedGeometryVisitor:
    def __init__(self): ...
    def applyTo(self, geometry: org.locationtech.jts.geom.Geometry) -> None: ...

class SineStarFactory(org.locationtech.jts.util.GeometricShapeFactory):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, geometryFactory: org.locationtech.jts.geom.GeometryFactory): ...
    @staticmethod
    def create(coordinate: org.locationtech.jts.geom.Coordinate, double: float, int: int, int2: int, double2: float) -> org.locationtech.jts.geom.Geometry: ...
    def createSineStar(self) -> org.locationtech.jts.geom.Geometry: ...
    def setArmLengthRatio(self, double: float) -> None: ...
    def setNumArms(self, int: int) -> None: ...

class GeometryEditor:
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, geometryFactory: org.locationtech.jts.geom.GeometryFactory): ...
    def edit(self, geometry: org.locationtech.jts.geom.Geometry, geometryEditorOperation: 'GeometryEditor.GeometryEditorOperation') -> org.locationtech.jts.geom.Geometry: ...
    def setCopyUserData(self, boolean: bool) -> None: ...
    class CoordinateOperation(org.locationtech.jts.geom.util.GeometryEditor.GeometryEditorOperation):
        def __init__(self): ...
        @typing.overload
        def edit(self, coordinateArray: typing.Union[typing.List[org.locationtech.jts.geom.Coordinate], jpype.JArray], geometry: org.locationtech.jts.geom.Geometry) -> typing.MutableSequence[org.locationtech.jts.geom.Coordinate]: ...
        @typing.overload
        def edit(self, geometry: org.locationtech.jts.geom.Geometry, geometryFactory: org.locationtech.jts.geom.GeometryFactory) -> org.locationtech.jts.geom.Geometry: ...
    class CoordinateSequenceOperation(org.locationtech.jts.geom.util.GeometryEditor.GeometryEditorOperation):
        def __init__(self): ...
        @typing.overload
        def edit(self, coordinateSequence: org.locationtech.jts.geom.CoordinateSequence, geometry: org.locationtech.jts.geom.Geometry) -> org.locationtech.jts.geom.CoordinateSequence: ...
        @typing.overload
        def edit(self, geometry: org.locationtech.jts.geom.Geometry, geometryFactory: org.locationtech.jts.geom.GeometryFactory) -> org.locationtech.jts.geom.Geometry: ...
    class GeometryEditorOperation:
        def edit(self, geometry: org.locationtech.jts.geom.Geometry, geometryFactory: org.locationtech.jts.geom.GeometryFactory) -> org.locationtech.jts.geom.Geometry: ...
    class NoOpGeometryOperation(org.locationtech.jts.geom.util.GeometryEditor.GeometryEditorOperation):
        def __init__(self): ...
        def edit(self, geometry: org.locationtech.jts.geom.Geometry, geometryFactory: org.locationtech.jts.geom.GeometryFactory) -> org.locationtech.jts.geom.Geometry: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.locationtech.jts.geom.util")``.

    AffineTransformation: typing.Type[AffineTransformation]
    AffineTransformationBuilder: typing.Type[AffineTransformationBuilder]
    AffineTransformationFactory: typing.Type[AffineTransformationFactory]
    ComponentCoordinateExtracter: typing.Type[ComponentCoordinateExtracter]
    GeometryCollectionMapper: typing.Type[GeometryCollectionMapper]
    GeometryCombiner: typing.Type[GeometryCombiner]
    GeometryEditor: typing.Type[GeometryEditor]
    GeometryExtracter: typing.Type[GeometryExtracter]
    GeometryFixer: typing.Type[GeometryFixer]
    GeometryMapper: typing.Type[GeometryMapper]
    GeometryTransformer: typing.Type[GeometryTransformer]
    LineStringExtracter: typing.Type[LineStringExtracter]
    LinearComponentExtracter: typing.Type[LinearComponentExtracter]
    NoninvertibleTransformationException: typing.Type[NoninvertibleTransformationException]
    PointExtracter: typing.Type[PointExtracter]
    PolygonExtracter: typing.Type[PolygonExtracter]
    ShortCircuitedGeometryVisitor: typing.Type[ShortCircuitedGeometryVisitor]
    SineStarFactory: typing.Type[SineStarFactory]
