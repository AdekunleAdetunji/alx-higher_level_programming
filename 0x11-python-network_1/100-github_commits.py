#!/usr/bin/python3
"""
Use the gihub API to list the commits for a particular github repo
"""
if __name__ == "__main__":
    import requests
    import sys

    owner = sys.argv[2]
    repo = sys.argv[1]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    resObj = requests.get(url)
    try:
        commits = resObj.json()
        for i in range(10):
            print(f"{commits[i].get('sha')}: "
                  f"{commits[i].get('commit').get('author').get('name')}")
    except IndexError:
        pass
