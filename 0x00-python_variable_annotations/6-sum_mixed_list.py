#!/usr/bin/env python3
""" complex type-annotated to Lists
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ function receive a list of int, float and return its sum as float
    """
    return sum(mxd_lst)
