#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not value:
        return a_dictionary
    a_dictionary = {a: b for a, b in a_dictionary.items() if b != value}
    return a_dictionary
