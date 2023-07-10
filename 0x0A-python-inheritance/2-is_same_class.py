#!/usr/bin/python3
"""
This module contains a function that checks wether a function is an instance
of a class
"""


def is_same_class(obj, a_class):
    """Function to check if an object is an instance of a class"""
    return type(obj) == a_class
