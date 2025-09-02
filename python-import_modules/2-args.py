#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    length = len(argv) - 1
    if length > 1:
        end_line = "arguments:\n"
    elif length == 1:
        end_line = "argument:\n"
    else:
        end_line = "arguments.\n"
    print("{:d} ".format(length), end=end_line)

    if length > 0:
        num_arg = 1
        while num_arg <= length:
            print(f"{num_arg}:", argv[num_arg])
            num_arg += 1
