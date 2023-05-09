#!/usr/bin/python3
import requests
"""A function to query the Reddit API and print the titles of... """


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()["data"]["children"]
    for i in range(min(10, len(data))):
        title = data[i]["data"]["title"]
        print(title)
