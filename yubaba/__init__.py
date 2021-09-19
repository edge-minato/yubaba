from pathlib import Path

from single_source import get_version

from .condition import F, If, Nif, print_if  # noqa
from .logical_operator import And, Nand, Nor, Or, Xnor, Xor  # noqa

__version__ = get_version(__name__, Path(__file__).parent.parent)
