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
        max_integer(['f', 3])
        raise ValueError("list must be a list of integers")
