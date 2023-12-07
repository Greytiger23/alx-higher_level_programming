#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    a = 0
    b = 0
    for x, y in my_list:
        a += x * y
        b += y
    if b == 0:
        return 0
    c = a / b
    return c
