#!/usr/bin/python3
"""
Adds two integers

Args:
    a (int): first number
    b (int): second number

Returns: sum of the two integer
"""


def add_integer(a, b=98):

    """
    Adds two integers
    Take two integer for arguments
    Return the result, or TypeError
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
