#!/usr/bin/env python3
"""
Write a function named index_range that
takes two integer arguments page and page_size
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    index_range function
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
