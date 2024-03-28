#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    n = len(list_of_integers)
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]
    a = 0
    b = n - 1
    while a < b:
        c = (a + b) // 2
        if list_of_integers[c] > list_of_integers[c + 1]:
            b = c
        else:
            a = c + 1
    return list_of_integers[a]
