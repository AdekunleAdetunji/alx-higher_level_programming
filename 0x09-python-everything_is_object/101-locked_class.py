#!/usr/bin/python3
"""
This module contains a locked class that prevents the addition of a new
instance attribute except the attribute is first_name
"""


class LockedClass():
    """
    This class creates a new  instance that does not allow the allocation of a
    new instance attirbute without it beign first_name
    @attrbs:
    __slots__ = a class attribute of type list with the names of allowed
    attributes
    """

    __slots__ = ["first_name"]
