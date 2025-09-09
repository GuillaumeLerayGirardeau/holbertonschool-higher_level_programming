#!/usr/bin/python3

def roman_to_int(roman_string):
    value = 0
    count = 0
    if type(roman_string) == str :
        while count < len(roman_string):
            #I
            if roman_string[count] == 'I':
                if count<(len(roman_string)-1) and roman_string[count + 1] == 'X':
                    value += 9
                    count += 1
                elif count<(len(roman_string)-1) and roman_string[count+1] == 'V':
                    value += 4
                    count += 1
                else:
                    value += 1
            #V
            elif roman_string[count] == 'V':
                value += 5
            #X
            elif roman_string[count] == 'X':
                if count<(len(roman_string)-1) and roman_string[count + 1] == 'L':
                    value += 40
                    count += 1
                elif count<(len(roman_string)-1) and roman_string[count + 1]=='C':
                    value += 90
                    count += 1
                else:
                    value += 10
            #L
            elif roman_string[count] == 'L':
                value += 50
            #C
            elif roman_string[count] == 'C':
                value += 100
            #D
            elif roman_string[count] == 'D':
                value += 500
            #M
            elif roman_string[count] == 'M':
                value += 1000
            else:
                return 0
            count += 1

    return value
