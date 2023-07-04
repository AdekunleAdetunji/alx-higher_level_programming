#!/usr/bin/python3
"""
This module contains the function add_integer() that adds two
integer/float values supplied to the function when it is called
Usage:
>>> add_integer(2, 3)
5
"""


def add_integer(a, b=98):
    """
    This function adds two integer values when called

    Args
    @a: The first positional argument
    @b: The second positional argument or keyword argment
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return (a + b)
