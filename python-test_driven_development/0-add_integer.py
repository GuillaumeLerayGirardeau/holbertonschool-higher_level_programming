#!/usr/bin/python3

def add_integer(a, b=98):
    """
    add_integer : adds two integers

    Return the result, or TypeError
    This function must take two integers. If float value, it will be converted
    into integer. 
    """
    try:
         return int(a) + int(b)
    except (TypeError, ValueError):
        if isinstance(a, int):
            raise TypeError("b must be an integer")
        else:
            raise TypeError("a must be an integer")
