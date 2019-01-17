#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" Class Rectangle - inherits from BaseGeometry """


class Rectangle(BaseGeometry):
    """ Implement area and __str__ """
    def __init__(self, width, height):
        """ Positive values """
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ Return: the area of the Rectangle """
        return self.__width * self.__height
