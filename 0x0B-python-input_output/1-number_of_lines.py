#!/usr/bin/python3
""" Function: number_of_lines """


def number_of_lines(filename=""):
    """ returns the number of lines of a text file """
    count = 0
    with open(filename, encoding="utf-8") as f:
        while f.readline() != "":
            count += 1
    return count
