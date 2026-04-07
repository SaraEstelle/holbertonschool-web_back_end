#!/usr/bin/env python3
"""Module de lancement concurrent de plusieurs coroutines wait_random."""

import asyncio
import bisect
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Lance n fois wait_random en concurrent et retourne les délais triés.

    Args:
        n: nombre de coroutines à lancer simultanément
        max_delay: délai maximum pour chaque wait_random

    Réturns:
        List[float]: liste des délais en ordre croissant.
    """
    delays: List[float] = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    for task in tasks:
        delay = await task
        bisect.insort(delays, delay)
    return delays
