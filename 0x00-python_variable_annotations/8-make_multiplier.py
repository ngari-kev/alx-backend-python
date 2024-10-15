#!/usr/bin/env python3
"""Contains a function that shows a callable type"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """"
    takes a float `multiplier` as argument and returns a function that multiplies a float by `multiplier`
    """
    def mul(operand: float) -> float:
        """takes a float and multiplies it with another float"""
        return operand * multiplier
    
    return mul
