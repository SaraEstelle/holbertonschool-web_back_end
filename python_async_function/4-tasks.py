#!/usr/bin/env python3
"""Module variant de wait_n utilisant task_wait_random."""

import asyncio
import bisect
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Lance n fois task_wait_random en concurrent et retourne les délais triés.

    variante de wait_n qui utilise task_wait pour créer les tâches
    asynchrones. Retourne les dérais dans l'ordre croissant grace
    à l'insertion triée de bisect sans utiliser sort().

    Args:
        n: nombre de coroutines à lancer simultanément
        max_delay: délai maximum en secondes pour chaque task_wait_random

    Réturns:
        List[float]: liste des délais en ordre croissant.
    """
    delays: List[float] = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in tasks:
        delay = await task
        bisect.insort(delays, delay)
    return delays
