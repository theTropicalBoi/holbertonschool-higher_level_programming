#!/usr/bin/python3
def lookup(obj):
    """
    Returns the list of available attributes and methods of an object

    Args:
        obj: object to look up
    """
    return dir(obj)
