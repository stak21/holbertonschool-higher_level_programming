#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as ve:
        sys.stderr.write("Exception: {}".format(ve.args[0]))
        return False
    else:
        return True