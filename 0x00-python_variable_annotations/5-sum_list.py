#!/usr/bin/env python3
""" complex type-annotated to Lists
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ function receive a list and return its sum as float
    """
    return sum(input_list)
