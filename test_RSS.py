#!/usr/bin/env python

import RSS as rss

url = "https://feeds.fireside.fm/linuxunplugged/rss"

def test_nothing():
    assert 0 == 0

def test_feedName():
    assert rss.feedName(url) == "LINUX Unplugged"

def test_ParsesIfHasntParsed():
    rss.feed = None
    assert rss.feed == None
    assert rss.parseIfNone(url) == True
    assert rss.feed != None

def test_DoesntParseIfAlreadyParsed():
    rss.parseIfNone(url)
    before = rss.feed
    assert rss.feed != None
    assert rss.parseIfNone(url) == False
    assert rss.feed == before

def test_getMediaUrl():
    assert rss.getMediaUrl(url,0) == "https://linuxunplugged.com/362"
