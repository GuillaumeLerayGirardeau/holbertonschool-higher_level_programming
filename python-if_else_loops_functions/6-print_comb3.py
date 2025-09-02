#!/usr/bin/python3

for i in range(9):
    for y in range(i+1, 10):
        if i != 8:
            print("{:d}".format(i) + "{:d}".format(y), end=", ")
        else:
            print("{:d}".format(i) + "{:d}".format(y))
