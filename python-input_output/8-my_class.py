#!/usr/bin/python3
"""
My class module
"""


class MyClass:
    """
    My class
    """

    def __init__(self, name):
        """
        Initialize functions
        """
        self.name = name
        self.number = 0

    def __str__(self):
        """
        str function
        """
        return "[MyClass] {} - {:d}".format(self.name, self.number)
