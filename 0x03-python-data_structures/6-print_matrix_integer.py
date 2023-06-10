#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx, val in enumerate(row):
            if idx == (len(row) - 1):
                print("{:d}".format(val))
            else:
                print("{:d}".format(val), end=" ")
    if not matrix[0]:
        print()
