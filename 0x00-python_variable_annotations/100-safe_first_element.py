#!/usr/bin/env python3
""" complex type-annotated to Any
"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ complex type-annotated to Any
    """
    if lst:
        return lst[0]
    else:
        return None
