#!/usr/bin/env python3
"""Contains a function with a list with many types"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Accepts a list and returns sum of all elements"""
    return sum(x for x in mxd_list)
