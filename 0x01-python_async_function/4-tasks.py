#!/usr/bin/env python3
""" function with multi coroutines and task
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n (int): times to iterate
        max_delay (int): number to pass as args to wait_random
    Returns:
        List: List with all delay
    """
    delay_list = []
    for _ in range(n):
        delay_list.append(await task_wait_random(max_delay))
    return [i for i in sorted(delay_list)]
