#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    a = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000}
    x = 0
    d = 0
    for b in reversed(roman_string):
        c = a[b]
        if c < d:
            x -= c
        else:
            x += c
        d = c
    return x
