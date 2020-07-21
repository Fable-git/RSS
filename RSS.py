#!/usr/bin/env python
import feedparser
import subprocess
import shlex
from xml.etree import ElementTree
import sys
from collections import defaultdict

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
        opml = ElementTree.parse(f)
    for node in opml.iter('outline'):
        name = node.attrib.get('text')
        url = node.attrib.get('xmlUrl')
        if name and url:
            print('{} :: {}'.format(name, url))
            downloadMedia(url,0)

def downloadNEpisodesFromOpml(opmlFile, depth):
    global subscriptions
    global subFileName
    def N():
        return 0
    episodesDownloaded = defaultdict(N)
    with open(subFileName,'rt') as f:
        opml = ElementTree.parse(f)
    while (sum(episodesDownloaded.values()) <= depth):
        for node in opml.iter('outline'):
            if (sum(episodesDownloaded.values()) <= depth):
                print(depth)
                name = node.attrib.get('text')
                url = node.attrib.get('xmlUrl')
                if name and url:
                    print('{} :: {}'.format(name, url))
                    downloadMedia(url,episodesDownloaded[url])
                    episodesDownloaded[url] += 1
                    print(episodesDownloaded[url])
                    print(sum(episodesDownloaded.values()))

def downloadAllEpisodesFromOpml(opmlFile):
    global subscriptions
    global subFileName
    with open(subFileName,'rt') as f:
        opml = ElementTree.parse(f)
    for node in opml.iter('outline'):
        name = node.attrib.get('text')
        url = node.attrib.get('xmlUrl')
        if name and url:
            print('{} :: {}'.format(name, url))
            downloadAllMedia(url)

def downloadAllMedia(rss):
    global feed
    parseRss(rss)
    for num in range(0, len(feed.entries)):
        downloadMedia(rss,num)

def getMediaUrl(rss, episode):
    global feed
    parseRss(rss)
    return feed.entries[episode].link

def downloadMedia(url, episode):
    url = getMediaUrl(url,episode)
    command = "youtube-dl -q " + url
    subprocess.call(shlex.split(command))

def main():
    hasOpml = "null"
    while(type(hasOpml) is not bool):
        hasOpml = input("Do you have an OMPL/XML file for your feeds? y/n: ")
        if("y" in hasOpml):
            hasOpml = True
        elif("n" in hasOpml):
            hasOpml = False
        else:
            print("Answer must have either y or n")
    if hasOpml:
        global subFileName
        subFileName = input("<Location>/<Name> of OPML/XML file: ")
    else:
        url = input("Paste the url to your RSS feed: ")
    depth = "null"
    while(depth.isdigit() != True):
        depth = input("How many episodes would you like to download?: ")
    depth = int(depth)
    print(depth)
    if (hasOpml):
        if (depth == 0):
            downloadAll = "null"
            while(type(downloadAll) is not bool):
                downloadAll = input("Are you sure you want to download ALL EPISODES? y/n: ")
                if("y" in downloadAll):
                    downloadAll = True
                elif("n" in downloadAll):
                    downloadAll = False
                else:
                    print("Answer must have either y or n")
                if (downloadAll):
                    downloadAllEpisodesFromOpml(subFileName)
        else:
            downloadNEpisodesFromOpml(subFileName, depth)
    else:
        if (depth == 0):
            downloadAll = "null"
            while(type(downloadAll) is not bool):
                downloadAll = input("Are you sure you want to download ALL EPISODES? y/n: ")
                if("y" in downloadAll):
                    downloadAll = True
                elif("n" in downloadAll):
                    downloadAll = False
                else:
                    print("Answer must have either y or n")
                if (downloadAll):
                    downloadAllMedia(url)
        else:
            depth -= 1
            while depth >= 0:
                print(depth)
                downloadMedia(url,depth)
                depth -= 1

if __name__ == "__main__":
    main()
