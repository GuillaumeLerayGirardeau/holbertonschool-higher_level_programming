"""
Module print square

Functions:
    print_square(size)
"""

#!/usr/bin/python3

def print_square(size):

    """
    Print the square of a number
    size is the size length of the square and must be an integer superior to 0
    return the value, else TypeError or ValueError
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    space = ""
    for i in range(size):
        for y in range(size):
            print(f"{space}#", end="")
            if y + 1 == size:
                print("")
