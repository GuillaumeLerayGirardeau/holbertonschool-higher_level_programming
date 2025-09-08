#!/usr/bin/python3

def check_doubles(doubles, num):
    for i in doubles:
        if i == num:
            return False
    return True


def uniq_add(my_list=[]):

    doubles = []
    result = 0
    count = 0

    for i in my_list:
        if count == 0:
            result += i
            doubles.append(i)
            count += 1
        else:
            if check_doubles(doubles, i):
                result += i
                doubles.append(i)

    return result
