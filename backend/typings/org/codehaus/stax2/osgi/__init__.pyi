
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.codehaus.stax2
import org.codehaus.stax2.validation
import typing



class Stax2InputFactoryProvider:
    OSGI_SVC_PROP_IMPL_NAME: typing.ClassVar[str] = ...
    OSGI_SVC_PROP_IMPL_VERSION: typing.ClassVar[str] = ...
    def createInputFactory(self) -> org.codehaus.stax2.XMLInputFactory2: ...

class Stax2OutputFactoryProvider:
    OSGI_SVC_PROP_IMPL_NAME: typing.ClassVar[str] = ...
    OSGI_SVC_PROP_IMPL_VERSION: typing.ClassVar[str] = ...
    def createOutputFactory(self) -> org.codehaus.stax2.XMLOutputFactory2: ...

class Stax2ValidationSchemaFactoryProvider:
    OSGI_SVC_PROP_IMPL_NAME: typing.ClassVar[str] = ...
    OSGI_SVC_PROP_IMPL_VERSION: typing.ClassVar[str] = ...
    OSGI_SVC_PROP_SCHEMA_TYPE: typing.ClassVar[str] = ...
    def createValidationSchemaFactory(self) -> org.codehaus.stax2.validation.XMLValidationSchemaFactory: ...
    def getSchemaType(self) -> str: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.stax2.osgi")``.

    Stax2InputFactoryProvider: typing.Type[Stax2InputFactoryProvider]
    Stax2OutputFactoryProvider: typing.Type[Stax2OutputFactoryProvider]
    Stax2ValidationSchemaFactoryProvider: typing.Type[Stax2ValidationSchemaFactoryProvider]
