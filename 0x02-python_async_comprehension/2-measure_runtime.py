#!/usr/bin/env python3
""" coroutine async comprehensions
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Returns:
        float: measured time
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension(),
                           async_comprehension(),
                           async_comprehension(),
                           async_comprehension()))
    elapsed = time.perf_counter() - start
    return elapsed
