#!/usr/bin/python3
""" Gets number of subscribers in a subreddit """
import requests as req


def number_of_subscribers(subreddit):
    """ Gets number of subscribers in a subreddit """
    headers = {'User-Agent': 'Ezea Richard'}
    link = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = req.get(url=link, headers=headers).json()
    # if r.status_code != 200:
    #     return 0
    return (r.get("data", {}).get("subscribers", 0))
