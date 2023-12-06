#!/usr/bin/python3
def search_replace(my_list, search, replace):
    a = []
    for b in my_list:
        if b == search:
            a.append(replace)
        else:
            a.append(b)
    return a
