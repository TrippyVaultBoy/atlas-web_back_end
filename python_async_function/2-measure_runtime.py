#!/usr/bin/env python3
"""
From the previous file, import wait_n into 2-measure_runtime.py.

Create a measure_time function with integers n and max_delay as
arguments that measures the total execution time for wait_n(n, max_delay),
and returns total_time / n. Your function should return a float.

Use the time module to measure an approximate elapsed time.
"""
import asyncio
import random
import time
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random function
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n function
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for coroutine in asyncio.as_completed(tasks):
        delay = await coroutine
        delays.append(delay)

    return delays


def measure_time(n: int, max_delay: int) -> float:
    """
    measure_time function
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    runtime = end - start
    return runtime / n
