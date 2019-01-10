#!/usr/bin/python3
""" Create a Rectangle class """


class Rectangle:
    """ build upon the previous project: attributes(width, height) """
    def __init__(self, width=0, height=0):
        """ initiate fields """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ property getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ property setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ property getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ property setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
