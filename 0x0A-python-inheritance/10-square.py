#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
""" Class Square - inherits from Rectangle """


class Square(Rectangle):
    """ implement init and area """
    def __init__(self, size):
        """ instantiate size """
        super().__init__(size, size)

    def area(self):
        """ Return the area of a square """
        return super().area()
