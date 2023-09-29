#!/usr/bin/python3
"""
This script send a post request with am email value supplied as cmd linearg
to script to a url supplied to the command line
"""
if __name__ == "__main__":
    import requests
    import sys

    data = {"email": sys.argv[2]}
    resObj = requests.post(sys.argv[1], data=data)
    print(resObj.text)
