#!/usr/bin/env python3
"""Create a tuple displaying results
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """[summary]
    Args:
        page (int): amount of pages
        page_size (int): amount row to display
    Returns:
        Tuple: start index - end index
    """
    start_index: int = (page - 1) * page_size
    end_index: int = page * page_size
    tuple_of_page = (start_index, end_index)
    return tuple_of_page
