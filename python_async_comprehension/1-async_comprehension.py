#!/usr/bin/env python3
"""
Import async_generator from the previous task and
then write a coroutine called async_comprehension
that takes no arguments.

The coroutine will collect 10 random numbers using
an async comprehensing over async_generator, then
return the 10 random numbers.
"""
import asyncio
import random
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
    result = []
    async for value in async_generator():
        result.append(value)
    return result
