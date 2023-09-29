#!/usr/bin/python3
"""
A script that takes your GitHub credentials (username and password) and uses
the GitHub API to display your id
"""
if __name__ == "__main__":
    import requests
    import sys

    user = sys.argv[1]
    token = sys.argv[2]
    headers = {"Accept": "application/vnd.github+json",
               "Authorization": f"Bearer {token}",
               "X-GitHub-Api-Version": "2022-11-28"
               }
    resObj = requests.get(f"https://api.github.com/users/{user}",
                          headers=headers)
    print(resObj.json().get("id"))
