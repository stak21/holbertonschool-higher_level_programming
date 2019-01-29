#!/usr/bin/python3
""" Class: Base """
import json


class Base:
    """ attr: __nb_objects : method: __init__(id=None) """
    __nb_objects = 0
    class_name = "Base"

    def __init__(self, id=None):
        """ Instantiates id, if id is None increment nb and set id to it """
        if not isinstance(id, int) and id is not None:
            raise TypeError("id must be an integer")
        if id is not None and id < 0:
            raise ValueError("id must be >= 0")
        self.id = id
        if self.id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @classmethod
    def load_from_file(cls):
        """ Retrieve the json formatted dictionary from a file and recreate it
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, "r", encoding="utf-8") as f:
            data = f.read()
        input_li = Base.from_json_string(data)
        ret_li = [cls.create(**obj) for obj in input_li]
        return ret_li

    @classmethod
    def save_to_file(cls, list_objs):
        """ Given a list of instances of a class, serialize each instance and
        save it to a file """
        filename = "{}.json".format(cls.__name__)

        with open(filename, "w", encoding="utf-8") as f:
            json_str = []
            for obj in list_objs:
                json_str.append(cls.to_dictionary(obj))
            json_str = Base.to_json_string(json_str)
            f.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """ Creates an instance of a class from a dictionary """
        if cls.__name__ == "Base":
            return cls(dictionary["id"])
        else:
            ret_cls = cls(1, 1)
        ret_cls.update(**dictionary)
        return ret_cls

    @classmethod
    def _reset(cls):
        """ testing purposes only """
        cls.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns a json string from a list of dictionaries """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Returns a object from a json string """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    def integer_validator(self, name, value, eq=None):
        """ raise an error if its not an integer or if its lte 0 """
        if eq is None:
            raise TypeError("Usage: 'string', value, bool")
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 and eq is False:
            raise ValueError("{} must be >= 0".format(name))
        elif value < 0:
            raise ValueError("{} must be > 0".format(name))
