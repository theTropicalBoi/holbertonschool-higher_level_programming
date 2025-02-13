#!/usr/bin/python3
"""Module for reading a text file"""


class Student:
    """
    Class Student

    Takes as public instance attributes:
        first_name
        last_name
        age

    Public method: def to_json(self): that retrieves a dict
    representation of a Student instance
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialization of Student class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns the dict representation of the Student Class
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
