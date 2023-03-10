#!/usr/bin/env python3
"""mixed list"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Element length"""
    return [(i, len(i)) for i in lst]
