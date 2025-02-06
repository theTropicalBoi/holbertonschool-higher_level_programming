#!/usr/bin/python3
"""
Function that returns True if the object if an instance of,
or if the object is an instance of a class that inherited from,
the specified class; otherwise false
"""


def is_kind_of_class(obj, a_class):
    """
    function is_kind_of_class

    arguments:
        _obj: object
        _a_class: specified class

    Return:
        _True if object is an instance of a class inherited from
        _False if otherwise
    """
    return isinstance(obj, a_class)
