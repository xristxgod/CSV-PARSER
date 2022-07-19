import csv
import sqlite3
from typing import Generator, Union, List, Dict

from .base import BaseDB, BaseStorage
from .utils import Utils
from config import logger


# <<<===========================================>>> SQLite databases <<<=============================================>>>


class Database(BaseDB):
    def __init__(self, path: str):
        self.connection: sqlite3.Connection = sqlite3.connect(path)
        self.connection.row_factory = Utils.dict_factory
        self.cursor: sqlite3.Cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def read(self, sql: str, is_all: bool = False) -> Union[List[Dict], Dict]:
        try:
            data = self.cursor.execute(sql)
            if is_all:
                # List[Dict]
                return data.fetchall()
            # Dict
            return data.fetchone()
        except Exception as error:
            logger.error(f"{error}")
            raise error

    def create(self, sql: str, is_transaction: bool = False) -> bool:
        try:
            if not is_transaction:
                self.cursor.execute(sql)
            else:
                self.cursor.executescript(sql)
            self.connection.commit()
            return True
        except Exception as error:
            self.connection.rollback()
            logger.error(f"{error}")
            return False


# <<<===========================================>>> CSV Storages <<<=================================================>>>


class CSVStorage(BaseStorage):
    def __init__(self, path: str):
        self.path: str = path

    def read(self) -> Generator:
        with open(self.path, newline='') as file:
            for row in csv.DictReader(file):
                yield row

    def get(self) -> List[Dict]:
        with open(self.path, newline='') as file:
            return [row for row in csv.DictReader(file)]
