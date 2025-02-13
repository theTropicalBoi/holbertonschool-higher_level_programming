#!/usr/bin/python3
"""This is a module for reading file."""


def read_file(filename=""):
    """Read a UTF-9 file and print it's content.
    
    Args:
        filename (str): The name of the file that needs to be reed. Empty by default.
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
