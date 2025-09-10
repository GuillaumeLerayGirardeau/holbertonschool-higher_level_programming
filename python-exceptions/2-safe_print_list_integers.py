#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    printed = 0
    try:
        for i in range(x):
            if type(my_list[count]) == int:
                print("{:d}".format(my_list[count]), end="")
                printed += 1
            count += 1
        print("")
        return printed
    except TypeError:
        return
