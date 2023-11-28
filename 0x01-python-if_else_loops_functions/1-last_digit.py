#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = abs(number) % 10
if a > 5:
    print(f"Last digit of {number:d} is {a:d} and is greater than 5")
elif a == 0:
    print(f"Last digit of {number:d} is {a:d} and is 0")
elif a < 6 or a < 0:
    print(f"Last digit of {number:d} is {a:d} and is less than 6 and not 0")
