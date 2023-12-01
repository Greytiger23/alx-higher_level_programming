#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = [int(b) for b in argv[1:]]
    c = sum(a)
    print(c)
