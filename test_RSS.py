#!/usr/bin/env python

import RSS as rss

url = "https://feeds.fireside.fm/linuxunplugged/rss"

def test_nothing():
    assert 0 == 0

def test_feedName():
    assert rss.feedName(url) == "LINUX Unplugged"

def test_parseIfNone():
    assert rss.feed == None
    assert rss.parseIfNone() == true
    assert rss.feed != None
