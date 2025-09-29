#!/usr/bin/python3
"""
function to append a string
"""


def append_write(filename="", text=""):
    """
    append a string at the end of a text file, returns the number of characters
    added
    """

    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
