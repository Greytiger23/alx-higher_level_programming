#!/usr/bin/python3
"""modules that define the list"""


import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_items_to_list_and_save(arguments):
    """defines the list"""
    try:
        existing_data = load_from_json_file("add_item.json") or []
        existing_data.extend(arguments)
        save_to_json_file(existing_data, "add_item.json")
        print("Items added to add_item.json: {}".format(arguments))
    except Exception as e:
        print("An error occurred: {}".format(e))

script_name = sys.argv[0]
arguments = sys.argv[1:]

add_items_to_list_and_save(arguments)
