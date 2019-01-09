#!/usr/bin/python3
""" Function: print a string with two parameters """


def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name is "":
        print("My name is {:s}".format(first_name))
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
