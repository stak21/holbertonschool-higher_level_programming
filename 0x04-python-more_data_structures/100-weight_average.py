#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0
    res = []
    weight = []
    for a in my_list:
        res.append(a[0] * a[1])
        weight.append(a[1])
    return sum(res) / sum(weight)
