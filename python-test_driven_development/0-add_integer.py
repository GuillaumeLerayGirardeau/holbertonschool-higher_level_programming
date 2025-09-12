#!/usr/bin/python3

def add_integer(a, b=98):
    """
    add_integer : adds two integers

    Return the result, or TypeError
    This function must take two integers. If float value, it will be converted
    into integer. 
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
