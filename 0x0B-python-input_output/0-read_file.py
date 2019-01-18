#!/usr/bin/python3
""" Function: read_file """


def read_file(filename=""):
    """ read from a text file and print it to the stdout """
    with open("my_file_0.txt", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
