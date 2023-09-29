#!/usr/bin/python3
"""
This script send a request to a url supplied to the script as cmd lind argument
and prints the output provided there is not error or "Error code: " followed by
the response error code provided an error is encountered
"""
if __name__ == "__main__":
    import requests
    import sys

    resObj = requests.get(sys.argv[1])
    code = resObj.status_code
    if code < 400:
        print(resObj.text)
    else:
        print(f"Error code: {code}")
