#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as ve:
        tmp = ve.args
        sys.stderr.write(tmp[0])
        return False
    else:
        return True
