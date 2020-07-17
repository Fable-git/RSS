#!/usr/bin/env python

import RSS as rss

url = "https://feeds.fireside.fm/linuxunplugged/rss"

def test_nothing():
    assert 0 == 0

def test_feedName():
    assert rss.feedName(url) == "LINUX Unplugged"

def test_ParseRss():
    rss.feed = None
    assert rss.feed == None
    assert rss.parseRss(url) == True
    assert rss.feed != None

def test_DoesntRepeatParse():
    rss.parseRss(url)
    before = rss.feed
    assert rss.feed != None
    assert rss.parseRss(url) == False
    assert rss.feed == before

def test_getMediaUrl():
    assert rss.getMediaUrl(url,0) == "https://linuxunplugged.com/362"

def test_opmlParsing():
    rss.subscriptions = None
    assert rss.subscriptions == None
    rss.parseOpml("subscriptions.opml")
