#!/usr/bin/env python
import feedparser

feed = None

def feedName(url):
   feed = feedparser.parse(url)
   return feed.feed.title

def parseIfNone(url):
    if feed == None:
        feed = feedparser.parse(url)
        return true
    return false
