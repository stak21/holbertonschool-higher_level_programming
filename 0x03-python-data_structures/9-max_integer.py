#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    biggest = None
    for i in my_list:
        if biggest == None:
            biggest = i
        if i > biggest:
            biggest = i
    return biggest
