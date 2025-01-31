#!/usr/bin/python3
"""
Module that defines a Square class
"""


class Square:
    """
    A class that represents a square
    """
    def __init__(self, size=0):
        """
        Initialize a new Square instance

        Args:
            size: The size of the square's side

        Raises:
            TypeError: If size isn't an integer.
            ValueError: If size < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the current square area
        """
        return self.__size ** 2
