#!/usr/bin/python3
"""
This module contains a function lookup() that returns a list of all the methods
and attributes associated with an object
"""


def lookup(obj):
    """
    This functions takes an object and returns the attributes and methods
    associated with the function

    Args
    @obj: The object whose attributes are to be printed
    """
    return (dir(obj))
