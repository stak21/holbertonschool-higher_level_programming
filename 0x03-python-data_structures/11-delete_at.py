#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not isinstance(my_list, list):
        return None
    if idx < 0 or idx >= len(my_list):
        return my_list
    newlist = []
    for i in my_list:
        if my_list[idx] != i:
            newlist.append(i)
    del my_list[idx]
    return newlist
