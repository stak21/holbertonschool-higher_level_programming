#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [replace if word == search else word for word in my_list]
    return new_list
