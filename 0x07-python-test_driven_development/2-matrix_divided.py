#!/usr/bin/python3
""" Divide a matrix by a given number """


def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError("Must be a matrix")
    elif len(matrix) == 1:
        raise TypeError("Matrix must have atleast 2 lists")
    elif len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size div")
    elif not all(type(val) is int or type(val) is float for val in matrix[0]):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    elif not all(type(val) != int or type(val) != float for val in matrix[1]):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    copy = [row[:] for row in matrix]
    count = 0
    for li in matrix:
        for idx in range(len(li)):
            copy[count][idx] = float(round(copy[count][idx] / div, 2))
        count += 1
    return copy
            
