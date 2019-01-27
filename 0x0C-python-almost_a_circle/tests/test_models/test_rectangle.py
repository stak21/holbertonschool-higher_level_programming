#!/usr/bin/python3
from models.rectangle import Rectangle
from models.base import Base
import sys
import io
import unittest


class TestRectangle(unittest.TestCase):
    """ Test the Rectangle class """
    def setUp(self):
        Base._reset()

    def test_parent(self):
        self.rec = Rectangle(1, 2)
        self.assertTrue(isinstance(self.rec, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertEqual(self.rec.id, 1)
        self.rec = Rectangle(1, 2)
        self.rec = Rectangle(1, 2)
        self.rec = Rectangle(1, 2)
        self.assertEqual(self.rec.id, 4)

    def test_init(self):
        """ test all values """
        self.rec = Rectangle(1, 2, 3, 4, 10)
        self.assertEqual(self.rec.width, 1)
        self.assertEqual(self.rec.height, 2)
        self.assertEqual(self.rec.x, 3)
        self.assertEqual(self.rec.y, 4)
        self.assertEqual(self.rec.id, 10)

        """ test default values """
        self.rec = Rectangle(1, 2)
        self.assertEqual(self.rec.x, 0)
        self.assertEqual(self.rec.y, 0)
        self.assertEqual(self.rec.id, 1)

    def test_bad_types(self):
        """ Test bad width types """
        with self.assertRaises(TypeError):
            self.rec = Rectangle('g', 1)
        with self.assertRaises(TypeError):
            self.rec = Rectangle(.3, 1)
        with self.assertRaises(TypeError):
            self.rec = Rectangle([3], 1)
        with self.assertRaises(TypeError):
            self.rec = Rectangle({2: 2}, 1)
        with self.assertRaises(TypeError):
            self.rec = Rectangle((2,), 1)
        """ Test bad height types """
        with self.assertRaises(TypeError):
            self.rec = Rectangle(1, 'g')
        with self.assertRaises(TypeError):
            self.rec = Rectangle(1, 1.2)
        with self.assertRaises(TypeError):
            self.rec = Rectangle(1, [3])
        with self.assertRaises(TypeError):
            self.rec = Rectangle(1, {2: 2})
        with self.assertRaises(TypeError):
            self.rec = Rectangle(1, (2,))
        """ Test bad x types """
        with self.assertRaises(TypeError):
            self.rec = Rectangle(1, 2, 'g')
        with self.assertRaises(TypeError):
            self.rec = Rectangle(1, 2, 1.2)
        with self.assertRaises(TypeError):
            self.rec = Rectangle(1, 2, [3])
        with self.assertRaises(TypeError):
            self.rec = Rectangle(1, 2, {2: 2})
        with self.assertRaises(TypeError):
            self.rec = Rectangle(1, 2, (2,))
        """ Test bad y types """
        with self.assertRaises(TypeError):
            self.rec = Rectangle(1, 2, 3, 'g')
        with self.assertRaises(TypeError):
            self.rec = Rectangle(1, 2, 3, 1.2)
        with self.assertRaises(TypeError):
            self.rec = Rectangle(1, 2, 3, [3])
        with self.assertRaises(TypeError):
            self.rec = Rectangle(1, 2, 3, {2: 2})
        with self.assertRaises(TypeError):
            self.rec = Rectangle(1, 1, 1, (2,))

    def test_bad_values(self):
        """ Test bad width values """
        with self.assertRaises(ValueError):
            self.rec = Rectangle(-1, 2)
        """ Test bad height values """
        with self.assertRaises(ValueError):
            self.rec = Rectangle(1, -2)
        """ Test bad x values """
        with self.assertRaises(ValueError):
            self.rec = Rectangle(1, 2, -2)
        """ Test bad y values """
        with self.assertRaises(ValueError):
            self.rec = Rectangle(1, 2, 2, -3)

    def test_etc(self):
        """ Test missing arguments """
        with self.assertRaises(TypeError):
            self.rec = Rectangle(1)
        with self.assertRaises(TypeError):
            self.rec = Rectangle()
        """ Test too many arguments """
        with self.assertRaises(TypeError):
            self.rec = Rectangle(1, 2, 3, 4, 5, 6)

    def test_area(self):
        """ Test the area method """
        self.rec = Rectangle(4, 2)
        self.assertEqual(self.rec.area(), 8)
        self.rec1 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(self.rec1.area(), 56)

    def test_display(self):
        """ Test the display: display will print the rectangle
        to the std out with '#' """
        self.rec = Rectangle(3, 3)
        cap_out = io.StringIO()
        sys.stdout = cap_out
        self.rec.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(cap_out.getvalue(), "###\n###\n###\n")
        """ Test with x and y """
        self.rec = Rectangle(2, 3, 1, 2)
        cap_out = io.StringIO()
        sys.stdout = cap_out
        self.rec.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(cap_out.getvalue(), "\n\n ##\n ##\n ##\n")

    def test_str(self):
        """ Test the __str__ method """
        self.rec = Rectangle(4, 5)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (1) 0/0 - 4/5")
        """ Test different values no default """
        self.rec = Rectangle(4, 5, 12, 1, 24)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (24) 12/1 - 4/5")

    def test_update(self):
        """ Test updated rectangle """
        self.rec = Rectangle(10, 10, 10, 10)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        self.rec.update(98)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (98) 10/10 - 10/10")
        self.rec.update(98, 2)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (98) 10/10 - 2/10")
        self.rec.update(98, 2, 3)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (98) 10/10 - 2/3")
        self.rec.update(98, 2, 3, 4)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (98) 4/10 - 2/3")
        self.rec.update(98, 2, 3, 4, 5)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (98) 4/5 - 2/3")
        """ Test update with a dictionary """
        self.rec = Rectangle(10, 10, 10, 10)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (2) 10/10 - 10/10")
        self.rec.update(id=98)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (98) 10/10 - 10/10")
        self.rec.update(id=98, width=2)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (98) 10/10 - 2/10")
        self.rec.update(id=98, width=2, height=3)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (98) 10/10 - 2/3")
        self.rec.update(id=98, width=2, height=3, x=4)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (98) 4/10 - 2/3")
        self.rec.update(id=98, width=2, height=3, x=4, y=5)
        self.assertEqual(self.rec.__str__(), "[Rectangle] (98) 4/5 - 2/3")
        """ Test update with a non_existant field """
        with self.assertRaises(KeyError):
            self.rec.update(chicken=3)
        """ Test update with a bad value """
        with self.assertRaises(TypeError):
            self.rec.update('f')
        with self.assertRaises(TypeError):
            self.rec.update(width='f')
        """ Test with both *args and **kwargs """
        self.rec1 = Rectangle(1, 2)
        self.rec1.update(3, 3, id=9)
        self.assertEqual(self.rec1.__str__(), "[Rectangle] (3) 0/0 - 3/2")

    def test_dictionary(self):
        self.rec = Rectangle(10, 10, 10, 10, 10)
        rec_dict = self.rec.to_dictionary()
        self.assertEqual(rec_dict, {'x': 10, 'y': 10, 'id': 10,
                                    'height': 10, 'width': 10})
        self.assertTrue(isinstance(rec_dict, dict))
        self.rec2 = Rectangle(1, 1)
        self.rec2.update(**rec_dict)
        self.assertFalse(self.rec == self.rec2)

    def test_to_json(self):
        self.rec = Rectangle(10, 10, 10, 10, 10)
        rec_dict = self.rec.to_dictionary()
        json_dict = Base.to_json_string([rec_dict])
        self.assertTrue(isinstance(json_dict, str))

    def test_save_json(self):
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
        """ Test the function from_json_string: returns a list of strings """
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


if __name__ == '__name__':
    unittest.main()
