#!/usr/bin/env python3
""" complex type-annotated to Tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ complex type-annotated to Tuple return diff types
    """
    return (k, v**2)
