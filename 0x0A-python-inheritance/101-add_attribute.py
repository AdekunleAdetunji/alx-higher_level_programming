#!/usr/bin/python3
"""
This module contains function to check wether an object has the capability to
accept new attributes or not
"""

def add_attribute(obj, attr, value):
    """
    This functions takes an object, checks wether it allows for the addition
    of a new attribute

    args
    @obj: The object we want to add enw attribute to
    @attr: The new attribute to be added to the object
    @value: The of the new attribute to be added to object
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
