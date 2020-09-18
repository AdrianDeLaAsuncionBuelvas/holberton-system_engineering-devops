#!/usr/bin/python3
"""Reddit API Module"""
import requests


def count_words(subreddit, word_list, count=0, after=None):
    """Parses the title of all hot article"""
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    USERAGENT = {'User-Agent':
                 'Unix:com.holberton.apiadvanced:task3 (by /u/_marc_marc_)'}
    params = {'limit': 100}
