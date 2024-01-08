#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        a = sorted(self)
        print(a)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
