#!/usr/bin/python3
for a in range(ord('z'), ord('a') - 1, -1):
    print("{}{}".format(chr(a).lower(), chr(a - 1).upper() if  a != ord('a') else ""), end='')
