import sqlite3

import databases
import sqlalchemy
from sqlalchemy import Column, orm
from sqlalchemy.types import Integer, BigInteger, JSON

from config import Config


database = databases.Database(Config.DATABASE_URL)
BaseModel = orm.declarative_base()
engine = sqlalchemy.create_engine(Config.DATABASE_URL, connect_args={"check_same_thread": False})
session = orm.Session(engine)


class StorageModel(BaseModel):
    __tablename__ = "user_model"
    id = Column(BigInteger, primary_key=True, unique=True)
    timestamp = Column(BigInteger)
    player_id = Column(Integer)
    event_id = Column(Integer)
    error_id = Column(Integer)
    json_server = Column(JSON)
    json_client = Column(JSON)


class CheatersDB:
    def __init__(self):
        self.connection = sqlite3.connect(Config.CHEATERS_DB_URL)
        self.cursor = self.connection.cursor()
