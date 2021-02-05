#!/usr/bin/python3
"""Queries the Reddit API.

Recursively obtains the count of words in all hot post titles.
"""
from requests import get
after = ""
word_count = {}


def count_words(subreddit, word_list):
    """Print the count of words fro, all hot post titles."""
    global after
    global word_count
    params = {
        "after": after,
        "limit": 100
    }
    url = 'https://www.reddit.com/r/{}/hot.json'
    headers = {'User-Agent': 'matv:1.0.0'}
    request = get(url.format(subreddit,
                  params=params),
                  headers=headers,
                  allow_redirects=False)
    if request.status_code != 200:
        return None

    data = request.json()

    hot_titles_list = [child.get("data").get("title")
                       for child in data
                       .get("data")
                       .get("children")]
    if not hot_titles_list:
        return None

    word_list = list(dict.fromkeys(word_list))
    if word_count == {}:
        word_count = {word: 0 for word in word_list}

    for title in hot_titles_list:
        split_words = title.split(" ")
        for word in word_list:
            for s_word in split_words:
                if s_word.lower() == word.lower():
                    word_count[word] += 1

    after = data.get("data").get("after")
    if not data:
        sorted_counts = sorted(word_count.items(), key=lambda kv: kv[0])
        sorted_counts = sorted(word_count.items(),
                               key=lambda kv: kv[1], reverse=True)
        [print("{} : {}".format(k, v)) for k, v in sorted_counts if v != 0]
    else:
        return count_words(subreddit, word_list)
