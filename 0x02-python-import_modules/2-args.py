#!/usr/bin/python3
from sys import argv
a = len(argv) - 1
if a == 0:
    print("{:d} arguments.".format(a))
if a > 0:
    print("{:d} arguments:".format(a))
    for b, arg in enumerate(argv[1:], start=1):
        print("{:d}: {}".format(b, arg))
