#!/usr/bin/python3
""" Create a Rectangle class """


class Rectangle:
    """ build upon the previous project: field(number_of_instances) """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ initiates fields """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ returns the rectangle """
        rep = ""
        if not self.area():
            return rep
        for row in range(self.height):
            rep += "#" * self.width
            if row != self.height - 1:
                rep += "\n"
        return rep

    def __repr__(self):
        """ return a string representation of the rectangle """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ deletes the instance """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """ returns private width """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns private height """
        return self.__height

    @height.setter
    def height(self, value):
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
        if self.area() == 0:
            return 0
        return (2 * self.width) + (2 * self.height)
