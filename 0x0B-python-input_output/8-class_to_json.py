#!/usr/bin/python3
"""
This module contains a function that gets all the JSON object replica of
python object attribute
"""


import json


def class_to_json(obj):
    """
    Computes JSON serialization of an object

    args
       @obj: Python object
    Return
       Dictionary replica of the attributes of a python class
    """
    return obj.__dict__
