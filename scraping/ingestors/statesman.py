#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from defusedxml.ElementTree import parse

def loadRSS():
    rss_url = 'https://www.statesman.com/news?template=rss&mime=xml'
    resp = requests.get(rss_url)
    with open('statesman.xml', 'wb') as f: 
        f.write(resp.content) 

def parseXML(xml):
    tree = parse(xml)
    root = tree.getroot()

    urls = []

    for item in root.findall('./channel/item/guid'):
        urls.append(item.text)

    return urls

def StatesmanIngestor():
    loadRSS()
    return parseXML('statesman.xml')

if __name__ == "__main__":
    StatesmanIngestor()