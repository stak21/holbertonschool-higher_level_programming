#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy = a_dictionary.copy()
    for value in copy:
        copy[value] *= 2
    return copy
