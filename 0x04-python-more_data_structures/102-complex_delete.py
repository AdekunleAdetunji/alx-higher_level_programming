#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    else:
        for k, v in a_dictionary.copy().items():
            if value == v:
                del a_dictionary[k]

        return a_dictionary
