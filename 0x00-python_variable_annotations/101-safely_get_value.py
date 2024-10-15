#!/usr/bin/env python3
"""Achieves the instructions below"""
# Given the parameters and the return values,
# add type annotations to the function

# Hint: look into TypeVar
# def safely_get_value(dct, key, default = None):
#     if key in dct:
#         return dct[key]
#     else:
#         return default
from typing import Any, Mapping, TypeVar, Optional, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """returns either none or the value if Key is present"""
    if key in dct:
        return dct[key]
    else:
        return default
