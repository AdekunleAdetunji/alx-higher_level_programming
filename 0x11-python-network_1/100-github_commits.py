#!/usr/bin/python3
"""
Use the gihub API to list the commits for a particular github repo
"""
if __name__ == "__main__":
    import requests
    import sys

    owner = sys.argv[1]
    repo = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    autho = "Bearer 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"
    headers = {"Accept": "application/vnd.github+json",
               "Authorization": autho,
               "X-GitHub-Api-Version": "2022-11-28"
               }
    reqObj = requests.get(url, headers=headers)
    for val in reqObj.json():
        print(f"{val.get('sha')}: "
              f"{val.get('commit').get('author').get('name')}")
