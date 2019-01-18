#!/usr/bin/python3
""" Class Student """


class Student:
    """ Method: __init__, to_json """
    def __init__(self, first_name, last_name, age):
        """ instantiate first_name, last_name, age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def first_name(self):
        """ return first_name """
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        """ Set a private first_name """
        self.__first_name = value

    @property
    def last_name(self):
        """ return last_name """
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        """ Set a private last_name """
        self.__last_name = value

    @property
    def age_name(self):
        """ return age_name """
        return self.__age_name

    @age_name.setter
    def age_name(self, value):
        """ Set a private age_name """
        self.__age_name = value

    def to_json(self):
        """ Retrieves a dictionary representation of a Student instance """
        return self.__dict__
