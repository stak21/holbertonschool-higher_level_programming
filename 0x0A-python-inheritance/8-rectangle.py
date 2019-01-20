#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" Class Rectangle : subclass of BaseGeomtry """


class Rectangle(BaseGeometry):
    """ define init """
    def __init__(self, width, height):
        """ instantiate private width and height """
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
