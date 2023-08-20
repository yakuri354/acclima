
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import jpype
import typing



class CMMException(java.lang.RuntimeException):
    def __init__(self, string: str): ...

class ColorSpace(java.io.Serializable):
    TYPE_XYZ: typing.ClassVar[int] = ...
    TYPE_Lab: typing.ClassVar[int] = ...
    TYPE_Luv: typing.ClassVar[int] = ...
    TYPE_YCbCr: typing.ClassVar[int] = ...
    TYPE_Yxy: typing.ClassVar[int] = ...
    TYPE_RGB: typing.ClassVar[int] = ...
    TYPE_GRAY: typing.ClassVar[int] = ...
    TYPE_HSV: typing.ClassVar[int] = ...
    TYPE_HLS: typing.ClassVar[int] = ...
    TYPE_CMYK: typing.ClassVar[int] = ...
    TYPE_CMY: typing.ClassVar[int] = ...
    TYPE_2CLR: typing.ClassVar[int] = ...
    TYPE_3CLR: typing.ClassVar[int] = ...
    TYPE_4CLR: typing.ClassVar[int] = ...
    TYPE_5CLR: typing.ClassVar[int] = ...
    TYPE_6CLR: typing.ClassVar[int] = ...
    TYPE_7CLR: typing.ClassVar[int] = ...
    TYPE_8CLR: typing.ClassVar[int] = ...
    TYPE_9CLR: typing.ClassVar[int] = ...
    TYPE_ACLR: typing.ClassVar[int] = ...
    TYPE_BCLR: typing.ClassVar[int] = ...
    TYPE_CCLR: typing.ClassVar[int] = ...
    TYPE_DCLR: typing.ClassVar[int] = ...
    TYPE_ECLR: typing.ClassVar[int] = ...
    TYPE_FCLR: typing.ClassVar[int] = ...
    CS_sRGB: typing.ClassVar[int] = ...
    CS_LINEAR_RGB: typing.ClassVar[int] = ...
    CS_CIEXYZ: typing.ClassVar[int] = ...
    CS_PYCC: typing.ClassVar[int] = ...
    CS_GRAY: typing.ClassVar[int] = ...
    def fromCIEXYZ(self, floatArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...
    def fromRGB(self, floatArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...
    @staticmethod
    def getInstance(int: int) -> 'ColorSpace': ...
    def getMaxValue(self, int: int) -> float: ...
    def getMinValue(self, int: int) -> float: ...
    def getName(self, int: int) -> str: ...
    def getNumComponents(self) -> int: ...
    def getType(self) -> int: ...
    def isCS_sRGB(self) -> bool: ...
    def toCIEXYZ(self, floatArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...
    def toRGB(self, floatArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...

class ICC_Profile(java.io.Serializable):
    CLASS_INPUT: typing.ClassVar[int] = ...
    CLASS_DISPLAY: typing.ClassVar[int] = ...
    CLASS_OUTPUT: typing.ClassVar[int] = ...
    CLASS_DEVICELINK: typing.ClassVar[int] = ...
    CLASS_COLORSPACECONVERSION: typing.ClassVar[int] = ...
    CLASS_ABSTRACT: typing.ClassVar[int] = ...
    CLASS_NAMEDCOLOR: typing.ClassVar[int] = ...
    icSigXYZData: typing.ClassVar[int] = ...
    icSigLabData: typing.ClassVar[int] = ...
    icSigLuvData: typing.ClassVar[int] = ...
    icSigYCbCrData: typing.ClassVar[int] = ...
    icSigYxyData: typing.ClassVar[int] = ...
    icSigRgbData: typing.ClassVar[int] = ...
    icSigGrayData: typing.ClassVar[int] = ...
    icSigHsvData: typing.ClassVar[int] = ...
    icSigHlsData: typing.ClassVar[int] = ...
    icSigCmykData: typing.ClassVar[int] = ...
    icSigCmyData: typing.ClassVar[int] = ...
    icSigSpace2CLR: typing.ClassVar[int] = ...
    icSigSpace3CLR: typing.ClassVar[int] = ...
    icSigSpace4CLR: typing.ClassVar[int] = ...
    icSigSpace5CLR: typing.ClassVar[int] = ...
    icSigSpace6CLR: typing.ClassVar[int] = ...
    icSigSpace7CLR: typing.ClassVar[int] = ...
    icSigSpace8CLR: typing.ClassVar[int] = ...
    icSigSpace9CLR: typing.ClassVar[int] = ...
    icSigSpaceACLR: typing.ClassVar[int] = ...
    icSigSpaceBCLR: typing.ClassVar[int] = ...
    icSigSpaceCCLR: typing.ClassVar[int] = ...
    icSigSpaceDCLR: typing.ClassVar[int] = ...
    icSigSpaceECLR: typing.ClassVar[int] = ...
    icSigSpaceFCLR: typing.ClassVar[int] = ...
    icSigInputClass: typing.ClassVar[int] = ...
    icSigDisplayClass: typing.ClassVar[int] = ...
    icSigOutputClass: typing.ClassVar[int] = ...
    icSigLinkClass: typing.ClassVar[int] = ...
    icSigAbstractClass: typing.ClassVar[int] = ...
    icSigColorSpaceClass: typing.ClassVar[int] = ...
    icSigNamedColorClass: typing.ClassVar[int] = ...
    icPerceptual: typing.ClassVar[int] = ...
    icRelativeColorimetric: typing.ClassVar[int] = ...
    icMediaRelativeColorimetric: typing.ClassVar[int] = ...
    icSaturation: typing.ClassVar[int] = ...
    icAbsoluteColorimetric: typing.ClassVar[int] = ...
    icICCAbsoluteColorimetric: typing.ClassVar[int] = ...
    icSigHead: typing.ClassVar[int] = ...
    icSigAToB0Tag: typing.ClassVar[int] = ...
    icSigAToB1Tag: typing.ClassVar[int] = ...
    icSigAToB2Tag: typing.ClassVar[int] = ...
    icSigBlueColorantTag: typing.ClassVar[int] = ...
    icSigBlueMatrixColumnTag: typing.ClassVar[int] = ...
    icSigBlueTRCTag: typing.ClassVar[int] = ...
    icSigBToA0Tag: typing.ClassVar[int] = ...
    icSigBToA1Tag: typing.ClassVar[int] = ...
    icSigBToA2Tag: typing.ClassVar[int] = ...
    icSigCalibrationDateTimeTag: typing.ClassVar[int] = ...
    icSigCharTargetTag: typing.ClassVar[int] = ...
    icSigCopyrightTag: typing.ClassVar[int] = ...
    icSigCrdInfoTag: typing.ClassVar[int] = ...
    icSigDeviceMfgDescTag: typing.ClassVar[int] = ...
    icSigDeviceModelDescTag: typing.ClassVar[int] = ...
    icSigDeviceSettingsTag: typing.ClassVar[int] = ...
    icSigGamutTag: typing.ClassVar[int] = ...
    icSigGrayTRCTag: typing.ClassVar[int] = ...
    icSigGreenColorantTag: typing.ClassVar[int] = ...
    icSigGreenMatrixColumnTag: typing.ClassVar[int] = ...
    icSigGreenTRCTag: typing.ClassVar[int] = ...
    icSigLuminanceTag: typing.ClassVar[int] = ...
    icSigMeasurementTag: typing.ClassVar[int] = ...
    icSigMediaBlackPointTag: typing.ClassVar[int] = ...
    icSigMediaWhitePointTag: typing.ClassVar[int] = ...
    icSigNamedColor2Tag: typing.ClassVar[int] = ...
    icSigOutputResponseTag: typing.ClassVar[int] = ...
    icSigPreview0Tag: typing.ClassVar[int] = ...
    icSigPreview1Tag: typing.ClassVar[int] = ...
    icSigPreview2Tag: typing.ClassVar[int] = ...
    icSigProfileDescriptionTag: typing.ClassVar[int] = ...
    icSigProfileSequenceDescTag: typing.ClassVar[int] = ...
    icSigPs2CRD0Tag: typing.ClassVar[int] = ...
    icSigPs2CRD1Tag: typing.ClassVar[int] = ...
    icSigPs2CRD2Tag: typing.ClassVar[int] = ...
    icSigPs2CRD3Tag: typing.ClassVar[int] = ...
    icSigPs2CSATag: typing.ClassVar[int] = ...
    icSigPs2RenderingIntentTag: typing.ClassVar[int] = ...
    icSigRedColorantTag: typing.ClassVar[int] = ...
    icSigRedMatrixColumnTag: typing.ClassVar[int] = ...
    icSigRedTRCTag: typing.ClassVar[int] = ...
    icSigScreeningDescTag: typing.ClassVar[int] = ...
    icSigScreeningTag: typing.ClassVar[int] = ...
    icSigTechnologyTag: typing.ClassVar[int] = ...
    icSigUcrBgTag: typing.ClassVar[int] = ...
    icSigViewingCondDescTag: typing.ClassVar[int] = ...
    icSigViewingConditionsTag: typing.ClassVar[int] = ...
    icSigChromaticityTag: typing.ClassVar[int] = ...
    icSigChromaticAdaptationTag: typing.ClassVar[int] = ...
    icSigColorantOrderTag: typing.ClassVar[int] = ...
    icSigColorantTableTag: typing.ClassVar[int] = ...
    icHdrSize: typing.ClassVar[int] = ...
    icHdrCmmId: typing.ClassVar[int] = ...
    icHdrVersion: typing.ClassVar[int] = ...
    icHdrDeviceClass: typing.ClassVar[int] = ...
    icHdrColorSpace: typing.ClassVar[int] = ...
    icHdrPcs: typing.ClassVar[int] = ...
    icHdrDate: typing.ClassVar[int] = ...
    icHdrMagic: typing.ClassVar[int] = ...
    icHdrPlatform: typing.ClassVar[int] = ...
    icHdrFlags: typing.ClassVar[int] = ...
    icHdrManufacturer: typing.ClassVar[int] = ...
    icHdrModel: typing.ClassVar[int] = ...
    icHdrAttributes: typing.ClassVar[int] = ...
    icHdrRenderingIntent: typing.ClassVar[int] = ...
    icHdrIlluminant: typing.ClassVar[int] = ...
    icHdrCreator: typing.ClassVar[int] = ...
    icHdrProfileID: typing.ClassVar[int] = ...
    icTagType: typing.ClassVar[int] = ...
    icTagReserved: typing.ClassVar[int] = ...
    icCurveCount: typing.ClassVar[int] = ...
    icCurveData: typing.ClassVar[int] = ...
    icXYZNumberX: typing.ClassVar[int] = ...
    def getColorSpaceType(self) -> int: ...
    @typing.overload
    def getData(self) -> typing.MutableSequence[int]: ...
    @typing.overload
    def getData(self, int: int) -> typing.MutableSequence[int]: ...
    @typing.overload
    @staticmethod
    def getInstance(byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> 'ICC_Profile': ...
    @typing.overload
    @staticmethod
    def getInstance(int: int) -> 'ICC_Profile': ...
    @typing.overload
    @staticmethod
    def getInstance(inputStream: java.io.InputStream) -> 'ICC_Profile': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str) -> 'ICC_Profile': ...
    def getMajorVersion(self) -> int: ...
    def getMinorVersion(self) -> int: ...
    def getNumComponents(self) -> int: ...
    def getPCSType(self) -> int: ...
    def getProfileClass(self) -> int: ...
    def setData(self, int: int, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> None: ...
    @typing.overload
    def write(self, outputStream: java.io.OutputStream) -> None: ...
    @typing.overload
    def write(self, string: str) -> None: ...

class ProfileDataException(java.lang.RuntimeException):
    def __init__(self, string: str): ...

class ICC_ColorSpace(ColorSpace):
    def __init__(self, iCC_Profile: ICC_Profile): ...
    def fromCIEXYZ(self, floatArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...
    def fromRGB(self, floatArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...
    def getMaxValue(self, int: int) -> float: ...
    def getMinValue(self, int: int) -> float: ...
    def getProfile(self) -> ICC_Profile: ...
    def toCIEXYZ(self, floatArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...
    def toRGB(self, floatArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...

class ICC_ProfileGray(ICC_Profile):
    def getGamma(self) -> float: ...
    def getMediaWhitePoint(self) -> typing.MutableSequence[float]: ...
    def getTRC(self) -> typing.MutableSequence[int]: ...

class ICC_ProfileRGB(ICC_Profile):
    REDCOMPONENT: typing.ClassVar[int] = ...
    GREENCOMPONENT: typing.ClassVar[int] = ...
    BLUECOMPONENT: typing.ClassVar[int] = ...
    def getGamma(self, int: int) -> float: ...
    def getMatrix(self) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    def getMediaWhitePoint(self) -> typing.MutableSequence[float]: ...
    def getTRC(self, int: int) -> typing.MutableSequence[int]: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.awt.color")``.

    CMMException: typing.Type[CMMException]
    ColorSpace: typing.Type[ColorSpace]
    ICC_ColorSpace: typing.Type[ICC_ColorSpace]
    ICC_Profile: typing.Type[ICC_Profile]
    ICC_ProfileGray: typing.Type[ICC_ProfileGray]
    ICC_ProfileRGB: typing.Type[ICC_ProfileRGB]
    ProfileDataException: typing.Type[ProfileDataException]