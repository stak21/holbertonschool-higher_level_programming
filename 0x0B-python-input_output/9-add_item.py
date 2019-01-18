#!/usr/bin/python3
import sys
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file
save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
""" Script: adds all arguments to a Python list and save them to a file """

filename = "add_item.json"
with open(filename, 'a', encoding="utf-8") as f:
    pass
existing_li = load_from_json_file(filename)
with open(filename, "w+") as f:
    for args in sys.argv[1:]:
        if existing_li is None:
            existing_li = []
        existing_li.append(args)
    save_to_json_file(existing_li, filename)
