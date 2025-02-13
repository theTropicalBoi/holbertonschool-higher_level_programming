#!/usr/bin/python3
"""Module for reading a text file"""


def pascal_triangle(n):
    """
    Return a list of int representing Pascal's triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for row_num in range(1, n):
        row = [1]
        for col_num in range(1, row_num):
            row.append(triangle[row_num - 1][col_num - 1] +
                       triangle[row_num - 1][col_num])
        row.append(1)
        triangle.append(row)

    return triangle
