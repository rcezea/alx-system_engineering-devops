#!/usr/bin/python3
"""
Using REST API, return info about employee todo list progress
"""

from sys import argv
import requests

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

    total_done = [i.get('title') for i in total if i.get('completed')]
    for i in total_done:
        print(i)
