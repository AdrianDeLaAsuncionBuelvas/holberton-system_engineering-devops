#!/usr/bin/python3
"""Module that calls RESTful API"""

import requests
import json
from sys import argv


if __name__ == '__main__':
    """REST API returns information about his/her TODO list progress"""
    _id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(_id)

    response = requests.get(url)
    jreq = response.json()
    name = jreq['name']
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    jreq = response.json()
    tasks = []
    complete_tasks = []
    for i in jreq:
        if i['userId'] == int(_id):
            tasks.append(i)
    total_tasks = len(tasks)
    for i in tasks:
        if i['completed'] is True:
            complete_tasks.append(i)
    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          len(complete_tasks),
                                                          total_tasks))
    for i in complete_tasks:
        print("\t {}".format(i['title']))
