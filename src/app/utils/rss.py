import feedparser
from pandas.io.json import json_normalize


def get_rss_items(url):
    return feedparser.parse(url)
    flattened = json_normalize(feed.entries)
    return flattened
