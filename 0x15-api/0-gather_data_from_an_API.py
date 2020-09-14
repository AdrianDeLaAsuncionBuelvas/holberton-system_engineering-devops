#!/usr/bin/python3
"""Module that calls RESTful API"""

import requests
from sys import argv


if __name__ == '__main__':
    """REST API returns information about his/her TODO list progress"""
    ID = argv[1]
    BASE_URL = 'https://jsonplaceholder.typicode.com/'
    TODOS_URL = BASE_URL + 'todos/'
    USER_URL = BASE_URL + 'users/'
    USER_PARAMS = {'id': ID}
    TODOS_PARAMS = {'userId': ID}
    todos = requests.get(url=TODOS_URL, params=TODOS_PARAMS).json()
    user = requests.get(url=USER_URL, params=USER_PARAMS).json()
    name = user[0].get('name')
    completed_todos = [todo.get('title')
                       for todo in todos if todo.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):"
          .format(name,
                  len(completed_todos), len(todos)), end='\n\t ')
    print(*completed_todos, sep='\n\t ')
