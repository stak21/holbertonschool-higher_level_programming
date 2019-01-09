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

    def testMaxAtEnd(self):
        """ Tests max number at the end of a list """
        self.assertEqual(max_integer([3, 2, 4]), 4)

    def testMaxAtBeginning(self):
        """ Tests max number at the beginning of a list """
        self.assertEqual(max_integer([5, 2, 3]), 5)

    def testNegative(self):
        """ Tests using a negative number """
        self.assertEqual(max_integer([-1, 2]), 2)

    def testTwoNegative(self):
        """ Tests using both parameters as negative """
        self.assertEqual(max_integer([-1, -4]), -1)

    def testMaxMiddle(self):
        """ Tests max number in the middle """
        self.assertEqual(max_integer([1,5,2]), 5)

    def testOneNum(self):
        """ Tests one number in the list """
        self.assertEqual(max_integer([1]), 1)

    def testEmpty(self):
        """ Tests an empty list """
        self.assertEqual(max_integer([]), None)
