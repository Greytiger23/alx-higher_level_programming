#!/usr/bin/python3
def uppercase(str):
    for a in str:
        b = a
        if 'a' <= a <= 'z':
            b = chr(ord(a) - ord('a') + ord('A'))
        print("{}".format(b), end='')
    print()
