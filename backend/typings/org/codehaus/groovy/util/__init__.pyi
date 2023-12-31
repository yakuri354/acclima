
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import groovy.lang
import groovy.util
import java.io
import java.lang
import java.lang.ref
import java.net
import java.nio
import java.util
import java.util.concurrent.locks
import jpype
import org
import typing



_ArrayIterator__T = typing.TypeVar('_ArrayIterator__T')  # <T>
class ArrayIterator(java.util.Iterator[_ArrayIterator__T], typing.Generic[_ArrayIterator__T]):
    def __init__(self, tArray: typing.Union[typing.List[_ArrayIterator__T], jpype.JArray]): ...
    def hasNext(self) -> bool: ...
    def next(self) -> _ArrayIterator__T: ...
    def remove(self) -> None: ...

class CharSequenceReader(java.io.Reader, java.io.Serializable):
    def __init__(self, charSequence: typing.Union[java.lang.CharSequence, str]): ...
    def close(self) -> None: ...
    def mark(self, int: int) -> None: ...
    def markSupported(self) -> bool: ...
    @typing.overload
    def read(self, charArray: typing.Union[typing.List[str], jpype.JArray]) -> int: ...
    @typing.overload
    def read(self, charBuffer: java.nio.CharBuffer) -> int: ...
    @typing.overload
    def read(self) -> int: ...
    @typing.overload
    def read(self, charArray: typing.Union[typing.List[str], jpype.JArray], int: int, int2: int) -> int: ...
    def reset(self) -> None: ...
    def skip(self, long: int) -> int: ...
    def toString(self) -> str: ...

class ComplexKeyHashMap:
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, boolean: bool): ...
    @typing.overload
    def __init__(self, int: int): ...
    def clear(self) -> None: ...
    def getEntrySetIterator(self) -> 'ComplexKeyHashMap.EntryIterator': ...
    def getTable(self) -> typing.MutableSequence['ComplexKeyHashMap.Entry']: ...
    @staticmethod
    def hash(int: int) -> int: ...
    def init(self, int: int) -> None: ...
    def isEmpty(self) -> bool: ...
    def resize(self, int: int) -> None: ...
    def size(self) -> int: ...
    class Entry:
        hash: int = ...
        next: 'ComplexKeyHashMap.Entry' = ...
        value: typing.Any = ...
        def __init__(self): ...
        def getValue(self) -> typing.Any: ...
        def setValue(self, object: typing.Any) -> None: ...
    class EntryIterator:
        def hasNext(self) -> bool: ...
        def next(self) -> 'ComplexKeyHashMap.Entry': ...

class FastArray(java.lang.Cloneable, java.io.Serializable):
    size: int = ...
    EMPTY_LIST: typing.ClassVar['FastArray'] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray]): ...
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection, typing.Sequence, typing.Set]): ...
    def add(self, object: typing.Any) -> None: ...
    @typing.overload
    def addAll(self, objectArray: typing.Union[typing.List[typing.Any], jpype.JArray], int: int) -> None: ...
    @typing.overload
    def addAll(self, list: java.util.List) -> None: ...
    @typing.overload
    def addAll(self, fastArray: 'FastArray') -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> 'FastArray': ...
    def get(self, int: int) -> typing.Any: ...
    def getArray(self) -> typing.MutableSequence[typing.Any]: ...
    def isEmpty(self) -> bool: ...
    def remove(self, int: int) -> None: ...
    def set(self, int: int, object: typing.Any) -> None: ...
    def size(self) -> int: ...
    def toList(self) -> java.util.List: ...
    def toString(self) -> str: ...

class Finalizable:
    def finalizeReference(self) -> None: ...

class HashCodeHelper:
    def __init__(self): ...
    @staticmethod
    def initHash() -> int: ...
    @typing.overload
    @staticmethod
    def updateHash(int: int, boolean: bool) -> int: ...
    @typing.overload
    @staticmethod
    def updateHash(int: int, booleanArray: typing.Union[typing.List[bool], jpype.JArray]) -> int: ...
    @typing.overload
    @staticmethod
    def updateHash(int: int, byteArray: typing.Union[typing.List[int], jpype.JArray, bytes]) -> int: ...
    @typing.overload
    @staticmethod
    def updateHash(int: int, char: str) -> int: ...
    @typing.overload
    @staticmethod
    def updateHash(int: int, charArray: typing.Union[typing.List[str], jpype.JArray]) -> int: ...
    @typing.overload
    @staticmethod
    def updateHash(int: int, double: float) -> int: ...
    @typing.overload
    @staticmethod
    def updateHash(int: int, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> int: ...
    @typing.overload
    @staticmethod
    def updateHash(int: int, float: float) -> int: ...
    @typing.overload
    @staticmethod
    def updateHash(int: int, floatArray: typing.Union[typing.List[float], jpype.JArray]) -> int: ...
    @typing.overload
    @staticmethod
    def updateHash(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def updateHash(int: int, intArray: typing.Union[typing.List[int], jpype.JArray]) -> int: ...
    @typing.overload
    @staticmethod
    def updateHash(int: int, character: str) -> int: ...
    @typing.overload
    @staticmethod
    def updateHash(int: int, double: float) -> int: ...
    @typing.overload
    @staticmethod
    def updateHash(int: int, float: float) -> int: ...
    @typing.overload
    @staticmethod
    def updateHash(int: int, integer: int) -> int: ...
    @typing.overload
    @staticmethod
    def updateHash(int: int, long: int) -> int: ...
    @typing.overload
    @staticmethod
    def updateHash(int: int, object: typing.Any) -> int: ...
    @typing.overload
    @staticmethod
    def updateHash(int: int, long: int) -> int: ...
    @typing.overload
    @staticmethod
    def updateHash(int: int, longArray: typing.Union[typing.List[int], jpype.JArray]) -> int: ...
    @typing.overload
    @staticmethod
    def updateHash(int: int, shortArray: typing.Union[typing.List[int], jpype.JArray]) -> int: ...

_IteratorBufferedIterator__T = typing.TypeVar('_IteratorBufferedIterator__T')  # <T>
class IteratorBufferedIterator(groovy.util.BufferedIterator[_IteratorBufferedIterator__T], typing.Generic[_IteratorBufferedIterator__T]):
    def __init__(self, iterator: java.util.Iterator[_IteratorBufferedIterator__T]): ...
    def hasNext(self) -> bool: ...
    def head(self) -> _IteratorBufferedIterator__T: ...
    def next(self) -> _IteratorBufferedIterator__T: ...
    def remove(self) -> None: ...

_ListBufferedIterator__T = typing.TypeVar('_ListBufferedIterator__T')  # <T>
class ListBufferedIterator(groovy.util.BufferedIterator[_ListBufferedIterator__T], typing.Generic[_ListBufferedIterator__T]):
    def __init__(self, list: java.util.List[_ListBufferedIterator__T]): ...
    def hasNext(self) -> bool: ...
    def head(self) -> _ListBufferedIterator__T: ...
    def next(self) -> _ListBufferedIterator__T: ...
    def remove(self) -> None: ...

_ListHashMap__K = typing.TypeVar('_ListHashMap__K')  # <K>
_ListHashMap__V = typing.TypeVar('_ListHashMap__V')  # <V>
class ListHashMap(java.util.Map[_ListHashMap__K, _ListHashMap__V], typing.Generic[_ListHashMap__K, _ListHashMap__V]):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    def clear(self) -> None: ...
    def containsKey(self, object: typing.Any) -> bool: ...
    def containsValue(self, object: typing.Any) -> bool: ...
    def entrySet(self) -> java.util.Set[java.util.Map.Entry[_ListHashMap__K, _ListHashMap__V]]: ...
    def get(self, object: typing.Any) -> _ListHashMap__V: ...
    def isEmpty(self) -> bool: ...
    def keySet(self) -> java.util.Set[_ListHashMap__K]: ...
    def put(self, k: _ListHashMap__K, v: _ListHashMap__V) -> _ListHashMap__V: ...
    def putAll(self, map: typing.Union[java.util.Map[_ListHashMap__K, _ListHashMap__V], typing.Mapping[_ListHashMap__K, _ListHashMap__V]]) -> None: ...
    @typing.overload
    def remove(self, object: typing.Any, object2: typing.Any) -> bool: ...
    @typing.overload
    def remove(self, object: typing.Any) -> _ListHashMap__V: ...
    def size(self) -> int: ...
    def values(self) -> java.util.Collection[_ListHashMap__V]: ...

class LockableObject(java.util.concurrent.locks.AbstractQueuedSynchronizer):
    def __init__(self): ...
    def lock(self) -> None: ...
    def unlock(self) -> None: ...

_ManagedConcurrentLinkedQueue__T = typing.TypeVar('_ManagedConcurrentLinkedQueue__T')  # <T>
class ManagedConcurrentLinkedQueue(java.lang.Iterable[_ManagedConcurrentLinkedQueue__T], typing.Generic[_ManagedConcurrentLinkedQueue__T]):
    def __init__(self, referenceBundle: 'ReferenceBundle'): ...
    def add(self, t: _ManagedConcurrentLinkedQueue__T) -> None: ...
    def isEmpty(self) -> bool: ...
    def iterator(self) -> java.util.Iterator[_ManagedConcurrentLinkedQueue__T]: ...
    def toArray(self, tArray: typing.Union[typing.List[_ManagedConcurrentLinkedQueue__T], jpype.JArray]) -> typing.MutableSequence[_ManagedConcurrentLinkedQueue__T]: ...
    def values(self) -> java.util.List[_ManagedConcurrentLinkedQueue__T]: ...

_ManagedConcurrentValueMap__K = typing.TypeVar('_ManagedConcurrentValueMap__K')  # <K>
_ManagedConcurrentValueMap__V = typing.TypeVar('_ManagedConcurrentValueMap__V')  # <V>
class ManagedConcurrentValueMap(typing.Generic[_ManagedConcurrentValueMap__K, _ManagedConcurrentValueMap__V]):
    def __init__(self, referenceBundle: 'ReferenceBundle'): ...
    def get(self, k: _ManagedConcurrentValueMap__K) -> _ManagedConcurrentValueMap__V: ...
    def put(self, k: _ManagedConcurrentValueMap__K, v: _ManagedConcurrentValueMap__V) -> None: ...
    def setBundle(self, referenceBundle: 'ReferenceBundle') -> None: ...

_ManagedLinkedList__T = typing.TypeVar('_ManagedLinkedList__T')  # <T>
class ManagedLinkedList(typing.Generic[_ManagedLinkedList__T]):
    def __init__(self, referenceBundle: 'ReferenceBundle'): ...
    def add(self, t: _ManagedLinkedList__T) -> None: ...
    def isEmpty(self) -> bool: ...
    def iterator(self) -> java.util.Iterator[_ManagedLinkedList__T]: ...
    def toArray(self, tArray: typing.Union[typing.List[_ManagedLinkedList__T], jpype.JArray]) -> typing.MutableSequence[_ManagedLinkedList__T]: ...

_Reference__T = typing.TypeVar('_Reference__T')  # <T>
_Reference__V = typing.TypeVar('_Reference__V', bound=Finalizable)  # <V>
class Reference(typing.Generic[_Reference__T, _Reference__V]):
    def clear(self) -> None: ...
    def get(self) -> _Reference__T: ...
    def getHandler(self) -> _Reference__V: ...

class ReferenceBundle:
    def __init__(self, referenceManager: 'ReferenceManager', referenceType: 'ReferenceType'): ...
    @staticmethod
    def getHardBundle() -> 'ReferenceBundle': ...
    def getManager(self) -> 'ReferenceManager': ...
    @staticmethod
    def getPhantomBundle() -> 'ReferenceBundle': ...
    @staticmethod
    def getSoftBundle() -> 'ReferenceBundle': ...
    def getType(self) -> 'ReferenceType': ...
    @staticmethod
    def getWeakBundle() -> 'ReferenceBundle': ...

class ReferenceManager:
    def __init__(self, referenceQueue: java.lang.ref.ReferenceQueue): ...
    def afterReferenceCreation(self, reference: Reference) -> None: ...
    @staticmethod
    def createCallBackedManager(referenceQueue: java.lang.ref.ReferenceQueue) -> 'ReferenceManager': ...
    @staticmethod
    def createIdlingManager(referenceQueue: java.lang.ref.ReferenceQueue) -> 'ReferenceManager': ...
    @staticmethod
    def createThreadedManager(referenceQueue: java.lang.ref.ReferenceQueue) -> 'ReferenceManager': ...
    @staticmethod
    def createThresholdedIdlingManager(referenceQueue: java.lang.ref.ReferenceQueue, referenceManager: 'ReferenceManager', int: int) -> 'ReferenceManager': ...
    @staticmethod
    def getDefaultSoftBundle() -> ReferenceBundle: ...
    @staticmethod
    def getDefaultWeakBundle() -> ReferenceBundle: ...
    def removeStallEntries(self) -> None: ...
    def stopThread(self) -> None: ...
    def toString(self) -> str: ...

class ReferenceType(java.lang.Enum['ReferenceType']):
    SOFT: typing.ClassVar['ReferenceType'] = ...
    WEAK: typing.ClassVar['ReferenceType'] = ...
    PHANTOM: typing.ClassVar['ReferenceType'] = ...
    HARD: typing.ClassVar['ReferenceType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ReferenceType': ...
    @staticmethod
    def values() -> typing.MutableSequence['ReferenceType']: ...

class ReleaseInfo:
    def __init__(self): ...
    @staticmethod
    def getAllProperties() -> java.util.Properties: ...
    @staticmethod
    def getVersion() -> str: ...

class StringUtil(groovy.lang.GroovyObject):
    def __init__(self): ...
    @staticmethod
    def tr(string: str, string2: str, string3: str) -> str: ...

class URLStreams:
    @staticmethod
    def openUncachedStream(uRL: java.net.URL) -> java.io.InputStream: ...

_AbstractConcurrentMapBase__Entry__V = typing.TypeVar('_AbstractConcurrentMapBase__Entry__V')  # <V>
class AbstractConcurrentMapBase:
    def __init__(self, object: typing.Any): ...
    def fullSize(self) -> int: ...
    def segmentFor(self, int: int) -> 'AbstractConcurrentMapBase.Segment': ...
    def size(self) -> int: ...
    def values(self) -> java.util.Collection: ...
    class Entry(typing.Generic[_AbstractConcurrentMapBase__Entry__V]):
        def getHash(self) -> int: ...
        def getValue(self) -> _AbstractConcurrentMapBase__Entry__V: ...
        def isValid(self) -> bool: ...
        def setValue(self, v: _AbstractConcurrentMapBase__Entry__V) -> None: ...
    class Segment(LockableObject): ...

_LazyReference__T = typing.TypeVar('_LazyReference__T')  # <T>
class LazyReference(LockableObject, typing.Generic[_LazyReference__T]):
    def __init__(self, referenceBundle: ReferenceBundle): ...
    def clear(self) -> None: ...
    def get(self) -> _LazyReference__T: ...
    def initValue(self) -> _LazyReference__T: ...
    def toString(self) -> str: ...

_ManagedReference__T = typing.TypeVar('_ManagedReference__T')  # <T>
class ManagedReference(Finalizable, typing.Generic[_ManagedReference__T]):
    @typing.overload
    def __init__(self, referenceBundle: ReferenceBundle, t: _ManagedReference__T): ...
    @typing.overload
    def __init__(self, referenceType: ReferenceType, referenceManager: ReferenceManager, t: _ManagedReference__T): ...
    def clear(self) -> None: ...
    def finalizeReference(self) -> None: ...
    def get(self) -> _ManagedReference__T: ...

class SingleKeyHashMap(ComplexKeyHashMap):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, boolean: bool): ...
    def containsKey(self, string: str) -> bool: ...
    @staticmethod
    def copy(singleKeyHashMap: 'SingleKeyHashMap', singleKeyHashMap2: 'SingleKeyHashMap', copier: 'SingleKeyHashMap.Copier') -> 'SingleKeyHashMap': ...
    def get(self, object: typing.Any) -> typing.Any: ...
    def getOrPut(self, object: typing.Any) -> 'SingleKeyHashMap.Entry': ...
    def getOrPutEntry(self, entry: 'SingleKeyHashMap.Entry') -> 'SingleKeyHashMap.Entry': ...
    def put(self, object: typing.Any, object2: typing.Any) -> None: ...
    def putCopyOfUnexisting(self, entry: 'SingleKeyHashMap.Entry') -> 'SingleKeyHashMap.Entry': ...
    def remove(self, object: typing.Any) -> ComplexKeyHashMap.Entry: ...
    class Copier:
        def copy(self, object: typing.Any) -> typing.Any: ...
    class Entry(ComplexKeyHashMap.Entry):
        key: typing.Any = ...
        def __init__(self): ...
        def getKey(self) -> typing.Any: ...

class TripleKeyHashMap(ComplexKeyHashMap):
    def __init__(self): ...
    def checkEquals(self, entry: 'TripleKeyHashMap.Entry', object: typing.Any, object2: typing.Any, object3: typing.Any) -> bool: ...
    def createEntry(self) -> 'TripleKeyHashMap.Entry': ...
    def get(self, object: typing.Any, object2: typing.Any, object3: typing.Any) -> typing.Any: ...
    def getOrPut(self, object: typing.Any, object2: typing.Any, object3: typing.Any) -> 'TripleKeyHashMap.Entry': ...
    def remove(self, object: typing.Any, object2: typing.Any, object3: typing.Any) -> ComplexKeyHashMap.Entry: ...
    class Entry(ComplexKeyHashMap.Entry):
        key1: typing.Any = ...
        key2: typing.Any = ...
        key3: typing.Any = ...
        def __init__(self): ...

_AbstractConcurrentMap__Entry__K = typing.TypeVar('_AbstractConcurrentMap__Entry__K')  # <K>
_AbstractConcurrentMap__Entry__V = typing.TypeVar('_AbstractConcurrentMap__Entry__V')  # <V>
_AbstractConcurrentMap__Segment__K = typing.TypeVar('_AbstractConcurrentMap__Segment__K')  # <K>
_AbstractConcurrentMap__Segment__V = typing.TypeVar('_AbstractConcurrentMap__Segment__V')  # <V>
_AbstractConcurrentMap__K = typing.TypeVar('_AbstractConcurrentMap__K')  # <K>
_AbstractConcurrentMap__V = typing.TypeVar('_AbstractConcurrentMap__V')  # <V>
class AbstractConcurrentMap(AbstractConcurrentMapBase, typing.Generic[_AbstractConcurrentMap__K, _AbstractConcurrentMap__V]):
    def __init__(self, object: typing.Any): ...
    def get(self, k: _AbstractConcurrentMap__K) -> _AbstractConcurrentMap__V: ...
    def getOrPut(self, k: _AbstractConcurrentMap__K, v: _AbstractConcurrentMap__V) -> 'AbstractConcurrentMap.Entry'[_AbstractConcurrentMap__K, _AbstractConcurrentMap__V]: ...
    def put(self, k: _AbstractConcurrentMap__K, v: _AbstractConcurrentMap__V) -> None: ...
    def remove(self, k: _AbstractConcurrentMap__K) -> None: ...
    def segmentFor(self, int: int) -> 'AbstractConcurrentMap.Segment': ...
    class Entry(AbstractConcurrentMapBase.Entry[_AbstractConcurrentMap__Entry__V], typing.Generic[_AbstractConcurrentMap__Entry__K, _AbstractConcurrentMap__Entry__V]):
        def isEqual(self, k: _AbstractConcurrentMap__Entry__K, int: int) -> bool: ...
    class Segment(AbstractConcurrentMapBase.Segment, typing.Generic[_AbstractConcurrentMap__Segment__K, _AbstractConcurrentMap__Segment__V]):
        def get(self, k: _AbstractConcurrentMap__Segment__K, int: int) -> _AbstractConcurrentMap__Segment__V: ...
        def getOrPut(self, k: _AbstractConcurrentMap__Segment__K, int: int, v: _AbstractConcurrentMap__Segment__V) -> 'AbstractConcurrentMap.Entry'[_AbstractConcurrentMap__Segment__K, _AbstractConcurrentMap__Segment__V]: ...
        def put(self, k: _AbstractConcurrentMap__Segment__K, int: int, v: _AbstractConcurrentMap__Segment__V) -> 'AbstractConcurrentMap.Entry': ...
        def remove(self, k: _AbstractConcurrentMap__Segment__K, int: int) -> None: ...

_ManagedConcurrentMap__Entry__K = typing.TypeVar('_ManagedConcurrentMap__Entry__K')  # <K>
_ManagedConcurrentMap__Entry__V = typing.TypeVar('_ManagedConcurrentMap__Entry__V')  # <V>
_ManagedConcurrentMap__EntryWithValue__K = typing.TypeVar('_ManagedConcurrentMap__EntryWithValue__K')  # <K>
_ManagedConcurrentMap__EntryWithValue__V = typing.TypeVar('_ManagedConcurrentMap__EntryWithValue__V')  # <V>
_ManagedConcurrentMap__Segment__K = typing.TypeVar('_ManagedConcurrentMap__Segment__K')  # <K>
_ManagedConcurrentMap__Segment__V = typing.TypeVar('_ManagedConcurrentMap__Segment__V')  # <V>
_ManagedConcurrentMap__K = typing.TypeVar('_ManagedConcurrentMap__K')  # <K>
_ManagedConcurrentMap__V = typing.TypeVar('_ManagedConcurrentMap__V')  # <V>
class ManagedConcurrentMap(AbstractConcurrentMap[_ManagedConcurrentMap__K, _ManagedConcurrentMap__V], typing.Generic[_ManagedConcurrentMap__K, _ManagedConcurrentMap__V]):
    def __init__(self, referenceBundle: ReferenceBundle): ...
    class Entry(ManagedReference[_ManagedConcurrentMap__Entry__K], AbstractConcurrentMap.Entry[_ManagedConcurrentMap__Entry__K, _ManagedConcurrentMap__Entry__V], typing.Generic[_ManagedConcurrentMap__Entry__K, _ManagedConcurrentMap__Entry__V]):
        def __init__(self, referenceBundle: ReferenceBundle, segment: 'ManagedConcurrentMap.Segment', k: _ManagedConcurrentMap__Entry__K, int: int): ...
        def finalizeRef(self) -> None: ...
        def finalizeReference(self) -> None: ...
        def getHash(self) -> int: ...
        def getValue(self) -> _ManagedConcurrentMap__Entry__V: ...
        def isEqual(self, k: _ManagedConcurrentMap__Entry__K, int: int) -> bool: ...
        def isValid(self) -> bool: ...
        def setValue(self, v: _ManagedConcurrentMap__Entry__V) -> None: ...
    class EntryWithValue(org.codehaus.groovy.util.ManagedConcurrentMap.Entry[_ManagedConcurrentMap__EntryWithValue__K, _ManagedConcurrentMap__EntryWithValue__V], typing.Generic[_ManagedConcurrentMap__EntryWithValue__K, _ManagedConcurrentMap__EntryWithValue__V]):
        def __init__(self, referenceBundle: ReferenceBundle, segment: 'ManagedConcurrentMap.Segment', k: _ManagedConcurrentMap__EntryWithValue__K, int: int, v: _ManagedConcurrentMap__EntryWithValue__V): ...
        def finalizeReference(self) -> None: ...
        def getValue(self) -> _ManagedConcurrentMap__EntryWithValue__V: ...
        def setValue(self, v: _ManagedConcurrentMap__EntryWithValue__V) -> None: ...
    class Segment(AbstractConcurrentMap.Segment[_ManagedConcurrentMap__Segment__K, _ManagedConcurrentMap__Segment__V], typing.Generic[_ManagedConcurrentMap__Segment__K, _ManagedConcurrentMap__Segment__V]):
        def __init__(self, referenceBundle: ReferenceBundle, int: int): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.util")``.

    AbstractConcurrentMap: typing.Type[AbstractConcurrentMap]
    AbstractConcurrentMapBase: typing.Type[AbstractConcurrentMapBase]
    ArrayIterator: typing.Type[ArrayIterator]
    CharSequenceReader: typing.Type[CharSequenceReader]
    ComplexKeyHashMap: typing.Type[ComplexKeyHashMap]
    FastArray: typing.Type[FastArray]
    Finalizable: typing.Type[Finalizable]
    HashCodeHelper: typing.Type[HashCodeHelper]
    IteratorBufferedIterator: typing.Type[IteratorBufferedIterator]
    LazyReference: typing.Type[LazyReference]
    ListBufferedIterator: typing.Type[ListBufferedIterator]
    ListHashMap: typing.Type[ListHashMap]
    LockableObject: typing.Type[LockableObject]
    ManagedConcurrentLinkedQueue: typing.Type[ManagedConcurrentLinkedQueue]
    ManagedConcurrentMap: typing.Type[ManagedConcurrentMap]
    ManagedConcurrentValueMap: typing.Type[ManagedConcurrentValueMap]
    ManagedLinkedList: typing.Type[ManagedLinkedList]
    ManagedReference: typing.Type[ManagedReference]
    Reference: typing.Type[Reference]
    ReferenceBundle: typing.Type[ReferenceBundle]
    ReferenceManager: typing.Type[ReferenceManager]
    ReferenceType: typing.Type[ReferenceType]
    ReleaseInfo: typing.Type[ReleaseInfo]
    SingleKeyHashMap: typing.Type[SingleKeyHashMap]
    StringUtil: typing.Type[StringUtil]
    TripleKeyHashMap: typing.Type[TripleKeyHashMap]
    URLStreams: typing.Type[URLStreams]
