#!/usr/bin/python3
"""
This module contains read_file() function demonstrating
how to use the read() function in python
"""


def read_file(filename=""):
    """
    This function reads a file encoded in utf-8 format and
    prints it to the stdout

    args
    @filename: The file whose content is to be read
    """

    with open(filename, encoding="utf-8") as fileObj:
        print(fileObj.read(), end='')
