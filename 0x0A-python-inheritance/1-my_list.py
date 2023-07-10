#!/usr/bin/python3
"""
This module contains a class MyList that inherits from the list class in python

>>> ls_obj = MyList()
>>> ls_obj.print_list()
[]
"""


class MyList(list):
    """
    This class inherits from the list class in python.

    args
    list: This is the class from which the child class is inheriting from
    """

    def print_sorted(self):
        """
        prints the element of the list in a sorted manner
        """
        print(sorted(self))
