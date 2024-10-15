#!/usr/bin/env python3
"""
Contains a function that accepts a string
and returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and a number (int or float), and returns a tuple.
    """
    return (k, float(v ** 2))
