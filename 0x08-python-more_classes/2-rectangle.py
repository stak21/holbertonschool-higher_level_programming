#!/usr/bin/python3
""" Create a Rectangle class """


class Rectangle:
    """ build upon a previous project: methods(area, perimeter) """
    def __init__(self, width, height):
        """ initiate fields """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ property setter: width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ property setter: height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ returns the perimeter of the rectangle """
        if self.width is 0 or self.height is 0:
            return 0
        return (2 * self.width) + (2 * self.height)
