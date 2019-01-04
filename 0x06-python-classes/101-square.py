#!/usr/bin/python3
"""Write a Square class"""


class Square:
    """Addition to Square - be able to print the Square by printing Square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def __repr__(self):
        ret_str = ""
        if self.size <= 0:
            return ret_str
        elif self.position[1] > 0:
            for newline in range(self.position[1]):
                ret_str += "\n"
        for count in range(self.size):
            ret_str += self.position[0] * " "
            ret_str += self.size * "#"
            ret_str += '\n'
        return ret_str[0:-1]

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if not isinstance(self.position, tuple) or len(self.position) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        if not all(type(n) is int for n in self.position):
            raise TypeError("position must be a tuple of 2 positive integer")
        if not all(n >= 0 for n in self.position):
            raise TypeError("position must be a tuple of 2 positive integer")

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size < 0:
            print("")
        elif self.position[1] > 0:
            for newline in range(self.position):
                print("")
        else:
            for count in range(self.size):
                print(" " * count)
                print("#" * count)
