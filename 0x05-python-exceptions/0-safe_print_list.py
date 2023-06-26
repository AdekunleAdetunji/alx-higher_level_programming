#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        idx = 0
        for index in range(x):
            print("{}".format(my_list[index]), end="")
            idx += 1
    except Exception as e:
        pass
    print("")
    return idx
