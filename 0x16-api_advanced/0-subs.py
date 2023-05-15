#!/usr/bin/python3
""" Gets number of subscribers in a subreddit """
import requests as req


def number_of_subscribers(subreddit):
    """ Gets number of subscribers in a subreddit """
    r = req.get("https://www.reddit.com/r/{}/about.json".format(subreddit),
                headers={'User-Agent': 'Ezea Richard'}).json()
    # if r.status_code != 200:
    #     return 0
    return (r.get("data", {}).get("subscribers", 0))
