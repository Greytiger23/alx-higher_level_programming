#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        x = a / b
    except ZeroDivisionError:
        x = None
    finally:
        if x is not None:
            print("Inside result: {}".format(x))
        else:
            print("Inside result: None")
        return x
