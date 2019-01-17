#!/usr/bin/python3
""" Class: MyList """


class MyList(list):
    """ implement method(print_sorted) """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """ prints an assorted list of type int """
        print(sorted(self))
