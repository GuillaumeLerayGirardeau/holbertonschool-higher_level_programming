#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
if number < 0:
    last_digit *= -1
    
if last_digit > 5:
    result = "is greater than 5"
elif last_digit <= 5 and last_digit != 0:
    result = "is less than 6 and not 0"
else:
    result = "is 0"

print(f"Last digit of {number} is {last_digit} and {result}")
    