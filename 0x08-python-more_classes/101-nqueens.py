#!/usr/bin/python3
"""
This module contains function to solve the n_queens_n function
using the backtracking algorithm
"""

import sys


def print_board(board):
    """The function to print the board"""
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col]:
                print(f"({row}, {col})", end=" ")
        print()


def is_safe(row, col):
    """The function to check for the safety of a position"""
    for i in range(n):
        if board[row][i]:
            return False

    for i in range(n):
        if board[i][col]:
            return False

    x = col + 1
    y = row - 1
    while(y >= 0 and x < n):
        if board[y][x]:
            return False
        x += 1
        y -= 1

    x = col - 1
    y = row - 1
    while (y >= 0 and x >= 0):
        if board[y][x]:
            return False
        x -= 1
        y -= 1

    x = col + 1
    y = row + 1
    while (y < n and x < n):
        if board[y][x]:
            return False
        x += 1
        y += 1

    x = col - 1
    y = row + 1
    while (y < n and x >= 0):
        if board[y][x]:
            return False
        x -= 1
        y += 1

    return True


def nqueens(n, count, solutions):
    """The function that execute and find possible combination"""
    if n == count:
        solutions.append([row[:] for row in board])
        return

    for y in range(n):
        for x in range(n):
            if is_safe(y, x):
                count += 1
                board[y][x] = True
                nqueens(n, count, solutions)
                board[y][x] = False
                count -= 1


def print_solution(solution):
    """print solution"""
    print(solution)


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print("Usage: nqueens N")
            exit(1)
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            exit(1)
        board = [[False for i in range(n)] for i in range(n)]
        solutions = []
        nqueens(n, 0, solutions)

        unique_solutions = []
        for solution in solutions:
            if solution not in unique_solutions:
                unique_solutions.append(solution)

        for solution in unique_solutions:
            print_solution([[row, col] for row, row_vals in enumerate(solution)
                            for col, val in enumerate(row_vals) if val])

    except ValueError as e:
        print("N must be a number")
        exit(1)
