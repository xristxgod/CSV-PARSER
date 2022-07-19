from typing import Union, Tuple, Dict
from datetime import datetime

from .models import Database, CSVStorage
from .utils import Utils
from config import Config


class Core:
    """Core - this base class"""
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Core, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.__main_db = Database(Config.DATABASE_URL)
        self.__cheaters_db = Database(Config.CHEATERS_DB_URL)
        self.__server_storage = CSVStorage(Config.SERVER_FILE)
        self.__client_storage = CSVStorage(Config.CLIENT_FILE)

    def get_data_by_time(self, date: Union[str, datetime, int]) -> Tuple[Dict, ...]:
        count_iteration = 0
        server_iteration, client_iteration = self.__server_storage.read(), self.__client_storage.read()
        server_data, client_data = None, None
        server_iter, client_iter = next(server_iteration), next(client_iteration)
        first_server_iteration, first_client_iteration = server_iter, client_iter
        date: int = Utils.get_timestamp(date)
        while True:
            if int(server_iter.get("timestamp")) == date:
                server_data = server_iter
            if int(client_iter.get("timestamp")) == date:
                client_data = client_iter
            if server_data and client_data:
                return server_data, client_data
            if count_iteration > 0 and (first_client_iteration == client_iter or first_server_iteration == server_iter):
                raise Exception
            next(client_iter), next(server_iter)
            count_iteration += 1
