#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        a = 0
        for b in range(x):
            if type(my_list[b]) is int:
                print("{:d}".format(my_list[b]), end="")
                a += 1
    except (ValueError, TypeError):
        pass
    print("")
    return a
