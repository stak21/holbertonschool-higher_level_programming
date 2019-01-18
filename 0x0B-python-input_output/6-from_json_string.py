#!/usr/bin/python3
import json
""" Function: from_json_string """


def from_json_string(my_str):
    """ Return an object represented by JSON string """
    return json.loads(my_str)
