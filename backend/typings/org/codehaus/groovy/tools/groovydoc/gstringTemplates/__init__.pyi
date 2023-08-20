
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import typing



class GroovyDocTemplateInfo:
    DEFAULT_DOC_TEMPLATES: typing.ClassVar[typing.MutableSequence[str]] = ...
    DEFAULT_PACKAGE_TEMPLATES: typing.ClassVar[typing.MutableSequence[str]] = ...
    DEFAULT_CLASS_TEMPLATES: typing.ClassVar[typing.MutableSequence[str]] = ...
    def __init__(self): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.codehaus.groovy.tools.groovydoc.gstringTemplates")``.

    GroovyDocTemplateInfo: typing.Type[GroovyDocTemplateInfo]
