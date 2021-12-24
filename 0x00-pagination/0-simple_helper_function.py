#!/usr/bin/env python3
"""
Find the index range
"""


def index_range(page: int, page_size: int) -> tuple:
    """ return a start index and an end index corresponding to the range """
    start = 0 if page == 1 else page
    end = page + start
    return (start, end)