#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for values in sorted(a_dictionary):
        print("{}: {}".format(values, a_dictionary.get(values)))
