#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    """
    Gets number of subscribers in a subreddit
    """
    if subreddit is None:
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Ezea Richard'}
    r = requests.get(url, headers=headers)
    return (r.json()['data']['subscribers'])
