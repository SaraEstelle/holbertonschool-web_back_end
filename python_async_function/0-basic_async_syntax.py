#!/usr/bin/env python3
"""Module contenant une coroutine asynchrone qui attend un délai aléatoire."""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """Attend un délai aléatoire entre 0 et max_delay seconds et le retourne.

    args:
        max_delay: délai maximum en secondes (défault: 10)

    Returns:
        Float: le délai effectivement attendu
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
