#!/usr/bin/python3
"""Module for reading a text file"""


def class_to_json(obj):
    """
    Function that returns the dict description with simple data struct
    for a JSON serialization of an object

    Arguments:
        obj: Instance of a class

    Returns:
        Dictionary description with simple data structure
    """
    return obj.__dict__
