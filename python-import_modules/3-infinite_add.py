#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    length = len(argv) - 1
    num = 1
    total = 0
    while num <= length:
        total += int(argv[num])
        num += 1
    print(f"{total}")
