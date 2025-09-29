#!/usr/bin/python3
"""
function to read and print a file
"""


def read_file(filename=""):
    """
    read and print a file
    """

    with open(filename, encoding="utf-8") as f:
        for i in f:
            print(i, end="")
