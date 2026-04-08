#!/usr/bin/env python3
"""Module contenant un générateur asynchrone de nombres aléatoires."""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:  # type: ignore
    """Génère 10 nombres aléatoires flottants de manière asynchrone.

    Coroutine qui boucle 10 fois, attend 1 seconde de manière asynchrone
    à chaque itération, puis produit un nombre aléatoire entre 0 et 10.

    Yields:
        float: Un nombre aléatoire entre 0.0 et 10.0.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
