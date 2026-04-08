#!/usr/bin/env python3
"""Module de lancement concurrent de plusieurs coroutines wait_random."""

import asyncio
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
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for finished_coroutine in asyncio.as_completed(coroutines):
        delay = await finished_coroutine
        delays.append(delay)

    return delays

