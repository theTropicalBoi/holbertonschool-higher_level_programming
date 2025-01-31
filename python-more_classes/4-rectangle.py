#!/usr/bin/python3
"""
Defines a class rectangle.
"""


class Rectangle:
    """
    Empty class that defines a rectangle.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the witdh of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the witdh of the rectangle.

        Args:
            width: The width of the rectangle.

        Raises:
            TypeError: If witdh isn't an integer.
            ValueError: If width < 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle.

        Args:
            height: The height of the rectangle.

        Raises:
            TypeError: If height isn't an integer.
            ValueError: If height < 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the current rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Returns the current rectangle perimeter
        If either width or height is 0, returns 0.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """
        Returns a string representation of the rectangle with '#'.

        If either width or height is 0, returns an empty string.
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle = []
        for _ in range(self.__height):
            rectangle.append("#" * self.__width)
        return "\n".join(rectangle)

    def __repr__(self):
        return ("{}({}, {})".format(__class__.__name__,
                                    self.__width, self.__height))
