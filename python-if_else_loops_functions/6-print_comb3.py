#!/usr/bin/python3

for i in range(9):
    for y in range(i+1, 10):
        if i != 8:
            print(f"{i}{y}", end=", ")
        else:
            print(f"{i}{y}")
