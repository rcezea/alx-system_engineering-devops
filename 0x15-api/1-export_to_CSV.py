#!/usr/bin/python3
"""
Using REST API, return info about employee todo list progress
"""
import csv
import requests
import sys


if __name__ == '__main__':

    url = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])

    username = requests.get(url, timeout=10)

    username = username.json()

    username = username.get('username')

    url2 = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            sys.argv[1])

    total = requests.get(url2, timeout=10)

    total = total.json()

    with open("{}.csv".format(sys.argv[1]), "w") as csvfile:
        write = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for i in total:
            status = i.get('completed')
            title = i.get('title')
            data = [sys.argv[1], username, status, title]
            write.writerow(data)
