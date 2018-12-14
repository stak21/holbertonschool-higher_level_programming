#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    li = []
    for word in a_dictionary:
            if a_dictionary[word] == value:
                li.append(word)
    for delete in li:
        a_dictionary.pop(delete)
    return a_dictionary
