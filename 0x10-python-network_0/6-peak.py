#!/usr/bin/python3
"""""Find the peak of a list of integer
"""


def find_peak(list_of_integers):
    """""Given a list of integers find a peak
    """
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        if list_of_integers[1] > list_of_integers[0]:
            return list_of_integers[1]
        else:
            return list_of_integers[0]

    middle = int(len(list_of_integers) / 2)
    li = list_of_integers
    low = li[middle - 1]
    high = li[middle + 1]
    mid = li[middle]
    if low < mid and high < mid:
        return mid
    """ left side """
    left = find_peak(li[:middle + 1])
    """ right side """
    right = find_peak(li[middle:])

    if left > right:
        return left
    else:
        return right
