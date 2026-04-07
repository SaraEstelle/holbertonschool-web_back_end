#!/usr/bin/env python3
"""Module providing a type-annoted higher-order multiplier finction."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    def multiply(x: float) -> float:
        """Multiply x by the captured multiplier value."""
        return x * multiplier
    return multiply
