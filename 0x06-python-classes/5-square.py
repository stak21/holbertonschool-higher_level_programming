#!/usr/bin/python3
"""Write a Square class"""


class Square:
    """Addition to Square- create a instance method my_print()"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size > 0:
            for row in range(self.__size):
                for collumn in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
