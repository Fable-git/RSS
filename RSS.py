#!/usr/bin/env python
import feedparser

feed = None

def feedName(url):
    global feed
    parseIfNone(url)
    return feed.feed.title

def parseIfNone(url):
    global feed
    if feed == None:
        feed = feedparser.parse(url)
        return True
    return False

def getMediaUrl(url, episode):
    global feed
    parseIfNone(url)
    return feed.entries[episode].link
