#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json

from scraping.scrapers.statesman import StatesmanScraper
from scraping.ingestors.statesman import StatesmanIngestor
from datetime import datetime
from sentiment.analyzer import Analyzer
from config import config
from common.mongo_connector import MongoConnector

settings = config()
mongo = MongoConnector(settings)
analyzer = Analyzer()
statesman_urls = StatesmanIngestor()
articles = []

for url in statesman_urls:
    articles.append(StatesmanScraper(url))

for article in articles:
    data = json.loads(article)
    data['sentiment'] = analyzer.sentiment(data['article']['content_text'])
    mongo.save("articles", data)

    # Uncomment the next 3 lines to see output to console (if testing)
    print(data['article']['title'])
    print('Sentiment: ', data['sentiment']['rating'])
    print('*********')



# print(StatesmanScraper('https://www.statesman.com/zz/news/20200325/colleges-are-emptying-because-of-coronavirus-liberty-university-is-inviting-students-back'))