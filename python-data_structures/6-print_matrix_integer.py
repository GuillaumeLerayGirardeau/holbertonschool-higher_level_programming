#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for i in matrix:
        count = 1
        for y in i:
            print("{:d}".format(y), end="")
            if count != len(i):
                print(" ", end="")
            count += 1
        print("")
