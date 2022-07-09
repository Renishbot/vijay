import logging
import motor.motor_asyncio

from info import Config

mongo_client = motor.motor_asyncio.AsyncIOMotorClient(Config.DATABASE_URI)

db_x = mongo_client["Friday"]
