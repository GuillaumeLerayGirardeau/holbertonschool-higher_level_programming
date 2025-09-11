#!/usr/bin/python3

# adds two integer 
def add_integer(a, b=98):
    
    try:
         return int(a) + int(b)
    except (TypeError, ValueError):
        if isinstance(a, int):
            raise TypeError("b must be an integer")
        else:
            raise TypeError("a must be an integer")
