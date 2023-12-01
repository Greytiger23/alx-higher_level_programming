#!/usr/bin/python3
def magic_calculation(a, b):
    d = __import__('magic_calculation_102').add
    s = __import__('magic_calculation_102').sub
    if a < b:
        x = add(a, b)
        for y in range(4, 6):
            x = add(x, y)
        return x
    else:
        return sub(a, b)
