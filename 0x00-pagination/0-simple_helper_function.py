#!/usr/bin/env python3
"""
Find the index range
"""


def index_range(page: int, page_size: int) -> tuple:
    """ return a start index and an end index corresponding to the range """
    start = sum([page_size for i in range(page - 1)]) if page > 0 else 0
    end = page_size + start
    return (start, end)
