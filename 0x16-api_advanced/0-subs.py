#!/usr/bin/python3
"""Python script that queries the Reddit API and returns the number of subscribers."""
import requests

def number_of_subscribers(subreddit):
	""" this function allows you to get the number of subscribers in reddit"""
	url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
	headers = {'User-Agent': 'mmasmar'}
	res = requests.get(url, headers=headers)
	subscribers = res.json().get('data', {}).get('subscribers', 0)
	return subscribers
