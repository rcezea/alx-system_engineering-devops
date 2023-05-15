#!/usr/bin/python3
""" Gets number of subscribers in a subreddit """
import requests


def number_of_subscribers(subreddit):
    """ Gets number of subscribers in a subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Ezea Richard'}
    r = requests.get(url, headers=headers).json()
    # if r.status_code != 200:
    #     return 0
    return (r.get("data", {}).get("subscribers", 0))