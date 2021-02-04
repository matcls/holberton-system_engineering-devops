#!/usr/bin/python3
"""Queries the Reddit API.

Returns the number of subscribers for a given subreddit.
"""
from requests import get


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for the given subreddit."""
    url = 'https://www.reddit.com/r/{}/about.json'
    headers = {'User-Agent': 'matv:1.0.0'}
    request = get(url.format(subreddit), headers=headers)
    if request.status_code != 200:
        return 0
    return request.json().get('data', {}).get('subscribers', 0)
