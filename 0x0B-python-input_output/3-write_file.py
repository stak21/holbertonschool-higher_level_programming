#!/usr/bin/python3
""" Function: write_file """


def write_file(filename="", text=""):
    """ Write a string to a file and return the number of characters """
    with open(filename,"w", encoding="utf-8") as f:
        count = f.write(text)
        return count
