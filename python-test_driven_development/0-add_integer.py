#!/usr/bin/python3
"""
This module contains a function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    Adds 2 integers.
    Args:
        a (int or float): The first number.
        b (int or float): The second number. Defaults to 98.
    Returns:
        an integer: the addition of a and b
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
