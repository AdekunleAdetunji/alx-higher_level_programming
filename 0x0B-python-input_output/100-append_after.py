#!/usr/bin/python3
"""
This module contains a function that inserts a new after a line of string
that contains a particular search string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    reads the content of a file an replaces add a new line of string after
    every line in the file having a particular search string

    args
       @filename: The filename we are reading from
       @search_string: The search string
       @new_string: The replacement string
    """
    result = []
    with open(filename) as fileObj:
        for line in fileObj.readlines():
            result.append(line)
            if search_string in line:
                result.append(new_string)
    with open(filename, 'w') as fileObj:
        for line in result:
            fileObj.write(line)
