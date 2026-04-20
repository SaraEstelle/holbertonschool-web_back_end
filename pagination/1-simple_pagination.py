#!/usr/bin/env python3
"""
Module providing a helper function to compute pagination index ranges.
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple containing the start and end index for pagination.
        Pages are 1-indexed: page 1 at index starts at index 0 for python

        Args:
            page: the page number (1-indexed, must be >= 1 )
            page_size: the number of items per page

        Returns:
            A tuple  ( startt, end) to use as slice bounds on a list.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server with an empty dataste cache."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset, loading from CSV file if necessary.
        The header row is excluded from the returned dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the appropriate page of data from the baby names dataset.

        Args:
            page: the page number to retrirve (1- indexed, must be int > 0).
            page_size: the number of rows per page (ust be int > 0)

        Returns:
            A list of rows for the requested page. or an empty list if
            the page is out of range.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []
        return dataset[start:end]
