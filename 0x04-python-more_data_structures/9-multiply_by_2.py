#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return dict(zip(a_dictionary.keys(), list(map(lambda x: x*2,
                                              a_dictionary.values()))))
