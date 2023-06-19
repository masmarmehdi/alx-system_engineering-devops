#!/usr/bin/python3
""" Python script that prints the title of first 10 posts listed in first page """
import requests

def top_ten(subreddit):
    """
    Main function
    """
    url = 'https://reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'mmasmar'}
    res = requests.get(url, headers=headers)

    try:
        children = res.json().get('data').get('children')
        for child in children:
            print(child.get('data').get('title'))
    except Exception:
        print(None)
