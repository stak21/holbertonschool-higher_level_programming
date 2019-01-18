#!/usr/bin/python3
""" Class Student """


class Student:
    """ Extend: attrs """
    def __init__(self, first_name, last_name, age):
        """ instantiate first_name, last_name, age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """
        if attrs is not None:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ Replace all attributes of the Student instance """
        for keys in json.keys():
            self.__dict__[keys] = json[keys]
