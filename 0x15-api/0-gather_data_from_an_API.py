#!/usr/bin/python3
"""
Accessing a url with employee ID to return information
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    Function to get employees todo list
    progress
    """
    ID = argv[1]
    BASE_URL = 'https://jsonplaceholder.typicode.com/'
    TODOS_URL = BASE_URL + 'todos/'
    USER_URL = BASE_URL + 'users/'
    USER_PARAMS = {'id': ID}
    TODOS_PARAMS = {'userId': ID}
    res_todos = requests.get(url=TODOS_URL, params=TODOS_PARAMS)
    res_user = requests.get(url=USER_URL, params=USER_PARAMS)
    user = res_user.json()
    todos = res_todos.json()
    name = user[0].get('name')
    completed_todos = [todo.get('title')
                       for todo in todos if todo.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):"
          .format(name,
                  len(completed_todos), len(todos)), end='\n\t ')
    print(*completed_todos, sep='\n\t ')
