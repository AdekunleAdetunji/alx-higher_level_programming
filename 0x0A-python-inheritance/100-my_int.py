#!/usr/bin/python3
"""
This module contains a class MyInt that inherits from the int class
"""

class MyInt(int):
    """
    This class inherits from the int class and have a modification of the
    int equals and not_equals magic method
    """

    def __eq__(self, other):
        """Inverted equals operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverted not equals operator"""
        return super().__eq__(other)
