#!/usr/bin/python3
"""
function that returns True if the object is an instance
of a class that inherited (directly or indirectly) from
the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """
    Function inherits_from

    arguments:
        _ibj: object
        _a_class: specified class

    Return:
        _True if the object if an instance of a class that inherited
        from the specified class
        _False if otherwise
    """
    if isinstance(obj, a_class):
        if obj.__class__ is not a_class:
            return True
    return False
