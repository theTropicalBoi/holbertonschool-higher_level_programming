#!/usr/bin/python3
"""BaseGeometry module.

This module defines the BaseGeometry class which serves as a base class
for all geometry shapes. It provides basic functionality for geometric
calculations and validations.

Example:
    >>> bg = BaseGeometry()
    >>> bg.integer_validator("side_length", 12)
"""


class BaseGeometry:
    """A base class for all geometric shapes.

    This class serves as a template for geometric calculations and validations.
    It provides methods for calculating area and validating integer values
    that will be used by geometric shape classes that inherit from it.

    Attributes:
        No attributes are defined in this base class.
    """

    def area(self):
        """Calculate the area of the geometric shape.

        This method must be implemented by all classes that inherit from
        BaseGeometry. The base implementation raises an Exception to remind
        the developer that this method needs to be implemented in the
        child class.

        Raises:
            Exception: Always, with the message "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.

        This method validates that the given value is a positive integer.
        It is typically used to validate geometric measurements like length,
        width, radius, etc. before they are used in calculations.

        Args:
            name (str): The name of the value being validated. This name
                will be used in error messages if validation fails.
            value: The value to validate. Must be a positive integer.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.

        Example:
            >>> bg = BaseGeometry()
            >>> bg.integer_validator("side_length", 12)
            >>> bg.integer_validator("radius", -5)  # Will raise ValueError
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
