#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            if not ((isinstance(a, int) or isinstance(a, float))
                    and (isinstance(b, int) or isinstance(b, float))):
                raise TypeError("wrong type")
            val = a / b

        except IndexError as ie:
            print("out of range")
            val = 0

        except TypeError as te:
            print("{}".format(te))
            val = 0

        except ZeroDivisionError as zde:
            print("division by 0")
            val = 0

        finally:
            result.append(val)
    return (result)
