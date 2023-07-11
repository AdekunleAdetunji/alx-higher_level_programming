#!/usr/bin/python3
"""
This module contains a python function that creates a pascal triangle
"""


def find_fac(n):
    """
    find the factorial of a value n

    args
    @n: integer whose value we want to find
    """
    if n == 1 or n == 0:
        return 1
    return n * find_fac(n - 1)


def pascal_triangle(n):
    """
    creates a pascals triangle of size n

    args
       @n: The size of the pascal's triangle
    """
    result = []
    if n <= 0:
        return result
    for row in range(0, n):
        row_vals = []
        for elem in range(0, row + 1):
            val = int(find_fac(row) / (find_fac(row-elem) * find_fac(elem)))
            row_vals.append(val)
        result.append(row_vals)
    return result
