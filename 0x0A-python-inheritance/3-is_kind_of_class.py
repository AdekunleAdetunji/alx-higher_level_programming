#!/usr/bin/python3
"""
This module contains a function that checks wether a object is
an instance of a class or inherited from a class
"""


def is_kind_of_class(obj, a_class):
    """
    checks wether two objects share similar parent classes

    args
    @obj: The object to be tested against a class
    @a_class: The class to be compared against
    """
    return isinstance(obj, a_class)
