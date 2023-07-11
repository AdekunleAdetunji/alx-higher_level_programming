#!/usr/bin/python3
"""
This module contains a function that demonstrate how to use the json.loads
function
"""


import json


def to_json_string(my_obj):
    """
    This function create the JSON representation of an object

    args
       @my_obj: The object whose JSON representation is to be gotten

    Return
       The JSON representation of the object
    """
    return json.dumps(my_obj)
