#!/usr/bin/python3
"""
Pascal triangle function
"""


def pascal_triangle(n):

    """
    Print a Pascal Triangle of size n
    """

    pascal_list = []
    next_list = []
    count = 0

    while count < n:
        if count > 1:
            temp = 0
            addition = 1
            while addition < len(pascal_list[count - 1]):
                next_list[0] = pascal_list[count - 1][0]
                next_list[addition] = (
                    pascal_list[count - 1][temp] +
                    pascal_list[count - 1][addition]
                )
                temp += 1
                addition += 1
            next_list.append(1)
            pascal_list.append(next_list.copy())
        else:
            next_list.append(1)
            pascal_list.append(next_list.copy())
        count += 1

    return pascal_list
