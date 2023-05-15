#!/usr/bin/python3
""" prints the titles of the first 10 hot posts listed
for a given subreddit """

import requests as req


def top_ten(subreddit):
    """ prints the titles of the first 10 hot
    posts listed for a given subreddit """
    headers = {'User-Agent': 'Ezea Richard'}
    link = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 10}
    r = req.get(url=link, headers=headers, params=params).json()
    for i in (r.get("data", {}).get("children", 0)):
        print(i.get("data", {}).get("title", 0))
