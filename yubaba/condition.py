from functools import partial
from typing import Any, Callable, TypeVar

_T = TypeVar("_T")


class F(partial):
    pass


def print_if(condition: bool, s: str) -> None:
    print(s) if condition else None


class If:
    def __new__(cls, condition: bool, func: Callable) -> Any:  # type: ignore
        return func() if condition else None


class Nif:
    def __new__(cls, condition: bool, func: Callable) -> Any:  # type: ignore
        return func() if not condition else None
