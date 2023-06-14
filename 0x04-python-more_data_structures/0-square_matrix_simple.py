#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return []
    else:
        return list(map(lambda x: list(map(lambda x: x**2, x)), matrix))
