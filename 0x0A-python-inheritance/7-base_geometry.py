#!/usr/bin/python3
""" Class: BaseGemotry """


class BaseGeometry:
    """ Implement integer_validator """
    def area(self):
        """ raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ raise an error if its not an integer or if its lte 0 """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
