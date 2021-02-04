#!/usr/bin/python3
"""Queries the Reddit API.

Recursively obtains the list of all hot post titles for a given subreddit.
"""
from requests import get
after = ""


def recurse(subreddit, hot_list=[]):
    """Returns a list containing the titles of all hot articles
     for the given subreddit"""
    global after
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'
    headers = {'User-Agent': 'matv:1.0.0'}
    request = get(url.format(subreddit, after),
                  headers=headers,
                  allow_redirects=False)
    if request.status_code != 200:
        return None
    if after is None:
        return hot_list
    data = request.json().get('data').get('children')
    for post in data:
        hot_list.append(post.get('data').get('title'))

    after = request.json().get('data').get('after')
    recurse(subreddit, hot_list)
    return(hot_list)
