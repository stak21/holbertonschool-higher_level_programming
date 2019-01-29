#!/usr/bin/python3
""" Class: Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Instantiate width, height, x=0, y=0, id=None with getters/setters """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ instantiate Rectangle object """
        super().integer_validator("width", width, False)
        self.width = width
        super().integer_validator("height", height, False)
        self.height = height
        super().integer_validator("x", x, True)
        self.x = x
        super().integer_validator("y", y, True)
        self.y = y
        super().__init__(id)

    def __str__(self):
        """ return id, x/y, width/height """
        return "[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """ Property decorator: getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Property decorator: setter """
        super().integer_validator("width", value, False)
        self.__width = value

    @property
    def height(self):
        """ Property decorator: getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Property decorator: setter """
        super().integer_validator("height", value, False)
        self.__height = value

    @property
    def x(self):
        """ Property decorator: getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ Property decorator: setter """
        super().integer_validator("x", value, True)
        self.__x = value

    @property
    def y(self):
        """ Property decorator: getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ Property decorator: setter """
        super().integer_validator("y", value, True)
        self.__y = value

    def area(self):
        """ Return the area of the rectangle """
        return self.width * self.height

    def display(self):
        """ print the display of the rectangle to the stdout """
        print("\n" * self.y, end="")
        for row in range(self.height):
            print(' ' * self.x, end="")
            print('#' * self.width)

    def update(self, *args, **kwargs):
        """ updates the attributes of the rectangle """
        fields = ['id', '_Rectangle__width', '_Rectangle__height',
                  '_Rectangle__x', '_Rectangle__y']
        dic_fields = {
                      'id': 'id', 'width': "_Rectangle__width",
                      "height": '_Rectangle__height', "x": '_Rectangle__x',
                      'y': '_Rectangle__y'
                      }
        if args:
            for field, arg in zip(fields, args):
                eq = False
                if field == "x" or field == "y":
                    eq = True
                super().integer_validator(field, arg, eq)
                self.__dict__[field] = arg
        else:
            for key, value in kwargs.items():
                eq = False
                if key == "x" or key == "y":
                    eq = True
                super().integer_validator(key, value, eq)
                self.__dict__[dic_fields[key]] = value

    def to_dictionary(self):
        """ Returns a dictionary representation of the object """
        ret_dict = {}
        ret_dict['id'] = self.id
        ret_dict['x'] = self.x
        ret_dict['y'] = self.y
        ret_dict['width'] = self.width
        ret_dict['height'] = self.height

        return ret_dict
