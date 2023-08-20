
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import javax.xml.stream
import javax.xml.stream.events
import org.codehaus.stax2
import typing



class DTD2(javax.xml.stream.events.DTD):
    def getInternalSubset(self) -> str: ...
    def getPublicId(self) -> str: ...
    def getRootName(self) -> str: ...
    def getSystemId(self) -> str: ...

class NotationDeclaration2(javax.xml.stream.events.NotationDeclaration):
    def getBaseURI(self) -> str: ...

class XMLEvent2(javax.xml.stream.events.XMLEvent):
    def writeUsing(self, xMLStreamWriter2: org.codehaus.stax2.XMLStreamWriter2) -> None: ...

class XMLEventFactory2(javax.xml.stream.XMLEventFactory):
    @typing.overload
    def createDTD(self, string: str) -> javax.xml.stream.events.DTD: ...
    @typing.overload
    def createDTD(self, string: str, string2: str, string3: str, string4: str) -> DTD2: ...
    @typing.overload
    def createDTD(self, string: str, string2: str, string3: str, string4: str, object: typing.Any) -> DTD2: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.stax2.evt")``.

    DTD2: typing.Type[DTD2]
    NotationDeclaration2: typing.Type[NotationDeclaration2]
    XMLEvent2: typing.Type[XMLEvent2]
    XMLEventFactory2: typing.Type[XMLEventFactory2]
