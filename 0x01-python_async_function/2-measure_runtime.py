#!/usr/bin/env python3
"""function that measures the total execution time for wait_n(n, max_delay)
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Args:
        n (int): [initial value]
        max_delay (int): [time to delay]
    Returns:
        float: time elapsed divided by n
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start
    return elapsed / n
