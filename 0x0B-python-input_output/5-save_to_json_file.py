#!/usr/bin/python3
"""module that defines the file"""
import json


def save_to_json_file(my_obj, filename):
    """defines the file"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
