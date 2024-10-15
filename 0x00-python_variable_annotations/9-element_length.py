#!/usr/bin/env python3
"""Read the comments below"""
# Annotate the below function’s parameters and return values with the
# appropriate types

# def element_length(lst):
#     return [(i, len(i)) for i in lst]

from typing import Iterable, Tuple, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuples"""
    return [(i, len(i)) for i in lst]
