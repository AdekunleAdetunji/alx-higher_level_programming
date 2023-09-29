#!/usr/bin/python3
"""
This is a  Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
if __name__ == "__main__":
    import requests
    import sys

    data = {"q": ""}
    if (len(sys.argv) > 1):
        data["q"] = sys.argv[1]
    resObj = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        json = resObj.json()
        if json:
            print(f"[{json.get('id')}] {json.get('name')}")
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
