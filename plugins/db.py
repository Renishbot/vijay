import pymongo
import os
from info import DATABASE_URI as MONGO_URL

database = pymongo.MongoClient(MONGO_URL)['notes']['notes']
