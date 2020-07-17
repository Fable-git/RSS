#!/usr/bin/env python
import feedparser
import subprocess
import shlex
from xml.etree import ElementTree
import sys

subscriptions = None
subFileName = None
feed = None

def feedName(url):
    global feed
    parseRss(url)
    return feed.feed.title

def parseRss (url):
    global feed
    feed = feedparser.parse(url)

def downloadLatestFromOpml(opmlFile):
    global subscriptions
    global subFileName
    with open(subFileName,'rt') as f:
        tree = ElementTree.parse(f)
    for node in tree.iter('outline'):
        name = node.attrib.get('text')
        url = node.attrib.get('xmlUrl')
        if name and url:
            print('{} :: {}'.format(name, url))
            downloadMedia(url,0)

def getMediaUrl(url, episode):
    global feed
    parseRss(url)
    return feed.entries[episode].link

def downloadMedia(url, episode):
    url = getMediaUrl(url,episode)
    command = "youtube-dl " + url
    subprocess.call(shlex.split(command))

subFileName = sys.argv[1]
downloadLatestFromOpml("subscriptions.opml")
