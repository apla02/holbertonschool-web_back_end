#!/usr/bin/env python3
""" complex type-annotated to Itarable and Sequence
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ complex type-annotated to Itarable and Sequence
    """
    return [(i, len(i)) for i in lst]
