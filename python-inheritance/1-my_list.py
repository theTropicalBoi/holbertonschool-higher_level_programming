#!/usr/bin/python3
"""
Class MyList that inherits from list
"""


class MyList(list):
    """
    Class MyList that inherits from list

    Arguments:
        _list: builtin list
    """
    def print_sorted(self):
        """
        Module print_sorted to print the list in sorted way
        """
        print(sorted(self))
