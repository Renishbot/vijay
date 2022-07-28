import motor
import logging
import motor.motor_asyncio as AsyncIOMotorClient
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from info import Config, DATABASE_URI as DB_URI

mongo_client = motor.motor_asyncio.AsyncIOMotorClient(Config.DB_URI)

db_x = mongo_client["Vijay"]

def start() -> scoped_session:
    engine = create_engine(DB_URI, client_encoding="utf8")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

BASE = declarative_base()
SESSION = start()
