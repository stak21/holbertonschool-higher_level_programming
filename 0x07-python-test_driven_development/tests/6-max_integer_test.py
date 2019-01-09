#!/usr/bin/python3
"""Unittest"""


import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ First time using Unittest """
    def test(self):
        """ Test a normal case """
        self.assertEqual(max_integer([2,3]), 3)

    def testFail(self):
        """ Test a failing case """
        with self.assertRaises(TypeError):
            max_integer(['f', 3])
    
    def testString(self):
        """ Test a string """
        self.assertEqual(max_integer('ddw'), 'w')

    def testListString(self):
        """ Test a list of strings """
        self.assertEqual(max_integer(['hi', 'bye']), 'hi')


