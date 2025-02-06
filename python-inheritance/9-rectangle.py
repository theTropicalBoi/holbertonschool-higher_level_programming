#!/usr/bin/python3
"""
Module that defines a Class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instantiation with width and height

        arguments:
            _width: positive integer
            _height: positive integer
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        Method that returns the current rectangle area
        """
        return self.__height * self.__width

    def __str__(self):
        """
        Return a string representation of the Rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
