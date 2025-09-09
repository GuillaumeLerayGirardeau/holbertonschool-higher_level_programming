#!/usr/bin/python3

def roman_to_int(roman_string):
    value = 0
    count = 0
    num = ""
    numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                'M': 1000}
    special = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90}

    if type(roman_string) == str:
        while count < len(roman_string): 
            if roman_string[count] in numbers:
                if count + 1 < len(roman_string):
                    num += roman_string[count] + roman_string[count + 1]
                    if count + 1 < len(roman_string) and num in special:
                        value += special.get(num)
                        count += 1
                    else:
                        value += numbers.get(roman_string[count])
                else:
                    value += numbers.get(roman_string[count])
            count += 1
            num = ""
            
        return value