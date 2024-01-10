#!/usr/bin/python3
"""module that defines the list"""


def load_from_json_file(filename):
    """defines the file"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            json_data = json.load(file)
            return json_data
    except Exception as e:
        print("An error occurred: {}".format(e))
        return None

