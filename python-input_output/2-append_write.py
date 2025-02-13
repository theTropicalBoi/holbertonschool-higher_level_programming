#!/usr/bin/python3
"""Module for reading a text file"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file
    and returns the number of characters added.
    If the file doesnt exist, it will be created.

    arguments:
        filename: The file we will append the string to.
        text: The text we will append to the file.

    Returns:
        The number of character added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
