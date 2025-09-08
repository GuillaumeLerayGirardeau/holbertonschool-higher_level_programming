#!/usr/bin/python3

def element_at(my_list, idx):

    num = None

    if idx < 0:
        num = None
    elif idx < len(my_list):
        num = my_list[idx]
    
    return(num)
