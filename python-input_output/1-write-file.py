#!/usr/bin/python3
"""Module for reading a text file"""


def write_file(filename="", text=""):
    """Writes a string from a text file and 
    returns the number of character written.

    Arguments:
        filename: the file we'll take the string from
        text: the string we'll write

    Returns:
        The number of character written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
