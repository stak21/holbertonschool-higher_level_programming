#!/usr/bin/python3
"""Create a Square class"""


class Square:
    """Add to Square- property setter"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(self.size) is not int:
            raise TypeError("size must be an integer")
        if self.size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.size ** 2
