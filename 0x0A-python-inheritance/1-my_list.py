#!/usr/bin/python3
"""defines the class list"""


class MyList(list):
    """defines the class"""

    def print_sorted(self):
        """public instance method"""
        a = sorted(self)
        print(a)
