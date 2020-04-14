from pymongo import MongoClient
import datetime
from bson.objectid import ObjectId
from urllib import parse

class MongoConnector:
    def __init__(self, settings={}):
        if not settings["mongo"]:
            print("MongoDB connection settings not supplied")
            exit(0)
        try:
            connectionString = "mongodb://{0}:{1}@{2}/?authSource={3}&authMechanism=SCRAM-SHA-256"
            connectionString = connectionString.format(settings["mongo"]["user"], parse.quote_plus(settings["mongo"]["password"]), settings["mongo"]["host"], settings["mongo"]["authSource"])
            self.client = MongoClient(connectionString)
            self.db = settings["mongo"]["db"]
            self.client.server_info()
        except Exception as e:
            print("Could not conenct to MongoDB - ", e)
            exit(0)

    def save(self, collection, items):
        result = self.client[self.db][collection].insert(items)
        return result

    def updateOne(self, collection, id, set_item):
        result = self.client[self.db][collection].update_one(
            {'_id': ObjectId(id)}, {'$set': set_item}, upsert=False)
        return result