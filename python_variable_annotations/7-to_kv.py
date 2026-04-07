#!/usr/bin/env python3
"""Module providing a type-annotated function returnin a key-value tuple."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple of the string k and the square of v as a float."""
    return (k, float(v ** 2))
