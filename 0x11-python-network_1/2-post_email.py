#!/usr/bin/python3
"""
This script sends a post request with email data to a url supplied as first
argument to the script at runtime
"""
if __name__ == "__main__":
    import sys
    import urllib.parse
    import urllib.request

    data = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(data)
    data = data.encode("ascii")
    reqObj = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(reqObj) as resObj:
        print(resObj.read().decode("utf-8"))
