from typing import Sequence


class And:
    def __new__(cls, itr: Sequence) -> bool:  # type: ignore
        return False if False in itr else True


class Or:
    def __new__(cls, itr: Sequence) -> bool:  # type: ignore
        return True if True in itr else False


class Xor:
    def __new__(cls, itr: Sequence) -> bool:  # type: ignore
        return True if itr.count(True) % 2 else False


class Nand:
    def __new__(cls, itr: Sequence) -> bool:  # type: ignore
        return True if False in itr else False


class Nor:
    def __new__(cls, itr: Sequence) -> bool:  # type: ignore
        return False if True in itr else True


class Xnor:
    def __new__(cls, itr: Sequence) -> bool:  # type: ignore
        return False if itr.count(True) % 2 else True
