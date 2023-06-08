#!/usr/bin/python3
import sys

argv = sys.argv
argc = len(argv) - 1
sumation = 0
if __name__ == "__main__":
    for i in range(1, argc + 1):
        value = int(argv[i])
        sumation += value
    print("{:d}".format(sumation))
