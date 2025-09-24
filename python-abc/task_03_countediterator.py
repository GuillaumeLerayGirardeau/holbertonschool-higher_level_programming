#!/usr/bin/python3
"""
CountedIterator class
"""


class CountedIterator():
    """
    Can iterate a list
    don't forget the uppercase characters
    """

    def __init__(self, my_list):
        self.iterator = iter(my_list)
        self.max_value = len(my_list)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        self.counter += 1
        if self.counter > self.max_value:
            raise StopIteration
        return next(self.iterator)
