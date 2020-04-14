#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import datetime
import re

# TODO - Add error handling for empty url

def StatesmanScraper(url):
    if url is None:
        print('No url provided')
        exit(0)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    char_subs = ["\n", "\r", "\t"]

    title_elem = soup.find('h1', class_='headline')
    date_elem = soup.find('span', class_='article-meta-date')
    byline_elem = soup.find('span', class_='byline-item')
    img_elem = soup.find('img', class_='image')["src"]
    article_summary_elem = soup.find('p', class_='article-summary').next_sibling.next_sibling

    # Data Cleansing
    byline_elem_text = re.sub("|".join(char_subs), "", byline_elem.text)
    content_text = re.sub("|".join(char_subs), "", article_summary_elem.text)

    response = {
        "article": {
            "title": title_elem.text,
            "date": date_elem.text,
            "author": byline_elem_text,
            "img_link": img_elem if img_elem else "",
            "content_html": article_summary_elem.prettify(formatter="html"),
            "content_text": content_text,
            "link": url
        },
        "source": {
            "name": "Austin Statesman",
            "link": "https://statesman.com",
            "img_link": "https://www.statesman.com/Global/images/head/nameplate/statesman_logo.png"
        },
        "metadata": {
            "analyzed_date": datetime.datetime.now()
        }
    }

    return json.dumps(response, default=str)

# url = 'https://statesman.com/news/20200325/austin-lake-travis-school-districts-extend-campus-closures-to-april-13'
# url = 'https://www.statesman.com/zz/news/20200325/colleges-are-emptying-because-of-coronavirus-liberty-university-is-inviting-students-back'
