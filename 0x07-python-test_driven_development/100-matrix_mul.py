#!/usr/bin/python3
"""
This module contains functions that helps to carry out multiplication
between two matrices
"""


def mat_check(matrix, label):
    """
    This function checks that a list of list meets the definition of a
    matrix

    Args
    @matrix: The matrix we are carrying out error check on
    @label: The label for the matrix to use in printing error message
    Return: A tuple of the matrix dimension in the format (row, col)
    """
    if type(matrix) != list:
        raise TypeError(f"{label} must be a list")

    if not all([type(i) == list for i in matrix]):
        raise TypeError(f"{label} must be a list of list")

    if not matrix or any([not i for i in matrix]):
        raise ValueError(f"{label} can't be empty")

    if any([any(list(map(lambda x: type(x) not in (float, int),
                         row))) for row in matrix]):
        raise TypeError(f"{label} should contain only integers or"
                        " floats")
    if len(set(list(map(lambda x: len(x), matrix)))) > 1:
        raise TypeError(f"each row of {label} must be of the same size")

    return (len(matrix), len(matrix[0]))


def sum_row(row):
    """
    Sum the rows obtained from scaling each row of the matrix together

    Args
    @row: The row resulting from scaling each row of second matrix by a row of
          the first matrix
    Return: The result of addition of the elements of the row
    """
    result = [0] * len(row[0])
    for row_elem in row:
        for idx, elem in enumerate(row_elem):
            result[idx] += elem

    return result


def matrix_mul(m_a, m_b):
    """
    This functions multiplies two matrices and returns the product matrix

    Args
    @m_a: The first matrix
    @m_b: The second matrix
    Return: The product of the addition of two matrices together
    """
    # check the arguments if it contains the right values
    dim_a = mat_check(m_a, "m_a")
    dim_b = mat_check(m_b, "m_b")
    if dim_a[1] != dim_b[0]:
        raise ValueError("m_a and m_b can't be multiplied")
    # carry out matrix multiplication
    result = []
    for row in m_a:
        result_row = []
        for idx, row_elem in enumerate(row):
            col = m_b[idx]
            result_row.append([row_elem * col_elem for col_elem in col])
        result.append(sum_row(result_row))
    return result
