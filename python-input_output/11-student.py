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

    def to_json(self, attrs=None):
        """
        Returns the dict representation of the Student Class.
        If attrs is a list of strings, only attribute names contained
        in the list must be retrieved.
        Otherwise, all attributes must be retrieved.
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            json_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_dict[attr] = getattr(self, attr)
            return json_dict

    def reload_from_json(self, json):
        """
        Reload the student instance attrs from the provided dict
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
