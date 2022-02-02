#!/usr/bin/env python3
""" complex type-annotated to Callable
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ func that takes a float as argument and returns a func
        that multiplies a float by multiplier.
    """
    def mul(b: float) -> float:
        return b * multiplier
    return mul
