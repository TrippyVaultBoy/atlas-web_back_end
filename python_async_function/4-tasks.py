#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new
function task_wait_n. The code is nearly identical
to wait_n except task_wait_random is being called.
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


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    task_wait_random function
    """
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_n function
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for coroutine in asyncio.as_completed(tasks):
        delay = await coroutine
        delays.append(delay)

    return delays
