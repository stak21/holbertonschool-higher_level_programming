#!/usr/bin/python3
"""Create a Square class"""


class Square:
    """Addition to Square - compare two squares"""
    def __init__(self, size=0):
        self.size = size

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.size == other.size

    def __ne__(self, other):
        return self.size != other.size

    def __gt__(self, other):
        return self.size > other.size

    def __ge__(self, other):
        return self.size >= other.size

    def __le__(self, other):
        return self.size <= other.size

    def __lt__(self, other):
        return self.size < other.size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(self.size, float) and not isinstance(self.size, int):
            raise TypeError("size must be a number")
        if self.size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.size ** 2
