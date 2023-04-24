#!/usr/bin/python3
"""
Using REST API, return info about employee todo list progress
"""
import json
import requests
import sys


if __name__ == '__main__':

    id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)

    username = requests.get(url, timeout=10)

    username = username.json()

    username = username.get('username')

    url2 = "https://jsonplaceholder.typicode.com/todos?userId={}".format(id)

    total = requests.get(url2, timeout=10)

    total = total.json()

    row = []
    for i in total:
        status = i.get('completed')
        title = i.get('title')
        data = {"task": title, "completed": status, "username": username}
        row.append(data)

    with open("{}.json".format(id), "w") as json_file:
        tionary = {id: row}
        json.dump(tionary, json_file)
