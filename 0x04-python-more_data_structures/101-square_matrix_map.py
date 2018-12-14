#!/usr/bin/python3
def square_matrix_map(matrix=[]):
        new = list(map(lambda y: list(map(lambda x: x**2, y)), matrix))
        return new
