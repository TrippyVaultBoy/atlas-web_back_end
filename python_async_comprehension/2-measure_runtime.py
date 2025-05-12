#!/usr/bin/env python3
"""
Import async_comprehension from the previous file
and write a measure_runtime coroutine that will
execute async_comprehension four times in parallel
using asyncio.gather.

measure_runtime should measure the total runtime
and return it.

Notice that the total runtime is roughly 10 seconds,
explain it to yourself.
"""
import asyncio
import random
import time
from typing import Generator, List


async def async_generator() -> Generator[float, None, None]:
    """
    async_generator function
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def async_comprehension() -> List[float]:
    """
    async_comprehension function
    """
    return [num async for num in async_generator()]


async def measure_runtime() -> float:
    """
    measure_runtime function
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
