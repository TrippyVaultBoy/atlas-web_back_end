#!/usr/bin/env python3
"""
Import wait_random from 0-basic_async_syntax.

Write a function (do not create an async function,
use the regular function syntax to do this) task_wait_random
that takes an integer max_delay and returns a asyncio.Task.
"""
import asyncio
import random
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


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    task_wait_random
    """
    return asyncio.create_task(wait_random(max_delay))
