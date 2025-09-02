#!/usr/bin/python3

def uppercase(str):

    count = 0

    if str == "":
        print()
        return

    for i in str:
        count += 1
        letter = ord(i)
        if letter > 96 and letter < 123:
            letter -= 32

        if count != len(str):
            end_char = ""
        else:
            end_char = "\n"

        print("{:c}".format(letter), end=end_char)
