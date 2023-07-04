#!/usr/bin/python3
"""
This module contains the print_square() function
Usage:
>>> print_square(3)
###
###
###
"""


def print_square(size):
    """
    This function prints a hash filled square of size equal to an
    integer value supplied to the function

    Args
    @size: The size of the square to be printed
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
