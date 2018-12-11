#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not isinstance(my_list, list):
        return None
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[:idx] + [element] + my_list[idx + 1:]
