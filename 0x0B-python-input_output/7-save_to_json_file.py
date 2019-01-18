#!/usr/bin/python3
import json
""" Function: save_to_json_file """


def save_to_json_file(my_obj, filename):
    """ Writes an Object to a file, using JSON representation """
    with open(filename, "a", encoding="utf_8") as f:
        f.write(json.dumps(my_obj))
