#!/usr/bin/python3
"""
This module contains function to carry out division of all elements to
uniformly divide a nested list by a given value
"""


def matrix_divided(matrix, div):
    """This function divides all the elements of a matrix by div"""
    invalid_mat = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list or not matrix:
        raise TypeError(invalid_mat)

    type_list = [type(elem) == list for elem in matrix]
    if not all(type_list):
        raise TypeError(invalid_mat)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    len_ls = {len(row) for row in matrix}
    if len(len_ls) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        if not row:
            raise TypeError(invalid_mat)
        for col in row:
            if type(col) not in [int, float]:
                raise TypeError(invalid_mat)

    return [[round(col/div, 2) for col in row]for row in matrix]
