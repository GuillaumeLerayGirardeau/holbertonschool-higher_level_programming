#!/usr/bin/python3

def roman_to_int(roman_string):
    x = roman_string
    value = 0
    count = 0
    if type(x) is str:
        while count < len(x):
            # I
            if x[count] == 'I':
                if count < (len(x) - 1) and x[count + 1] == 'X':
                    value += 9
                    count += 1
                elif count < (len(x) - 1) and x[count + 1] == 'V':
                    value += 4
                    count += 1
                else:
                    value += 1
            # V
            elif x[count] == 'V':
                value += 5
            # X
            elif x[count] == 'X':
                if count < (len(x) - 1) and x[count + 1] == 'L':
                    value += 40
                    count += 1
                elif count < (len(x) - 1) and x[count + 1] == 'C':
                    value += 90
                    count += 1
                else:
                    value += 10
            # L
            elif x[count] == 'L':
                value += 50
            # C
            elif x[count] == 'C':
                value += 100
            # D
            elif x[count] == 'D':
                value += 500
            # M
            elif x[count] == 'M':
                value += 1000
            else:
                return 0
            count += 1

    return value
