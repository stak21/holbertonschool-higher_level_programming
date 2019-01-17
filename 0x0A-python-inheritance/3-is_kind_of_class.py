#!/usr/bin/python3
""" Function is_kind_of_class """


def is_kind_of_class(obj, a_class):
    """ Returns True if the object is an instance of a class """
    if isinstance(obj, a_class):
        return True
    else:
        return False
