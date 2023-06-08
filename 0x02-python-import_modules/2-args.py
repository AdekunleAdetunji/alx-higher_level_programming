#!/usr/bin/python3
import sys

args = sys.argv
argc = len(args) - 1
if __name__ == "__main__":
    if argc == 0:
        print("{:d} arguments.".format(argc))
    else:
        if argc == 1:
            print("{:d} argument:".format(argc))
            print("{:d}: {:s}".format(argc, args[1]))
        else:
            print("{:d} arguments:".format(argc))
            for i in range(1, argc + 1):
                print("{:d}: {:s}".format(i, args[i]))
