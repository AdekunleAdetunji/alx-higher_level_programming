#!/usr/bin/python3
"""
This module contains from_json_string() function that deserializes a JSON
string
"""

import json


def from_json_string(my_str):
    """
    This function demonstrates how deserialization of JSON objects work in
    python

    args
       @my_str: The string to be converted to python data structure
    Return
       A valid python string
    """
    return json.loads(my_str)
