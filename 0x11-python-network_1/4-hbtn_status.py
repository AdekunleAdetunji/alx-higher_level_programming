#!/usr/bin/python3
"""
A script that request for a resource from a url and prints to stdout the
content of the response body
"""
if __name__ == "__main__":
    import requests

    resObj = requests.get("https://alx-intranet.hbtn.io/status")
    content = resObj.text
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
