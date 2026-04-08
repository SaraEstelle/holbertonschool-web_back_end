#!/usr/bin/env python3
"""Module fournissant une factory de Tasks asyncio pour wait_random."""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Crée et retourne un asyncio. Task pour wait_random(max_delay).

    cette fonction synchrone crée un Task qui planifie l'exécution
    de wait_random dans l'event loop courante.

    args:
        max_delay (int): Le délai maximum en secondes pour wait_random.*

    Returns:
        asyncio.Task: Un Task qui planifie l'exécution
        de wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))
