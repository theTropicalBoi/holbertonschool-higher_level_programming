#!/usr/bin/python3
"""
Basic serialization module that adds the functionality to
serialize a Python dictionary to JSON file and deserialize the
JSON file to recreate the Python Dictionary.
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize Python dictionary and save it as a JSON file

    Args:
        data (dict): The python dict to be serialized
        filename (str): the name of the JSON file to save the serialized data.
    """
    with open(filename, "w") as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file into a python dict.

    Args:
        filename (str): The name of the JSON file to be loaded and
        deserialize.

    Returns:
        data: the serialized dictionary.
    """
    with open(filename, "r") as file:
        data = json.load(file)
    return data
