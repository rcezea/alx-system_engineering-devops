#!/usr/bin/python3
"""
Module that extract data from api
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    filename = 'todo_all_employees.json'
    user_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(user_url).json()
    tasks = requests.get(todo_url).json()

    record = {}

    for user in users:
        user_task = []
        for task in tasks:
            if user.get("id") == task.get("userId"):
                row = {
                         "task": task.get('title'),
                         "completed": task.get('completed'),
                         "username": user.get('username')
                         }
                user_task.append(row)
        record[user.get("id")] = user_task

    with open(filename, 'w') as json_file:
        json.dump(record, json_file)
