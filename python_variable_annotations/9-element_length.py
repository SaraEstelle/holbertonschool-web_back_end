#!/usr/bin/env python3
"""Module providing a duck-typed function returning element lengths."""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing each element and its length."""
    return [(i, len(i)) for i in lst]
