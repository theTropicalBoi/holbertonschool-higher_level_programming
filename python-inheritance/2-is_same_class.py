#!/usr/bin/python3
"""
Function that returns True if the object is EXACTLY an instance
of the specified class, otherwise False
"""


def is_same_class(obj, a_class):
    """
    Function is_same_class

    arguments:
        _obj: object
        _a_class: a specified class

    Return:
        _True if right
        _False otherwise
    """
    if type(obj) is a_class:
        return True
    else:
        return False
