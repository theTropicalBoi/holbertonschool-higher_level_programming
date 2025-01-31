#!/usr/bin/python3
"""
Defines a class rectangle.
"""


class Rectangle:
    """
    Empty class that defines a rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            rectangle.append(str(self.print_symbol) * self.__width)
        return "\n".join(rectangle)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __repr__(self):
        return ("{}({}, {})".format(__class__.__name__,
                                    self.__width, self.__height))

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
