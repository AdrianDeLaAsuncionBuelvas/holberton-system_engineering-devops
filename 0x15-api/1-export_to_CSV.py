#!/usr/bin/python3
"""Module Export to CSV"""

import csv
import requests
from sys import argv


if __name__ == '__main__':
    _id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(_id)

    response = requests.get(url)
    jreq = response.json()
    name = jreq['name']
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    jreq = response.json()
    tasks = []
    completed_tasks = []
    for task in jreq:
        if task['userId'] == int(_id):
            tasks.append(task)
    total_tasks = len(tasks)
    for task in tasks:
            completed_tasks.append({'name': name, 'id': _id,
                                    'completed': task['completed'],
                                    'title': task['title']})
    with open('{}.csv'.format(_id), mode='w') as csv_file:
        fieldnames = ['id', 'name', 'completed', 'title']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for task in completed_tasks:
            writer.writerow(task)
