#!/usr/bin/python3
"""module that defines the file"""


def save_to_json_file(my_obj, filename):
    """defines the file"""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(my_obj, file)
    except Exception as e:
        print("An error occurred: {}".format(e))
