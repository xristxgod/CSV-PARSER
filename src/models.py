import csv
import sqlite3
from typing import Generator, Optional

from .base import BaseDB, BaseStorage


# <<<===========================================>>> SQLite databases <<<=============================================>>>


class Database(BaseDB):
    def __init__(self, path: str):
        self.connection: sqlite3.Connection = sqlite3.connect(path)
        self.cursor: sqlite3.Cursor = self.connection.cursor()


# <<<===========================================>>> CSV Storages <<<=================================================>>>


class CSVStorage(BaseStorage):
    def __init__(self, path: str):
        self.path: str = path

    def connect(self) -> csv.DictReader:
        with open(self.path, newline='') as file:
            return csv.DictReader(file)

    def read(self) -> Generator:
        for row in self.connect():
            yield row
