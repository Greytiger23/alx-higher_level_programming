#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    x = []
    try:
        for a in range(list_length):
            try:
                b = float(my_list_1[a])
                c = float(my_list_2[a])
                y = b / c
                x.append(y)
            except (ValueError, TypeError):
                print("wrong type")
                x.append(0)
            except ZeroDivisionError:
                print("division by 0")
                x.append(0)
    except IndexError:
        print("out of range")
    finally:
        return x
