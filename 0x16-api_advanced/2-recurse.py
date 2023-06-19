#!/usr/bin/python3
""" Recursive function that queries the Reddit API and return list of all\
hot articles for a subreddit"""
import requests


def recurse(subreddit, after='', count=0, hot_list=[]):
    """ Returns list of all hot articles for a given subreddit."""
    url = 'https://reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': 'mmasmar'}
    params = {
        'after': after,
        'count': count,
        'limit': 100
    }
    res = requests.get(
        url,
        headers=headers,
        params=params
    )

    if res.status_code == 404:
        return None

    data = res.json().get('data')
    after = data.get('after')
    count += data.get('dist')

    for child in data.get('children'):
        hot_list.append(child.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, after, count, hot_list)

    return hot_list
