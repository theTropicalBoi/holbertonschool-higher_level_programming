#!/usr/bin/python3
"""
Class CountedIterator that extends the built-in iterator obtained from the
iter function. CountedIterator should keep track of the number of items
that have been iterated over.
"""


class CountedIterator:
    """
    CountedIterator class that extends the built-in iterator.
    """
    def __init__(self, iterable):
        """
        Initialize iterator and the counter

        argument:
            _i: iterable
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Method to increment the counter each time __next__ is called.
        Raises exception StopIteration if there are no more items.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """
        Return the current count of items iterated over.
        """
        return self.count
