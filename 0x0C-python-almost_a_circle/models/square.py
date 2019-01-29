#!/usr/bin/python3
""" Class: Square """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class: Square of Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Instantiate size, x, y, id """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ String representation of the class """
        return "[Square] ({}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y,
                                                       self.width)

    @property
    def size(self):
        """ Property getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Property setter for size """
        super().integer_validator("size", value, False)
        self.width = value

    def update(self, *args, **kwargs):
        """ Updates the square fields """
        fields = ['id', '_Rectangle__width', '_Rectangle__x', '_Rectangle__y']
        dic_fields = {
                      'id': 'id', 'width': "_Rectangle__width",
                      "height": '_Rectangle__height', "x": '_Rectangle__x',
                      'y': '_Rectangle__y'
                      }
        """ args iteration """
        if args:
            for field, arg in zip(fields, args):
                eq = False
                if field == "x" or field == "y":
                    eq = True
                super().integer_validator(field, arg, eq)
                if field is "_Rectangle__width":
                    self.__dict__[field] = arg
                self.__dict__[field] = arg
        else:
            """ kwargs iteration """
            for key, value in kwargs.items():
                eq = False
                if key == "x" or key == "y":
                    eq = True
                super().integer_validator(key, value, eq)
                if key in "size height" or key is "width":
                    self.__dict__["_Rectangle__width"] = value
                    self.__dict__["_Rectangle__height"] = value
                else:
                    self.__dict__[dic_fields[key]] = value

    def to_dictionary(self):
        """ Returns the dictionary representation of the instance """
        ret_dict = {}
        ret_dict['id'] = self.id
        ret_dict['x'] = self.x
        ret_dict['y'] = self.y
        ret_dict['size'] = self.size

        return ret_dict
