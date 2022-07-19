import csv
from typing import Generator, Optional


class BaseDB:
    pass


class BaseStorage:

    def connect(self) -> csv.DictReader:
        raise NotImplementedError

    def read(self) -> Generator:
        raise NotImplementedError
