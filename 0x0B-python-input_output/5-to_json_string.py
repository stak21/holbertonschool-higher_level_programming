#!/usr/bin/python3
import json
""" Function: to_json_string """


def to_json_string(my_obj):
    """ return the JSON representation of an object """
    return json.dumps(my_obj, sort_keys=True)
