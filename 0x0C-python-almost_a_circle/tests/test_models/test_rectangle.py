#!/usr/bin/python3
"""
This module contains a Unittest class to test the Rectangle class
"""

import io
import unittest
import models.rectangle as rectangle
from unittest import mock
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Module to test the Rectangle class and its functionality
    """
    @classmethod
    def setUpClass(cls):
        """
        Setup the variables to use in the function
        """
        cls.new_class = Rectangle
        cls.obj_1 = Rectangle(1, 2)
        cls.obj_2 = Rectangle(1, 2, 1, 1)

    def test_mod(self):
        """
        Check if the module and class has a documentation
        """
        self.assertTrue(rectangle.__doc__)
        self.assertTrue(Rectangle.__doc__)

    def test_instance(self):
        """
        Check that the Rectangle instantiates correctly
        """
        self.assertTrue(type(self).obj_1)
        self.assertTrue(type(self).obj_2)

    def test_1_inst_arg(self):
        """
        Check that the right error is raised when the class is instantiated
        with only one argument
        """
        self.assertRaises(TypeError, type(self).new_class, 1)

    def test_3_inst_arg(self):
        """
        Check that the class instantiates correctly by passing just three args
        """
        self.assertTrue(type(self).new_class(1, 2, 3))

    def test_5_inst_arg(self):
        """
        Check that the class instantiates correctly when called with four
        """

    def test_priv_height(self):
        """
        Check that the private attributes are not accessible
        """
        with self.assertRaises(AttributeError):
            print(type(self).obj_1.__height)

    def test_priv_width(self):
        """
        Check that the private attributes are not accessible
        """
        with self.assertRaises(AttributeError):
            print(type(self).obj_1.__width)

    def test_priv_x(self):
        """
        Check that the private attributes are not accessible
        """
        with self.assertRaises(AttributeError):
            print(type(self).obj_1.__x)

    def test_priv_y(self):
        """
        Check that the private attributes are not accessible
        """
        with self.assertRaises(AttributeError):
            print(type(self).obj_1.__y)

    def test_wrong_w_inst(self):
        """
        Check for wrong width instance call
        """
        self.assertRaises(TypeError, Rectangle, "a", 1)

    def test_wrong_h_inst(self):
        """
        check for wrong height instantiation
        """
        self.assertRaises(TypeError, Rectangle, 1, "a")

    def test_wrong_w_v_inst(self):
        """
        Check for wrong width value instance call
        """
        self.assertRaises(ValueError, Rectangle, -1, 1)

    def test_wrong_h_v_inst(self):
        """
        Check for wrong height value instance call
        """
        self.assertRaises(ValueError, Rectangle, 1, -1)

    def test_wrong_x_inst(self):
        """
        Check for wrong x value instance call
        """
        self.assertRaises(TypeError, Rectangle, 1, 1, "a")

    def test_wrong_x_v_inst(self):
        """
        Check for wrong x value instance call
        """
        self.assertRaises(ValueError, Rectangle, 1, 1, -1)

    def test_wrong_y_inst(self):
        """
        Check for wrong y value instance call
        """
        self.assertRaises(TypeError, Rectangle, 1, 1, "a")

    def test_wrong_y_v_inst(self):
        """
        Check for wrong y value instance call
        """
        self.assertRaises(ValueError, Rectangle, 1, 1, -1)

    def test_diff_id_type(self):
        """
        check for an id type that is not an integer
        """
        self.assertTrue(Rectangle(1, 1, id="2"))
        self.assertEqual(Rectangle(1, 1, id="3").id, "3")

    def test_wrong_init(self):
        """
        Check that the right error is raised when init is called with
        insufficient number of arguments
        """
        with self.assertRaises(TypeError):
            print(Rectangle())

    def test_wrong_init_2(self):
        """
        Check that the right error is raised when init is called with too
        much arguments
        """
        with self.assertRaises(TypeError):
            print(Rectangle(1, 2, 3, 4, 5, 6))

    def test_area(self):
        """
        Check that the area functionality works properly
        """
        self.assertTrue(type(self).obj_1.area())

    def test_wrong_area(self):
        """
        Validate error raise when the area method is wrongly called
        """
        self.assertRaises(TypeError, type(self).obj_1.area, 1)

    def test_wrong_display(self):
        """
        Validate error raise when the display method is wrongly called
        """
        self.assertRaises(TypeError, type(self).obj_1.display, 1)

    def test_display(self):
        """
        Check that the display functionality works properly
        """
        with mock.patch('builtins.print') as mock_print:
            self.assertFalse(type(self).obj_1.display())

    def test_string(self):
        """
        Check that the display functionality works properly
        """
        with mock.patch('builtins.print') as mock_print:
            print(type(self).obj_1)

    def test_update_args_1(self):
        """
        Check if the update method works with one positional argument
        """
        type(self).obj_1.update(4)
        self.assertEqual(getattr(type(self).obj_1, "id"), 4)
        type(self).obj_1.update(1)

    def test_update_args_1_wrong(self):
        """
        Check if the update method works with one positional argument of
        type other than int
        """
        type(self).obj_1.update("a")
        self.assertEqual(getattr(type(self).obj_1, "id"), "a")
        type(self).obj_1.update(1)

    def test_update_args_2(self):
        """
        Check if the update method works with 2 positional argument other
        """
        type(self).obj_1.update("a", 1)
        self.assertEqual(getattr(type(self).obj_1, "width"), 1)

    def test_update_args_2_wrong(self):
        """
        Check if the update method works with 2 positional argument of
        type other than int
        """
        with self.assertRaises(TypeError):
            type(self).obj_1.update("a", "b")

    def test_update_args_3(self):
        """
        Check if the update method works with 3 positional argument other
        """
        type(self).obj_1.update("a", 1, 2)
        self.assertEqual(getattr(type(self).obj_1, "height"), 2)

    def test_update_args_3_wrong(self):
        """
        Check if the update method works with 3 positional argument of
        type other than int
        """
        with self.assertRaises(TypeError):
            type(self).obj_1.update(1, 2, "b")

    def test_update_args_4(self):
        """
        Check if the update method works with 2 positional argument other
        """
        type(self).obj_1.update(1, 2, 3, 4)
        self.assertEqual(getattr(type(self).obj_1, "x"), 4)

    def test_update_args_4_wrong(self):
        """
        Check if the update method works with one positional argument of
        type other than int
        """
        with self.assertRaises(TypeError):
            type(self).obj_1.update(1, 2, 3, "a")

    def test_update_args_5(self):
        """
        Check if the update method works with 2 positional argument other
        """
        type(self).obj_1.update(1, 2, 3, 4, 5)
        self.assertEqual(getattr(type(self).obj_1, "y"), 5)

    def test_update_args_5_wrong(self):
        """
        Check if the update method works with one positional argument of
        type other than int
        """
        with self.assertRaises(TypeError):
            type(self).obj_1.update(1, 2, 3, 4, "a")
