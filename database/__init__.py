import motor
import pymongo
import logging
import motor.motor_asyncio as AsyncIOMotorClient
from info import Config, DATABASE_URI 
from info import DATABASE_URI

mongo_client = motor.motor_asyncio.AsyncIOMotorClient(Config.DATABASE_URI)

db_x = mongo_client["Vijay"]
