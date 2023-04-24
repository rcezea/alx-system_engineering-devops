#!/usr/bin/python3
"""
Using REST API, return info about employee todo list progress
"""
import requests
import sys


if __name__ == '__main__':

    url = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])

    name = requests.get(url, timeout=10)

    name = name.json()

    name = name.get('name')

    url2 = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            sys.argv[1])

    total = requests.get(url2, timeout=10)

    total = total.json()
    done = 0

    for i in total:
        if i.get('completed'):
            done += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, done, len(total)))

    for i in total:
        if i.get('completed'):
            print("\t {}".format(i.get('title')))
