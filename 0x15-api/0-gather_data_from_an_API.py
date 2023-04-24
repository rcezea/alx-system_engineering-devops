#!/usr/bin/python3
"""
Using REST API, return info about employee todo list progress
"""
import sys
import requests


if __name__ == '__main__':
    """
    Using REST API, return info about employee todo list progress
    """

    url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"

    name = requests.get(url, timeout=10)

    name = name.json()

    name = name.get('name')

    url2 = f"https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}"

    total = requests.get(url2, timeout=10)

    total = total.json()
    done = 0

    for i in total:
        if i.get('completed'):
            done += 1

    print(f"Employee {name} is done with tasks({done}/{len(total)}):")

    for i in total:
        if i.get('completed'):
            print(f"\t {i.get('title')}")
