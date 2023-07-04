#!/usr/bin/python3
"""
This module contains the say_my_name() function
Usage:
>>> say_my_name('Adetunji')
Adetunji
"""


def say_my_name(first_name, last_name=''):
    """
    This function prints to the stdout a message in the output
    format: 'My name is first_name last_name'

    Args
    @first_name: The first positional argument
    @last_name: The second positional argument or keyword argument
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
