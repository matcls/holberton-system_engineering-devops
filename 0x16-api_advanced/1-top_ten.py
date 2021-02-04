#!/usr/bin/python3
"""Queries the Reddit API.

Prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
from requests import get


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts
     listed for a given subreddit."""
    url = 'https://www.reddit.com/r/{}/.json?sort=hot&limit=10'
    headers = {'User-Agent': 'matv:1.0.0'}
    request = get(url.format(subreddit),
                  headers=headers,
                  allow_redirects=False)
    if request.status_code != 200:
        print("None")
        return
    data = request.json().get('data', {}).get('children', {})
    for post in data:
        print(post.get('data', {}).get('title'))
