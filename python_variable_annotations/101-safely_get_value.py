#!/usr/bin/env python3
"""Module providing a type-annotated safe dictionary value getter."""
from typing import Any, Mapping, Optional, TypeVar, Union

T = TypeVar('T')

def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """Return dct[key] if key exists, otherwse return default."""
    if key in dct:
        return dct[key]
    else:
        return default
