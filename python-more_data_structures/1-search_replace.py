#!/usr/bin/python3

def search_replace(my_list, search, replace):

    new_list = my_list.copy()
    idx = search - 1

    if idx < len(my_list):
        new_list[idx] = replace
    return new_list
