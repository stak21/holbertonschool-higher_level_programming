#!/usr/bin/python3
""" Function: read_lines """


def read_lines(filename="", nb_lines=0):
    """ read n lines of a text file and prints it to the stdout """
    count = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            if nb_lines != 0 and count == nb_lines:
                break
            print(line, end="")
            count += 1
