from info import DATABASE_URI as DB_URI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

BASE = declarative_base()
SESSION = start()
