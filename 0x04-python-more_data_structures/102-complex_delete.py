#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    x = {a for a, b in a_dictionary.items() if b == value}
    for a in x:
        del a_dictionary[a]
    return a_dictionary
