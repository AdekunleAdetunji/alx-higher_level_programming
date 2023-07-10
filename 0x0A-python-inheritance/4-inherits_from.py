#!/usr/bin/python3
"""
This module contains a function that checks wether a class is a child
of another class
"""


def inherits_from(obj, a_class):
    """
    This function checks an object is a child class of a parent class

    args
    @obj: The childclass to be checked
    @a_class: The parent class
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
