
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.math
import java.util
import javax.xml.namespace
import jpype
import org
import org.codehaus.stax2.typed
import typing



class AsciiValueEncoder:
    def bufferNeedsFlush(self, int: int) -> bool: ...
    @typing.overload
    def encodeMore(self, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes], int: int, int2: int) -> int: ...
    @typing.overload
    def encodeMore(self, charArray: typing.Union[typing.List[str], jpype.JArray], int: int, int2: int) -> int: ...
    def isCompleted(self) -> bool: ...

class NumberUtil:
    MAX_INT_CLEN: typing.ClassVar[int] = ...
    MAX_LONG_CLEN: typing.ClassVar[int] = ...
    MAX_DOUBLE_CLEN: typing.ClassVar[int] = ...
    MAX_FLOAT_CLEN: typing.ClassVar[int] = ...
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def writeDouble(double: float, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes], int: int) -> int: ...
    @typing.overload
    @staticmethod
    def writeDouble(double: float, charArray: typing.Union[typing.List[str], jpype.JArray], int: int) -> int: ...
    @typing.overload
    @staticmethod
    def writeFloat(float: float, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes], int: int) -> int: ...
    @typing.overload
    @staticmethod
    def writeFloat(float: float, charArray: typing.Union[typing.List[str], jpype.JArray], int: int) -> int: ...
    @typing.overload
    @staticmethod
    def writeInt(int: int, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes], int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def writeInt(int: int, charArray: typing.Union[typing.List[str], jpype.JArray], int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def writeLong(long: int, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes], int: int) -> int: ...
    @typing.overload
    @staticmethod
    def writeLong(long: int, charArray: typing.Union[typing.List[str], jpype.JArray], int: int) -> int: ...

class SimpleValueEncoder:
    def __init__(self): ...
    @typing.overload
    def encodeAsString(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> str: ...
    @typing.overload
    def encodeAsString(self, floatArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> str: ...
    @typing.overload
    def encodeAsString(self, intArray: typing.Union[typing.List[int], jpype.JArray], int2: int, int3: int) -> str: ...
    @typing.overload
    def encodeAsString(self, longArray: typing.Union[typing.List[int], jpype.JArray], int: int, int2: int) -> str: ...
    @typing.overload
    def encodeAsString(self, base64Variant: org.codehaus.stax2.typed.Base64Variant, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes], int: int, int2: int) -> str: ...

class ValueEncoderFactory:
    def __init__(self): ...
    @typing.overload
    def getEncoder(self, base64Variant: org.codehaus.stax2.typed.Base64Variant, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes], int: int, int2: int) -> 'ValueEncoderFactory.Base64Encoder': ...
    @typing.overload
    def getEncoder(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> 'ValueEncoderFactory.DoubleArrayEncoder': ...
    @typing.overload
    def getEncoder(self, double: float) -> 'ValueEncoderFactory.DoubleEncoder': ...
    @typing.overload
    def getEncoder(self, floatArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> 'ValueEncoderFactory.FloatArrayEncoder': ...
    @typing.overload
    def getEncoder(self, float: float) -> 'ValueEncoderFactory.FloatEncoder': ...
    @typing.overload
    def getEncoder(self, intArray: typing.Union[typing.List[int], jpype.JArray], int2: int, int3: int) -> 'ValueEncoderFactory.IntArrayEncoder': ...
    @typing.overload
    def getEncoder(self, int: int) -> 'ValueEncoderFactory.IntEncoder': ...
    @typing.overload
    def getEncoder(self, longArray: typing.Union[typing.List[int], jpype.JArray], int: int, int2: int) -> 'ValueEncoderFactory.LongArrayEncoder': ...
    @typing.overload
    def getEncoder(self, long: int) -> 'ValueEncoderFactory.LongEncoder': ...
    @typing.overload
    def getEncoder(self, boolean: bool) -> 'ValueEncoderFactory.ScalarEncoder': ...
    def getScalarEncoder(self, string: str) -> 'ValueEncoderFactory.ScalarEncoder': ...
    class Base64Encoder: ...
    class DoubleArrayEncoder: ...
    class DoubleEncoder: ...
    class FloatArrayEncoder: ...
    class FloatEncoder: ...
    class IntArrayEncoder: ...
    class IntEncoder: ...
    class LongArrayEncoder: ...
    class LongEncoder: ...
    class ScalarEncoder: ...

class CharArrayBase64Decoder(org.codehaus.stax2.ri.typed.Base64DecoderBase):
    def __init__(self): ...
    def decode(self, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes], int: int, int2: int) -> int: ...
    def init(self, base64Variant: org.codehaus.stax2.typed.Base64Variant, boolean: bool, charArray: typing.Union[typing.List[str], jpype.JArray], int: int, int2: int, list: java.util.List[typing.Union[typing.List[str], jpype.JArray]]) -> None: ...

class StringBase64Decoder(org.codehaus.stax2.ri.typed.Base64DecoderBase):
    def __init__(self): ...
    def decode(self, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes], int: int, int2: int) -> int: ...
    def init(self, base64Variant: org.codehaus.stax2.typed.Base64Variant, boolean: bool, string: str) -> None: ...

class ValueDecoderFactory:
    def __init__(self): ...
    def getBooleanDecoder(self) -> 'ValueDecoderFactory.BooleanDecoder': ...
    def getDecimalDecoder(self) -> 'ValueDecoderFactory.DecimalDecoder': ...
    @typing.overload
    def getDoubleArrayDecoder(self) -> 'ValueDecoderFactory.DoubleArrayDecoder': ...
    @typing.overload
    def getDoubleArrayDecoder(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> 'ValueDecoderFactory.DoubleArrayDecoder': ...
    def getDoubleDecoder(self) -> 'ValueDecoderFactory.DoubleDecoder': ...
    @typing.overload
    def getFloatArrayDecoder(self) -> 'ValueDecoderFactory.FloatArrayDecoder': ...
    @typing.overload
    def getFloatArrayDecoder(self, floatArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int) -> 'ValueDecoderFactory.FloatArrayDecoder': ...
    def getFloatDecoder(self) -> 'ValueDecoderFactory.FloatDecoder': ...
    @typing.overload
    def getIntArrayDecoder(self) -> 'ValueDecoderFactory.IntArrayDecoder': ...
    @typing.overload
    def getIntArrayDecoder(self, intArray: typing.Union[typing.List[int], jpype.JArray], int2: int, int3: int) -> 'ValueDecoderFactory.IntArrayDecoder': ...
    def getIntDecoder(self) -> 'ValueDecoderFactory.IntDecoder': ...
    def getIntegerDecoder(self) -> 'ValueDecoderFactory.IntegerDecoder': ...
    @typing.overload
    def getLongArrayDecoder(self) -> 'ValueDecoderFactory.LongArrayDecoder': ...
    @typing.overload
    def getLongArrayDecoder(self, longArray: typing.Union[typing.List[int], jpype.JArray], int: int, int2: int) -> 'ValueDecoderFactory.LongArrayDecoder': ...
    def getLongDecoder(self) -> 'ValueDecoderFactory.LongDecoder': ...
    def getQNameDecoder(self, namespaceContext: javax.xml.namespace.NamespaceContext) -> 'ValueDecoderFactory.QNameDecoder': ...
    class BaseArrayDecoder(org.codehaus.stax2.typed.TypedArrayDecoder):
        def expand(self) -> None: ...
        def getCount(self) -> int: ...
        def hasRoom(self) -> bool: ...
    class BooleanDecoder(org.codehaus.stax2.ri.typed.ValueDecoderFactory.DecoderBase):
        def __init__(self): ...
        @typing.overload
        def decode(self, charArray: typing.Union[typing.List[str], jpype.JArray], int: int, int2: int) -> None: ...
        @typing.overload
        def decode(self, string: str) -> None: ...
        def getType(self) -> str: ...
        def getValue(self) -> bool: ...
    class DecimalDecoder(org.codehaus.stax2.ri.typed.ValueDecoderFactory.DecoderBase):
        def __init__(self): ...
        @typing.overload
        def decode(self, charArray: typing.Union[typing.List[str], jpype.JArray], int: int, int2: int) -> None: ...
        @typing.overload
        def decode(self, string: str) -> None: ...
        def getType(self) -> str: ...
        def getValue(self) -> java.math.BigDecimal: ...
    class DecoderBase(org.codehaus.stax2.typed.TypedValueDecoder):
        def getType(self) -> str: ...
        def handleEmptyValue(self) -> None: ...
    class DoubleArrayDecoder(org.codehaus.stax2.ri.typed.ValueDecoderFactory.BaseArrayDecoder):
        @typing.overload
        def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int, doubleDecoder: 'ValueDecoderFactory.DoubleDecoder'): ...
        @typing.overload
        def __init__(self, doubleDecoder: 'ValueDecoderFactory.DoubleDecoder'): ...
        @typing.overload
        def decodeValue(self, charArray: typing.Union[typing.List[str], jpype.JArray], int: int, int2: int) -> bool: ...
        @typing.overload
        def decodeValue(self, string: str) -> bool: ...
        def expand(self) -> None: ...
        def getValues(self) -> typing.MutableSequence[float]: ...
    class DoubleDecoder(org.codehaus.stax2.ri.typed.ValueDecoderFactory.DecoderBase):
        def __init__(self): ...
        @typing.overload
        def decode(self, charArray: typing.Union[typing.List[str], jpype.JArray], int: int, int2: int) -> None: ...
        @typing.overload
        def decode(self, string: str) -> None: ...
        def getType(self) -> str: ...
        def getValue(self) -> float: ...
    class FloatArrayDecoder(org.codehaus.stax2.ri.typed.ValueDecoderFactory.BaseArrayDecoder):
        @typing.overload
        def __init__(self, floatArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int, floatDecoder: 'ValueDecoderFactory.FloatDecoder'): ...
        @typing.overload
        def __init__(self, floatDecoder: 'ValueDecoderFactory.FloatDecoder'): ...
        @typing.overload
        def decodeValue(self, charArray: typing.Union[typing.List[str], jpype.JArray], int: int, int2: int) -> bool: ...
        @typing.overload
        def decodeValue(self, string: str) -> bool: ...
        def expand(self) -> None: ...
        def getValues(self) -> typing.MutableSequence[float]: ...
    class FloatDecoder(org.codehaus.stax2.ri.typed.ValueDecoderFactory.DecoderBase):
        def __init__(self): ...
        @typing.overload
        def decode(self, charArray: typing.Union[typing.List[str], jpype.JArray], int: int, int2: int) -> None: ...
        @typing.overload
        def decode(self, string: str) -> None: ...
        def getType(self) -> str: ...
        def getValue(self) -> float: ...
    class IntArrayDecoder(org.codehaus.stax2.ri.typed.ValueDecoderFactory.BaseArrayDecoder):
        @typing.overload
        def __init__(self, intArray: typing.Union[typing.List[int], jpype.JArray], int2: int, int3: int, intDecoder: 'ValueDecoderFactory.IntDecoder'): ...
        @typing.overload
        def __init__(self, intDecoder: 'ValueDecoderFactory.IntDecoder'): ...
        @typing.overload
        def decodeValue(self, charArray: typing.Union[typing.List[str], jpype.JArray], int: int, int2: int) -> bool: ...
        @typing.overload
        def decodeValue(self, string: str) -> bool: ...
        def expand(self) -> None: ...
        def getValues(self) -> typing.MutableSequence[int]: ...
    class IntDecoder(org.codehaus.stax2.ri.typed.ValueDecoderFactory.DecoderBase):
        def __init__(self): ...
        @typing.overload
        def decode(self, charArray: typing.Union[typing.List[str], jpype.JArray], int: int, int2: int) -> None: ...
        @typing.overload
        def decode(self, string: str) -> None: ...
        def getType(self) -> str: ...
        def getValue(self) -> int: ...
    class IntegerDecoder(org.codehaus.stax2.ri.typed.ValueDecoderFactory.DecoderBase):
        def __init__(self): ...
        @typing.overload
        def decode(self, charArray: typing.Union[typing.List[str], jpype.JArray], int: int, int2: int) -> None: ...
        @typing.overload
        def decode(self, string: str) -> None: ...
        def getType(self) -> str: ...
        def getValue(self) -> java.math.BigInteger: ...
    class LongArrayDecoder(org.codehaus.stax2.ri.typed.ValueDecoderFactory.BaseArrayDecoder):
        @typing.overload
        def __init__(self, longArray: typing.Union[typing.List[int], jpype.JArray], int: int, int2: int, longDecoder: 'ValueDecoderFactory.LongDecoder'): ...
        @typing.overload
        def __init__(self, longDecoder: 'ValueDecoderFactory.LongDecoder'): ...
        @typing.overload
        def decodeValue(self, charArray: typing.Union[typing.List[str], jpype.JArray], int: int, int2: int) -> bool: ...
        @typing.overload
        def decodeValue(self, string: str) -> bool: ...
        def expand(self) -> None: ...
        def getValues(self) -> typing.MutableSequence[int]: ...
    class LongDecoder(org.codehaus.stax2.ri.typed.ValueDecoderFactory.DecoderBase):
        def __init__(self): ...
        @typing.overload
        def decode(self, charArray: typing.Union[typing.List[str], jpype.JArray], int: int, int2: int) -> None: ...
        @typing.overload
        def decode(self, string: str) -> None: ...
        def getType(self) -> str: ...
        def getValue(self) -> int: ...
    class QNameDecoder(org.codehaus.stax2.ri.typed.ValueDecoderFactory.DecoderBase):
        def __init__(self, namespaceContext: javax.xml.namespace.NamespaceContext): ...
        @typing.overload
        def decode(self, charArray: typing.Union[typing.List[str], jpype.JArray], int: int, int2: int) -> None: ...
        @typing.overload
        def decode(self, string: str) -> None: ...
        def getType(self) -> str: ...
        def getValue(self) -> javax.xml.namespace.QName: ...

class Base64DecoderBase: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.stax2.ri.typed")``.

    AsciiValueEncoder: typing.Type[AsciiValueEncoder]
    Base64DecoderBase: typing.Type[Base64DecoderBase]
    CharArrayBase64Decoder: typing.Type[CharArrayBase64Decoder]
    NumberUtil: typing.Type[NumberUtil]
    SimpleValueEncoder: typing.Type[SimpleValueEncoder]
    StringBase64Decoder: typing.Type[StringBase64Decoder]
    ValueDecoderFactory: typing.Type[ValueDecoderFactory]
    ValueEncoderFactory: typing.Type[ValueEncoderFactory]
