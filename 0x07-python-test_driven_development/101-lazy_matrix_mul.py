#!/usr/bin/python3
"""
This module contains a function called lazy_matrix that multiplies two matrices
together using the numpy module
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This function utilizing the numpy library multiplies two matrixes together
    and in the case where and error is encountered an error message is raised

    Args
    @m_a: The matrix a
    @m_b: The matrix b
    Return: The product of the two matrices
    """
    mat_a = np.array(m_a)
    mat_b = np.array(m_b)
    return np.dot(mat_a, mat_b)
