#!/usr/bin/python3
from models.base import Base
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
