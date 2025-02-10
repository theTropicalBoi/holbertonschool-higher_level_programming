#!/usr/bin/python3
"""
Abstract class Shape with two abstract methods area and perimeter.
Two concrete classes, Circle and Rectangle, both inheriting Shape
Each class should provide implementation for area and perimeter.
Standalone function named shape_info that accepts an object of type Shape
and prints its area and perimeter.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract class Shape
    """
    @abstractmethod
    def area(self):
        """
        Abstract method area
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method perimeter
        """
        pass


class Circle(Shape):
    """
    Concrete Class Circle that inherits from Shape
    """
    def __init__(self, radius):
        """
        Initialization method

        Argument:
            _radius: the radius of the circle
        """
        self.radius = abs(radius)

    def area(self):
        """
        Area method for circle
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Perimeter method for circle
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Concrete class Rectangle that inherits from shape
    """
    def __init__(self, width, height):
        """
        Initialization with width and height
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Area method for rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Perimeter method for rectangle
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Function shape_info relying on duck typing to call area() and perimeter() methods.

    Argument:
        _shape: shape of the circle and rectangle
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
