#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """hat takes a float multiplier as argument """
    def f(n: float) -> float:
        """multiplies a float by multiplier"""
        return float(n * multiplier)

    return f
