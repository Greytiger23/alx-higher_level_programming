#!/usr/bin/python3
"""defines the read file"""


def read_file(filename=""):
    """defines the filename"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(file.read(), end="")
    except FileNotFoundError:
        print("File '{}' not found.".format(filename))
    except Exception as e:
        print("An error occurred: {}".format(e))
