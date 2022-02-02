#!/usr/bin/env python3
""" Asyncronous function with random delay
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Args:
        max_delay (int, optional): [description]. Defaults to 10.
    Returns:
        [type]: [description]
    """
    r = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
