#!/usr/bin/python3
import json
""" Function: load_from_json_file """


def load_from_json_file(filename):
    """ Create an object from a "JSON file" """
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            return json.loads(line)
