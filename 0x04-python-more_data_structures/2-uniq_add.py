#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    [uniq.append(num) if num not in uniq else num for num in my_list]
    return sum(uniq)
