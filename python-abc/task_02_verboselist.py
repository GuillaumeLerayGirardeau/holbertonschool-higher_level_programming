#!/usr/bin/python3
"""
Class VerboseList, subclass of list
"""


class VerboseList(list):
    """
    can use methods from list
    don't forget the uppercase characters
    """

    def append(self, value):
        super().append(value)
        print(f"Added [{value}] to the list.")

    def extend(self, value):
        super().extend(value)
        print(f"Extended the list with [{len(value)}] items.")

    def remove(self, value):
        print(f"Removed [{value}] from the list.")
        super().remove(value)

    def pop(self, index=None):
        if index is None:
            index = -1
        value = self[index]
        print(f"Popped [{value}] from the list.")
        super().pop(index)
