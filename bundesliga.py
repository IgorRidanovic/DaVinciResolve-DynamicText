#! /usr/bin/env python
# -*- coding: utf-8 -*-

# This module fetches the most recent Bundesliga headlines and places them in a
# crawl ready string while keeping Unicode characters intact. igor@hdhead.com

import csv
import requests
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

class Bundesliga(object):
    def __init__(self):
        # URL of Bundesliga news RSS feed
        self.url = 'https://www.dfb.de/news/rss/feed/?tx_news_pi1[overwriteDemand][categories]=10071'

    def get_RSS(self):
        # Create HTTP response object from the URL
        return requests.get(self.url).text.encode('utf8')

    def get_headlines(self, rss):
        tree = ET.ElementTree(ET.fromstring(rss))
        root = tree.getroot()

        # Find title items
        rssList = []
        for i in tree.iter(tag='title'):
            # Strip newlines and tabs
            headline = ' '.join(i.text.encode('utf8').split())
            rssList.append(headline)

        # Join into a string and strip off the word 'Feed' from the top
        whitespace = '      '
        headlineString = whitespace.join(rssList)[7:]
        # Remove quotes (we should really replace with \")
        headlineString = ''.join(headlineString.split('"'))
        return headlineString

if __name__ == '__main__':

    football = Bundesliga()

    # RSS XML to string
    rss = football.get_RSS()

    # Parse xml file
    crawl = football.get_headlines(rss)
    print crawl
