#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
import unittest


class TestBase(unittest.TestCase):
    """ Testing implementation of a class: Base """
    def setUp(self):
        Base._reset()

    def test_normal(self):
        self.base = Base(5)
        self.assertEqual(self.base.id, 5)
        """ Check if nb_objects incremented """
        self.base = Base()
        self.assertEqual(self.base._Base__nb_objects, 1)
        """ See if it id is set to nb_objects """
        self.base = Base()
        self.assertEqual(self.base.id, 2)

    def test_bad_type(self):
        """ float """
        with self.assertRaises(TypeError):
            self.base = Base(.5)
        """ character """
        with self.assertRaises(TypeError):
            self.base = Base('f')
        with self.assertRaises(TypeError):
            self.base = Base(float("NaN"))
        with self.assertRaises(TypeError):
            self.base = Base(float("Inf"))
        with self.assertRaises(TypeError):
            self.base = Base(-float("Inf"))
        with self.assertRaises(TypeError):
            self.base = Base([2])
        with self.assertRaises(TypeError):
            self.base = Base({2: 5})
        with self.assertRaises(TypeError):
            self.base = Base((1,))

    def test_bad_value(self):
        with self.assertRaises(ValueError):
            self.base = Base(-4)

    def test_arg_count(self):
        with self.assertRaises(TypeError):
            self.base = Base(2, 2)

    def test_json(self):
        self.base = Base()
        """ test one dictionary """
        dic = {'test': 1, 'test2': 2, 'test3': 3}
        lidi = [dic]
        json_dict = self.base.to_json_string(lidi)
        self.assertTrue(isinstance(json_dict, str))
        """ test multiple dictionary """
        dic1 = {'test': 1, 'test2': 2, 'test3': 3}
        lidi = [dic, dic1]
        json_dict = self.base.to_json_string(lidi)
        self.assertTrue(isinstance(json_dict, str))
        """ test empty or None """
        json_dict = self.base.to_json_string([])
        self.assertEqual(json_dict, "[]")
        json_dict = self.base.to_json_string(None)
        self.assertEqual(json_dict, "[]")

    def test_json_to_file(self):
        """ Test save_json: note* 52 characters per dict """
        self.r1 = Rectangle(1, 2)
        Rectangle.save_to_file([self.r1])
        with open("Rectangle.json", "r") as f:
            data = f.read()
            self.assertEqual(len(data), 52)
        self.r2 = Rectangle(3, 4)
        Rectangle.save_to_file([self.r1, self.r2])
        with open("Rectangle.json", "r") as f:
            data = f.read()
            self.assertEqual(len(data), 104)
        """ Test empty list """
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            data = f.read()
            self.assertEqual(len(data), 2)

    def test_from_json(self):
        self.rec = Rectangle(1, 2)
        li = [self.rec.to_dictionary()]
        json_list_input = Rectangle.to_json_string(li)
        from_json = Rectangle.from_json_string(json_list_input)
        self.assertTrue(isinstance(from_json, list))
        self.assertTrue(isinstance(from_json[0], dict))
        """ Test empty or None """
        self.assertEqual(Rectangle.from_json_string(None), [])
        self.assertEqual(Rectangle.from_json_string("[]"), [])

    def test_create_cls(self):
        """ Test the function create: returns an instance with all attributes
        set """
        self.r1 = Rectangle(10, 10, 10)
        self.r1_dict = self.r1.to_dictionary()
        self.r2 = Rectangle.create(**self.r1_dict)
        self.assertEqual(self.r2.__str__(), "[Rectangle] (1) 10/0 - 10/10")
        self.assertTrue(self.r2 is not self.r1)
        self.assertTrue(self.r2 != self.r1)
