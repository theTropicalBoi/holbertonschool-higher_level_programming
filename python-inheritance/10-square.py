#!/usr/bin/python3
"""
Class Square that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Instantiation with size

        arguments:
            _size(int): Positive integer of the size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Public instance method that returns the area of the square.
        """
        return self.__size * self.__size
