#!/usr/bin/python3
"""
This module contains various test cases for the base module
"""

import unittest
import models.base as base
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Create the various test cases for the base class

    args
       @unittest.TestCase: The parent class that the TestBase class inherits
        from
    """
    @classmethod
    def setUpClass(cls):
        """
        Setup the variables that will be used in testing the functionality of
        the base class
        """
        cls.base_1 = Base()
        cls.base_2 = Base(3)

    def test_mod_doc(self):
        """
        Check that the base module has a documentation
        """
        self.assertTrue(base.__doc__)

    def test_doc(self):
        """
        Check that class and class module has a documentation
        """
        self.assertTrue(Base.__doc__)

    def test_existence(self):
        """
        Check if the Base class exists
        """
        self.assertTrue(self.base_1)

    def test_nb_instance(self):
        """
        Check that the nb_instance on the first call is 1
        """
        self.assertEqual(self.base_1.id, 1)

    def test_diff_call(self):
        """
        Test behaviour of class when called with the different number of
        arguments
        """
        self.assertTrue(Base(1))

    def test_wrong_call(self):
        """
        Check class behaviour when called with the wrong
        """
        self.assertRaises(TypeError, Base, id=2, name=3)

    def test_null_ins_att(self):
        """
        Check for non-existent instance attribute
        """
        self.assertRaises(AttributeError, getattr, self.base_1, "a")

    def test_inst_att(self):
        """
        Check for an existing class attribute
        """
        self.assertTrue(getattr(self.base_1, "id"))

    def test_id_call(self):
        """
        Check that the id is set with a class call with id argument supplied
        """
        self.assertEqual(getattr(self.base_2, "id"), 3)

    def test_private(self):
        """
        Check wether private class attribute is accessible from outside
        """
        with self.assertRaises(AttributeError):
            print(self.base_1.__nb_instance)

    @classmethod
    def tearDownClass(cls):
        cls.tearDown
