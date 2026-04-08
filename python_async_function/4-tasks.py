#!/usr/bin/env python3
"""Module variant de wait_n utilisant task_wait_random."""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Lance n fois task_wait_random en concurrent
    et retourne les délais triés.
    """
    delays = []
    tasks = []
    for i in range(n):
        tasks.append(task_wait_random(max_delay))
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
