#!/usr/bin/python3
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import unittest
import io
import sys


class TestSquare(unittest.TestCase):
    """ Test the Square class """
    def setUp(self):
        Base._reset()

    def test_parent(self):
        self.sq = Square(1)
        self.assertTrue(isinstance(self.sq, Rectangle))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertEqual(self.sq.id, 1)

    def test_init(self):
        """ test all values """
        self.sq = Square(1, 2, 3, 10)
        self.assertEqual(self.sq.width, 1)
        self.assertEqual(self.sq.height, 1)
        self.assertEqual(self.sq.size, 1)
        self.assertEqual(self.sq.x, 2)
        self.assertEqual(self.sq.y, 3)
        self.assertEqual(self.sq.id, 10)

        """ test default values """
        self.sq = Square(1)
        self.assertEqual(self.sq.x, 0)
        self.assertEqual(self.sq.y, 0)
        self.assertEqual(self.sq.id, 1)

    def test_bad_types(self):
        """ Test bad size types """
        with self.assertRaises(TypeError):
            self.sq = Square('g')
        with self.assertRaises(TypeError):
            self.sq = Square(.3)
        with self.assertRaises(TypeError):
            self.sq = Square([3])
        with self.assertRaises(TypeError):
            self.sq = Square({2: 2})
        with self.assertRaises(TypeError):
            self.sq = Square((2,))

    def test_bad_values(self):
        """ Test bad size values """
        with self.assertRaises(ValueError):
            self.sq = Square(-1)
        """ Test bad x values """
        with self.assertRaises(ValueError):
            self.sq = Square(1, -2)
        """ Test bad y values """
        with self.assertRaises(ValueError):
            self.sq = Square(1, 2, -3)

    def test_etc(self):
        """ Test missing arguments """
        with self.assertRaises(TypeError):
            self.sq = Square()
        """ Too many arguments """
        with self.assertRaises(TypeError):
            self.sq = Square(1, 3, 5, 6, 3, 4, 4)

    def test_area(self):
        """ Test the area method """
        self.sq = Square(4)
        self.assertEqual(self.sq.area(), 16)
        self.sq1 = Square(8, 0, 0, 12)
        self.assertEqual(self.sq1.area(), 64)

    def test_display(self):
        """ Test the display: display will print the sqtangle
        to the std out with '#' """
        self.sq = Square(3)
        cap_out = io.StringIO()
        sys.stdout = cap_out
        self.sq.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(cap_out.getvalue(), "###\n###\n###\n")
        """ Test with x and y """
        self.sq = Square(2, 1, 2)
        cap_out = io.StringIO()
        sys.stdout = cap_out
        self.sq.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(cap_out.getvalue(), "\n\n ##\n ##\n")

    def test_str(self):
        """ Test the __str__ method """
        self.sq = Square(4)
        self.assertEqual(self.sq.__str__(), "[Square] (1) 0/0 - 4")
        """ Test different values no default """
        self.sq = Square(4, 12, 1, 24)
        self.assertEqual(self.sq.__str__(), "[Square] (24) 12/1 - 4")

    def test_update(self):
        """ Test updated rectangle """
        self.sq = Square(10, 10, 10)
        self.assertEqual(self.sq.__str__(), "[Square] (1) 10/10 - 10")
        self.sq.update(98)
        self.assertEqual(self.sq.__str__(), "[Square] (98) 10/10 - 10")
        self.sq.update(98, 2)
        self.assertEqual(self.sq.__str__(), "[Square] (98) 10/10 - 2")
        self.sq.update(98, 2, 3)
        self.assertEqual(self.sq.__str__(), "[Square] (98) 3/10 - 2")
        self.sq.update(98, 2, 3, 4)
        self.assertEqual(self.sq.__str__(), "[Square] (98) 3/4 - 2")
        """ Test update with a dictionary """
        self.sq = Square(10, 10, 10)
        self.assertEqual(self.sq.__str__(), "[Square] (2) 10/10 - 10")
        self.sq.update(id=98)
        self.assertEqual(self.sq.__str__(), "[Square] (98) 10/10 - 10")
        self.sq.update(id=98, size=2)
        self.assertEqual(self.sq.__str__(), "[Square] (98) 10/10 - 2")
        self.sq.update(id=98, size=2, x=4)
        self.assertEqual(self.sq.__str__(), "[Square] (98) 4/10 - 2")
        self.sq.update(id=98, size=2, x=4, y=5)
        self.assertEqual(self.sq.__str__(), "[Square] (98) 4/5 - 2")
        """ Test update with a non_existant field """
        with self.assertRaises(KeyError):
            self.sq.update(chicken=3)
        """ Test update with a bad value """
        with self.assertRaises(TypeError):
            self.sq.update('f')
        with self.assertRaises(TypeError):
            self.sq.update(size='f')
        """ Test with both *args and **kwargs """
        self.sq = Square(1, 2)
        self.sq.update(3, 3, id=9)
        self.assertEqual(self.sq.__str__(), "[Square] (3) 2/0 - 3")

    def test_dictionary(self):
        self.sq = Square(10, 10, 10, 10)
        sq_dict = self.sq.to_dictionary()
        self.assertEqual(sq_dict, {'id': 10, 'x': 10, 'size': 10, 'y': 10})
        self.assertTrue(isinstance(sq_dict, dict))
        self.sq2 = Square(1, 1)
        self.sq2.update(**sq_dict)
        self.assertFalse(self.sq == self.sq2)

    def test_create_cls(self):
        """ Test the function create: returns an instance with all attributes
        set """
        self.s1 = Square(10, 10, 10, 99)
        self.s1_dict = self.s1.to_dictionary()
        self.s2 = Square.create(**self.s1_dict)
        self.assertEqual(self.s2.__str__(), "[Square] (99) 10/10 - 10")
        self.assertTrue(self.s2 is not self.s1)
        self.assertTrue(self.s2 != self.s1)

    def test_loading_from_file(self):
        """ Test the function load_from_file: returns a list of instances """
        self.s1 = Square(1)
        self.s2 = Square(1)
        input_li = [self.s1, self.s2]
        Square.save_to_file(input_li)
        output_li = Square.load_from_file()
        for obj1, obj2 in zip(input_li, output_li):
            self.assertEqual(obj1.__dict__, obj2.__dict__)

if __name__ == '__name__':
    unittest.main()
