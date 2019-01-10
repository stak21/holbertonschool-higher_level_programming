#!/usr/bin/python3
""" A simple functino that adds 2 integers and returns the result """


def add_integer(a, b=98):
    """ Given 2 variables, return the addition them """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
