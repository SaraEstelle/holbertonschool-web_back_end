#!/bin/usr/env python3
"""Module pour mesurer le temps d'exécution de wait_n."""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Mesure le temps total d'exécution de wait_n et retourne le temps moyen.

    lance wait_n(n, max_delay) et mesure le temps écoulé. Retourne
    le temps total divisé par n pour obtenir le temps moyen par coroutine.

    Args:
        n: nombre de coroutines à lancer
        max_delay: délai maximum en secondes

    Returns:
        float: temps moyen d'exécution par coroutine"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
