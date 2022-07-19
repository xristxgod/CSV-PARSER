import sqlite3
from typing import Optional

from .base import BaseDB
from config import Config


# <<<===========================================>>> SQLite databases <<<=============================================>>>


class MainDB(BaseDB):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MainDB, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.connection: Optional[sqlite3.Connection] = None
        self.cursor: Optional[sqlite3.Cursor] = None

    def connect(self) -> Optional:
        if self.connection is None:
            self.connection = sqlite3.connect(Config.DATABASE_URL)
            self.cursor = self.connection.cursor()


class CheatersDB:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CheatersDB, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.connection: Optional[sqlite3.Connection] = None
        self.cursor: Optional[sqlite3.Cursor] = None

    def connect(self) -> Optional:
        if self.connection is None:
            self.connection = sqlite3.connect(Config.CHEATERS_DB_URL)
            self.cursor = self.connection.cursor()


# <<<===========================================>>> CSV Storages <<<=================================================>>>


class ServerStorage:
    pass


class ClientStorage:
    pass
