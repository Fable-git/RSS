# RSS
A python script that downloads mp3/mp4 files from RSS feeds and might support opml if I get it to work in the first place

## Requirements

+ Probably need to be on linux
+ Needs youtube-dl package(can get from most package managers)

## How to use:

Currently this is how you would probably want to use it:
1. make sure you have python and youtube-dl installed
2. Download your list of rss feeds from your feed reader as a .opml file
3. Download and extract this project
4. Put the opml file in the project
5. open up a terminal and in the project folder run: python3 RSS.py youropmlfilename.opml
6. This should download most if not all of your rss mp3 mp4 etc files to the current folder
