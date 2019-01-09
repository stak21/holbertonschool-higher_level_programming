#!/usr/bin/python3
""" print_square: prints a square with '#' """


def print_square(size):
    """ given size, print a column and row of '#' """
    if type(size) is not int or type(size) is float:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        print("#" * size)
