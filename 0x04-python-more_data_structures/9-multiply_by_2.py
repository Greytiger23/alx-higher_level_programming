#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = {b: c * 2 for b, c in a_dictionary.items()}
    return a
