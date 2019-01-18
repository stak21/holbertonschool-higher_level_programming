#!/usr/bin/python3
""" Function: pascal_triangle """


def pascal_triangle(n):
    """ return a list of lists of integers representing Pascal's triangle """
    li = [[1]]
    if n <= 0:
        return []
    for row in range(1, n):
        li.append([1])
        for count in range(row):
            try:
                num = li[row - 1][count + 1] + li[row - 1][count]
            except:
                num = 1
            if row - 1 == count:
                num = 1
            li[row].append(num)
    return li
