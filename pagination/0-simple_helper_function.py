#!/usr/bin/env python3
"""
Module providing a helper function to compute pagination index ranges.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple containing the start and end index for pagination.
        Pages are 1-indexed: page 1 at index starts at index 0 for python

        Args:
            page: the page number (1-indexed, must be >= 1 )
            page_size: the number of items per page

        Returns:
            A tuple  ( startt, end) to use as slice bounds on a list.
    """
    start =(page - 1) * page_size
    end = page* page_size
    return ( start, end)
