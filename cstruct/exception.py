from typing import Iterable, Union

from .type import Type


class CStructError(Exception):
    ...


class InvalidAnnotation(CStructError):
    def __init__(self, cls: str, annotation: Union[str, Type]) -> None:
        super().__init__(f"Invalid annotation {annotation} for {cls}")
        self._cls = cls
        self._annotation = annotation

    @property
    def cls(self) -> str:
        return self._cls

    @property
    def annotation(self) -> Union[str, Type]:
        return self._annotation


class AnnotationError(CStructError):
    def __init__(self, cls: str, annotations: Iterable[str]) -> None:
        super().__init__(f"Invalid annotations for {cls}: {annotations}")
        self._cls = cls
        self._annotations = annotations

    @property
    def cls(self) -> str:
        return self._cls

    @property
    def annotations(self) -> Iterable[str]:
        return self._annotations


class ArgumentError(CStructError):
    ...


class BadStructFormat(CStructError):
    def __init__(self, fmt: str) -> None:
        super().__init__(f'Bad struct format "{fmt}"')
