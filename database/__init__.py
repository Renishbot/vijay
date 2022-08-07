import motor
import pymongo
import logging
import motor.motor_asyncio as AsyncIOMotorClient
from info import Config, DATABASE_URI 
from info import DATABASE_URI
from sys import exit as exiter
from pymongo import MongoClient
from info import DATABASE_URI as DB_URI
from pyrogram import *
import pymongo
from pymongo.errors import PyMongoError

langdb = db.language

mongo_client = motor.motor_asyncio.AsyncIOMotorClient(Config.DATABASE_URI)

db_x = mongo_client["Vijay"]

myapp = pymongo.MongoClient(DATABASE_URI)
dbx = myapp["AsyncIOMotorCursor"]

class DATABASE_URL:

    def __init__(self, collection) -> None:
        self.collection = main_db[collection]

    def insert_one(self, document):
        result = self.collection.insert_one(document)
        return repr(result.inserted_id)

    def find_one(self, query):
        result = self.collection.find_one(query)
        if result:
            return result
        return False

    def find_all(self, query=None):
        if query is None:
            query = {}
        return list(self.collection.find(query))

    def count(self, query=None):
        if query is None:
            query = {}
        return self.collection.count_documents(query)

    def delete_one(self, query):
        self.collection.delete_many(query)
        return self.collection.count_documents({})

    def replace(self, query, new_data):
        old = self.collection.find_one(query)
        _id = old["_id"]
        self.collection.replace_one({"_id": _id}, new_data)
        new = self.collection.find_one({"_id": _id})
        return old, new

    def update(self, query, update):
        result = self.collection.update_one(query, {"$set": update})
        new_document = self.collection.find_one(query)
        return result.modified_count, new_document

def __connect_first():
    _ = MongoDB("test")

__connect_first()
