#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    c = sys.argv
    a = len(c) - 1
    if a == 0:
        print("{:d} arguments.".format(a))
    if a > 1:
        print("{:d} arguments:".format(a))
        for b in range(1, a + 1):
            print("{:d}: {}".format(b, c[b]))
    elif a > 0:
        print("{:d} argument:".format(a))
        print("{:d}: {}".format(a, c[1]))
