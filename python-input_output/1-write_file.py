#!/usr/bin/python3
"""
function that write into a file
"""


def write_file(filename="", text=""):
    """
    write into a file and returns number of characters written
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
