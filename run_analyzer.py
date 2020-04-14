#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sentiment.analyzer import Analyzer
from config import config
from common.mongo_connector import MongoConnector
from azure.storage.queue import QueueClient
from datetime import datetime
import requests
import json

settings = config()
mongo = MongoConnector(settings)
analyzer = Analyzer()
queue = QueueClient.from_connection_string(
    conn_str=settings['azure_storage']['connection_string'], queue_name=settings['azure_storage']['queue_name_article'])

response = queue.receive_messages()

for message in response:
    print(message.content)
    data = requests.get(message.content)
    json = data.json()
    try:
        sentiment = analyzer.sentiment(json['article']['content_text'])
        newValues = {
            "sentiment": {
                "status": "Complete",
                "analyzed_date": datetime.now(),
                "num_value": sentiment['num_value'],
                "rating": sentiment['rating']
            }
        }
        json['sentiment']['analyzed_date'] = datetime.now()
        mongo.updateOne("articles", json['_id'], newValues)
        queue.delete_message(message)
    except Exception as inst:
        print(type(inst))    # the exception instance
        print(inst.args)     # arguments stored in .args
        print(inst)

    print(json['article']['title'])
    print('Sentiment: ', json['sentiment']['rating'])
    print('*********')
