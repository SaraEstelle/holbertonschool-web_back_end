#!/usr/bin/env python3
"""Module utilisant une async comprehension pour collecter des valeurs.

Ce module démontre l'utilisation des async comprehensions (PEP 530)
pour collecter des résultats depuis un générateur asynchrone.
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collecte 10 nombres aléatoires via une async comprehension.

    Utilise une async comprehension pour itérer sur async_generator
    et collecter les 10 valeurs flottantes produites.

    Returns:
        List[float]: Une liste de 10 nombres aléatoires entre 0.0 et 10.0.
    """
    return [val async for val in async_generator()]
