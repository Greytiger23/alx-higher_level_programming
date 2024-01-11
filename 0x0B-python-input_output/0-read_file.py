#!/usr/bin/python3
"""defines the read file"""


def read_file(filename=""):
    """defines the filename"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
