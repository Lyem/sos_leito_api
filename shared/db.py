import pymongo
import os

class Db:

    def __init__(self):
        client = pymongo.MongoClient(os.environ['token'])
        self.db = client.sos_leito

    def insert(self, collection, json):
	    self.db[collection].insert_one(json)

    def find(self, collection, json):
        return self.db[collection].find_one(json)
    
    def findAll(self, collection, json):
        return self.db[collection].find(json,{"_id": 0})

    def delete(self,collection, json):
        self.db[collection].delete_one(json)