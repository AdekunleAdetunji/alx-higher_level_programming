#!/usr/bin/python3
"""
This module contains a unittest subclass to be used in testing the max_integer
function of the 6-max_integer module
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """A subclass of containing each test case for the max_integer function"""

    def test_norm(self):
        """Test normal use of the function"""
        self.assertEqual(max_integer([1, 2]), 2)

    def test_empty(self):
        """Test for an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_multiple(self):
        """Test for a list with non-unique values"""
        self.assertEqual(max_integer([1, 1, 3, 4]), 4)
        self.assertEqual(max_integer('ab'), 'b')

    def test_error(self):
        """Test for the behaviour of funtion when a non-iterable is supplied"""
        self.assertRaises(TypeError, max_integer, 2)

    def test_mixed(self):
        """Test for the behaviour of function when an iterable of mixed object
        types is supplied"""
        self.assertRaises(TypeError, max_integer, ['a', 1, 3, []])

    def test_str_array(self):
        """Test for the behaviour of function when a list of strings is
        supplied"""
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')

    def test_list_array(self):
        """Test for the behaviour of function when a list of list is
        supplied"""
        self.assertEqual(max_integer([[1], []]), [1])

    def test_none(self):
        """Test for a the behaviour of function when a None type is supplied"""
        self.assertRaises(TypeError, max_integer, None)

    def test_float(self):
        """Test for the behaviour of function when an array of float is
        supplied"""
        self.assertEqual(max_integer([1.1, 2.2, 1.5, 5.2]), 5.2)

    def test_digitmix(self):
        """Test for function behaviour when an array mix of float and integers
        is supplied"""
        self.assertEqual(max_integer([1, 0.4, 2, 1.4, 5.2, 4.8]), 5.2)
