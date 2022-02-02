#!/usr/bin/env python3
""" coroutine async generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Yields:
        [type]: [description]
    """
    n: int = 10
    for i in range(n):
        await asyncio.sleep(1)
        yield random.uniform(0, n)
