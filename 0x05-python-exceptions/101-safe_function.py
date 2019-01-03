#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except ZeroDivisionError as zde:
        sys.stderr.write("Exception: {}\n".format(zde.args[0]))
    except IndexError as ie:
        sys.stderr.write("Exception: {}\n".format(ie.args[0]))
    except:
        raise
        return None
