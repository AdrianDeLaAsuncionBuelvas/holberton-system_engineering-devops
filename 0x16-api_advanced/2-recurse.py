#!/usr/bin/python3
"""Reddit API Module"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Return a list containg the titles of all hot article"""
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    USERAGENT = {'User-Agent':
                 'Unix:com.holberton.apiadvanced:task0 (by /u/_marc_marc_)'}
    params = {'limit': 100}
    if count > 0:
        params['after'] = after
    req = requests.get(URL, headers=USERAGENT, params=params)
    if req.status_code is not 200:
        return (None)
    jreq = req.json()
    data_path = jreq['data']['children']
    for i in range(len(data_path)):
        hot_list.append(data_path[i]['data']['title'])
    count = count + 1
    after = jreq['data']['after']
    if after is None:
        return (hot_list)
    else:
        return recurse(subreddit, hot_list, count, after)
