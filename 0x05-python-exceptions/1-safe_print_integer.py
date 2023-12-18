#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        if value is int:
            return True
    except ValueError:
        return False