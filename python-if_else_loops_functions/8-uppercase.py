#!/usr/bin/python3

def uppercase(str):

    count = 0

    if len(str) == 0:
        print("")

    for i in str:
        count += 1
        letter = ord(i)
        if letter > 96 and letter < 123:
            letter -= 32
        if count < len(str):
            print("{:c}".format(letter), end="")
        else:
            print("{:c}".format(letter))
