#!/usr/bin/python3
"""
Using REST API, return info about employee todo list progress
"""


def main():
    import sys
    import requests

    url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"

    name = requests.get(url).json().get('name')

    url = f"https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}"

    total = requests.get(url).json()
    done = 0

    for i in total:
        if i.get('completed'):
            done += 1

    print(f"Employee {name} is done with tasks({done}/{len(total)}):")

    total_done = [i.get('title') for i in total if i.get('completed')]
    for i in total_done:
        print("\t ", i)


if __name__ == '__main__':
    main()
