#!/usr/bin/python3
"""
Class named VerboseList that extends the Python list class.
This custom class should print a notification message every time
an item is added or removed.
"""


class VerboseList(list):
    """
    Custom list class that extends the Python list class and prints
    notification when items are added or removed
    """
    def append(self, item):
        """
        Method to add an item to the list and print a notification
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, i):
        """
        Method to extend the list with iteration and print a notification
        """
        super().extend(i)
        print(f"Extended the list with [{len(i)}] items.")

    def remove(self, item):
        """
        Method to remove item from the list and print a notification
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Method to remove an item from the list by the index
        (or the last one if no index given)
        """
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
