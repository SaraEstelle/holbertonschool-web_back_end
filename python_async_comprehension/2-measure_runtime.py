#!/usr/bin/env python3
"""Module mesurant le temps d'exécution de quatre comprehensions parallèles.

Ce module illustre l'utilisation de asyncio.gather pour exécuter plusieurs
coroutines en parallèle et mesure le temps total d'exécution résultant.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Mesure le temps d'exécution de quatre async comprehensions en parallèle.

    Exécute async_comprehension quatre fois simultanément via asyncio.gather,
    mesure le temps total écoulé et le retourne. Le temps attendu est d'environ
    10 secondes car les quatre coroutines s'exécutent de manière concurrente
    et partagent les mêmes périodes d'attente asynchrone.

    Returns:
        float: Le temps total d'exécution en secondes (environ 10.0).
    """
    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    return time.perf_counter() - start
