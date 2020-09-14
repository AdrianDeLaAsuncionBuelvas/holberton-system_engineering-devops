#!/usr/bin/python3
"""Module that calls RESTful API"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    """REST API returns information about his/her TODO list progress"""
    _id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(_id)

    response = requests.get(url)
    name = response.json().get('name')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    total_tasks = 0
    completed = 0

    for task in todos.json():
        if task.get('userId') == int(_id):
            total_tasks += 1
            if task.get('completed'):
                completed += 1
    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          completed,
                                                          total_tasks))
    print('\n'.join(["\t " + task.get('title') for task in todos.json()
                     if task.get('userId') == int(_id) and
                     task.get('completed')]))
