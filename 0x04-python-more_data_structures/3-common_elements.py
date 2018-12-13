#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = []
    [common.append(word) if word in set_2 else word for word in set_1]
    return common
