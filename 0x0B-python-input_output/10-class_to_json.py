#!/usr/bin/python3
import json
""" Function: class_to_json """


def class_to_json(obj):
    """ Returns the dictionary description with simple data structure """
    dic = json.dumps(obj.__dict__)
    return json.loads(dic)
