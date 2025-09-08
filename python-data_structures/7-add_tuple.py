#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) >= 1 and len(tuple_b) >= 1:
        value_1 = tuple_a[0] + tuple_b[0]
    elif len(tuple_a) >= 1 and len(tuple_b) < 1:
        value_1 = tuple_a[0] + 0
    elif len(tuple_a) < 1 and len(tuple_b) >= 1:
        value_1 = 0 + tuple_b[0]
    else:
        value_1 = 0

    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        value_2 = tuple_a[1] + tuple_b[1]
    elif len(tuple_a) >= 2 and len(tuple_b) < 2:
        value_2 = tuple_a[1] + 0
    elif len(tuple_a) < 2 and len(tuple_b) >= 2:
        value_2 = 0 + tuple_b[1]
    else:
        value_2 = 0

    new_tuple = (value_1, value_2)

    return new_tuple
