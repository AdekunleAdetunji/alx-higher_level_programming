#!/usr/bin/python3
"""
This script sends a get request to a url provided to it on the command line
and prints value of the X-Request-Id found in the header
"""
if __name__ == "__main__":
    import sys
    import urllib.request

    reqObj = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(reqObj) as resObj:
        print(resObj.headers.get('X-Request-Id'))
