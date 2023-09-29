#!/usr/bin/python3
"""
This script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8)
"""
if __name__ == "__main__":
    import sys
    import urllib.request

    reqObj = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(reqObj) as resObj:
            print(resObj.read().decode("utf-8"))
    except urllib.request.HTTPError as e:
        print(f"Error code: {e.code}")
