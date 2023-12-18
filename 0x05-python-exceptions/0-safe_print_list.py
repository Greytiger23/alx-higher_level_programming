#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        a = 0
        for b in range(x):
            print(my_list[b], end="")
            a += 1
    except IndexError:
        pass
    finally:
        print()
        return a
