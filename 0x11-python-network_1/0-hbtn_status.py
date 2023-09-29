#!/usr/bin/python3
"""
This script sends an HTTP request to a specific url using urllib and prints the
response in a particular format to stdout
"""
if __name__ == "__main__":
    import urllib.request

    reqObj = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(reqObj) as resObj:
        content = resObj.read()
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")
