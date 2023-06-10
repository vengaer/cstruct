import functools
import struct

from typing import Any, Optional, TypeVar

from .exception import (
    AnnotationError,
    ArgumentError,
    BadStructFormat,
    InvalidAnnotation,
)
from .type import Type

_T = TypeVar("_T")


def _cstruct(cls: _T, packed: bool = False) -> _T:
    types = []
    for attr, anot in cls.__annotations__.items():
        if isinstance(anot, str):
            try:
                anot = getattr(Type, anot.replace(" ", "_"))
            except AttributeError as err:
                raise InvalidAnnotation(cls.__class__.__name__, attr) from err
        types.append(anot)

    pformat = ("=" if packed else "@") + "".join([e.format for e in types])

    def __init__(self, raw: Optional[bytes] = None, **kwargs: Any) -> None:
        if raw is not None and kwargs:
            raise ArgumentError("Must pass either only raw or kwargs, not both")

        if raw is not None:
            try:
                unpacked = struct.unpack(pformat, raw)
            except struct.error as err:
                raise BadStructFormat(pformat) from err

            if len(cls.__annotations__) != len(unpacked):
                raise AnnotationError(
                    cls.__class__.__name__, cls.__annotations__.keys()
                )
            for attr, value in zip(cls.__annotations__, unpacked):
                setattr(self, attr, value)
        else:
            for attr, ctype in zip(cls.__annotations__.keys(), types):
                setattr(cls, attr, kwargs.get(attr, ctype.value().value))

    cls.__init__ = __init__  # type: ignore[misc]
    return cls


cstruct = functools.partial(_cstruct, packed=False)
cstruct_packed = functools.partial(_cstruct, packed=True)
