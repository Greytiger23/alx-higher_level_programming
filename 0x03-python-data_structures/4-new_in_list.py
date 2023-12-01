#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = len(my_list)
    if idx < 0 or idx >= a:
        return my_list
    b = my_list.copy()
    b[idx] = element
    return b
