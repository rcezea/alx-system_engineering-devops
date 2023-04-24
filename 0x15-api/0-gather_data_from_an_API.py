#!/usr/bin/python3
"""
Using REST API, return info about employee todo list progress
"""

import requests
from sys import argv

if __name__ == '__main__':
    """
    Using REST API, return info about employee todo list progress
    """

    url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"

    name = requests.get(url).json().get('name')

    url = f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}"

    total = requests.get(url).json()
    done = 0

    for i in total:
        if i.get('completed'):
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, done, len(total)))

    for i in total:
        if i.get('completed'):
            print("\t {}".format(i.get('title')))
