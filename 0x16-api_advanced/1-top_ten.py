#!/usr/bin/python3
"""Reddit API Module"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    USERAGENT = {'User-Agent':
                 'Unix:com.holberton.apiadvanced:task1 (by /u/_marc_marc_)'}
    req = requests.get(URL, headers=USERAGENT)
    if req.status_code is not 200:
        print(None)
        return (0)
    jreq = req.json()
    data_path = jreq['data']['children']
    for i in range(10):
        print(data_path[i]['data']['title'])
