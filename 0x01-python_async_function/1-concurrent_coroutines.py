#!/usr/bin/env python3
""" function with multy coroutines
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n (int): times to iterate
        max_delay (int): number to pass as args to wait_random
    Returns:
        List: List with all delay
    """
    delay_list = []
    for _ in range(n):
        delay_list.append(await wait_random(max_delay))
    return [i for i in sorted(delay_list)]
