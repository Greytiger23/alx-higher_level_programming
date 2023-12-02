#!/usr/bin/python3
def no_c(my_string):
    b = ''
    for a in my_string:
        if a.lower() != 'c':
            b += a
    return b
