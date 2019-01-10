#!/usr/bin/python3
""" Create a Rectangle class """


class Rectangle:
    """ build upon the previous project: method(str) """
    def __init__(self, width=0, height=0):
        """ initiates fields """
        self.height = height
        self.width = width

    def __str__(self):
        """ return a string representation of the rectangle """
        rep = ""
        if not self.area():
            return rep
        for row in range(self.height):
            rep += "#" * self.width
            if row != self.height - 1:
                rep += "\n"
        return rep

    @property
    def width(self):
        """ Returns private width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Property sets width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Returns private height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Property sets height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of a rectangle """
        return self.width * self.height

    def perimeter(self):
        """ returns the perimeter of a rectangle """
        if self.height is 0 or self.width is 0:
            return 0
        return (2 * self.width) + (2 * self. height)
