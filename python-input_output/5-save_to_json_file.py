#!/usr/bin/python3
"""Module for reading a text file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an object to a text file,
    using a JSON representation

    Arguments:
        my_obj: the object to write
        filename: the text file
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
