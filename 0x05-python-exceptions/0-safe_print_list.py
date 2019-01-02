#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0

    try:
        for idx in range(x):
            print("{:d}".format(my_list[idx]), end="")
            count += 1
    except IndexError:
        print("")
        return count
    else:
        print("")
        return count
