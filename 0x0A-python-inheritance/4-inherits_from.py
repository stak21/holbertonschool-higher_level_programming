#!/usr/bin/python3
""" Function: inherits_from """


def inherits_from(obj, a_class):
    """ Returns true if the object is an instance of the given class """
    if isinstance(obj, a_class):
        return True
    else:
        return False
