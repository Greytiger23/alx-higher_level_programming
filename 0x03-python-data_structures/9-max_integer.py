#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    a = my_list[0]
    for b in my_list[1:]:
        if b > a:
            a = b
    return a
