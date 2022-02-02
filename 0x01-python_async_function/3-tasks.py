#!/usr/bin/env python3
"""function asyncio Task
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Args:
        max_delay (int, optional): [description]. Defaults to 10.
    Returns:
        Any: Task Asyncio
    """
    return asyncio.Task(wait_random(max_delay))
