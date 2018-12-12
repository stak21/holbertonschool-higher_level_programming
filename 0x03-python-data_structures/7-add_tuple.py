#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup_ret = ()
    count = 0

    for i, j in zip(tuple_a, tuple_b):
        if count == 2:
            break
        if not i:
            i = 0
        if not j:
            j = 0
        count += 1
        tup_ret += ((i + j),)
    if count == 1:
        if tuple_a[1] >= 0:
            tup_ret += (tuple_a[1],)
        else:
            tuple_ret += (tuple_b[1],)
    if count == 0:
        if tuple_a[0] >= 0:
            return tuple_a
        else:
            return tuple_b
    return tup_ret
