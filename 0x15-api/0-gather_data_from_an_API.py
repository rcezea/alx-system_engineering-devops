#!/usr/bin/python3
"""
Using REST API, return info about employee todo list progress
"""

import requests
import sys


if __name__ == '__main__':
    url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"

    name = requests.get(url).json().get('name')

    url = f"https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}"

    total = requests.get(url).json()
    done = 0

    for i in total:
        if i.get('completed'):
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, done, len(total)))

    total_done = [i.get('title') for i in total if i.get('completed')]
    for i in total_done:
        print("\t ", i)
