#!/usr/bin/python3
""" Gets number of subscribers in a subreddit """
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
