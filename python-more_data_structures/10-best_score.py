#!/usr/bin/python3

def best_score(a_dictionary):
    value = 0
    name = None
    if a_dictionary is not None:
        for i in a_dictionary:
            if a_dictionary[i] > value:
                value = a_dictionary[i]
                name = i
    return name
