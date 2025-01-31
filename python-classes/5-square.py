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
        Initialize a new Square instance.

        Args:
            size (int, optional): The size of the square's side. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter for the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size of the square's side.

        Args:
            size: The size of the square's side

        Raises:
            TypeError: If size isn't an integer.
            ValueError: If size < 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints in stdout the square with the character #
        """
        if self.size == 0:
            print()
        for i in range(self.size):
            print("{}".format("#" * self.size))
