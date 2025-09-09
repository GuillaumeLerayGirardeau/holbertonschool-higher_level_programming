#!/usr/bin/python3

def roman_to_int(roman_string):
    value = 0
    last = 0
    if type(roman_string) is str:

        numbers = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        for i in reversed(roman_string):
            if i in numbers:
                if numbers.get(i) < last:
                    value -= numbers.get(i)
                else:
                    value += numbers.get(i)
                last = numbers.get(i)

    return value
