#!/usr/bin/env python3
"""
Module that contains one function
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes a list and retunrs a sum of the floats"""
    return sum(x for x in input_list)
