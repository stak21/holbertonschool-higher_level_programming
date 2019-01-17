#!/usr/bin/python3
""" Function: is_same_class """


def is_same_class(obj, a_class):
    """ Returns true if the object is exact instance of the specified class """
    if type(obj) is a_class:
        return True
    else:
        return False
