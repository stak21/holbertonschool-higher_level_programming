#!/usr/bin/python3
""" function append_write """


def append_write(filename="", text=""):
    """ Append a string at the end of a text file and return the number
    characters """
    with open(filename, "a", encoding="utf-8") as f:
        chars = f.write(text)
        return chars
