#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    x = []
    for a in range(0, list_length):
        try:
            b = float(my_list_1[a])
            c = float(my_list_2[a])
            y = b / c
        except (ValueError, TypeError):
            print("wrong type")
            y = 0
        except ZeroDivisionError:
            print("division by 0")
            y = 0
        except IndexError:
            print("out of range")
            y = 0
        finally:
            x.append(y)
    return x
