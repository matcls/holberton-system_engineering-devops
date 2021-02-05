#!/usr/bin/python3
"""Queries the Reddit API.

Recursively obtains the count of words in all hot post titles.
"""
from requests import get
after = ""


def count_words(subreddit, word_list):
    """Print the count of words fro, all hot post titles."""
    hot_list = recurse(subreddit)
    word_dict = {}

    if not hot_list:
        return None
    else:
        word_dict = {word: 0 for word in word_list}

    for title in hot_list:
        title_split = title.split(" ")
        for word in title_split:
            for s_word in word_list:
                if word.lower() == s_word.lower():
                    word_dict[s_word] += 1

    for k, v in sorted(word_dict.items(), key=lambda kv: kv[1], reverse=True):
        if v != 0:
            print("{}: {}".format(k, v))


def recurse(subreddit, hot_list=[]):
    """Return a list with the titles of all hot articles for subreddit."""
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
