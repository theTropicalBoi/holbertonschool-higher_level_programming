#!/usr/bin/python3
"""
Class that can serialize and deserialize custom Python Objects
using the pickle module.
"""


import pickle


class CustomObject:
    """
    Custom class 'CustomObject'.
    """
    def __init__(self, name, age, is_student):
        """
        Initialize the attributes name, age, is_student.

        Args:
            name (str): Name of the students
            age (int): Age of the students
            is_student (bool): Is a student or not
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object attributes.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize and save it to a file
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error during serialization: {e}.")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize and return an instance of CustomObject
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Error during deserialization: {e}.")
            return None
