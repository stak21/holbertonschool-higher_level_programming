#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new = {key: value}
    a_dictionary.update(new)
    return a_dictionary
