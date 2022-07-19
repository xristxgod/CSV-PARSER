from typing import Union, Tuple, List, Dict
from datetime import datetime

from .models import Database, CSVStorage
from .utils import Utils
from .base.schemas import ServerData, ClientData
from config import Config


class Core:
    """Core - this base class"""
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Core, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.__main_db = Database(Config.MAIN_DB_PATH)
        self.__cheaters_db = Database(Config.CHEATERS_DB_PATH)
        self.__server_storage = CSVStorage(Config.SERVER_FILE)
        self.__client_storage = CSVStorage(Config.CLIENT_FILE)

    def get_data_by_time(self, date: Union[str, datetime, int]) -> Tuple:
        date: int = Utils.get_timestamp(date)
        server_data, client_data = [], []
        server_iteration, client_iteration = self.__server_storage.read(), self.__client_storage.read()
        server_iter, client_iter = next(server_iteration), next(client_iteration)
        while True:
            if int(server_iter.get("timestamp")) == date:
                server_data.append(server_iter)
            if int(client_iter.get("timestamp")) == date:
                client_data.append(client_data)
            try:
                server_iter, client_iter = next(client_iteration), next(server_iteration)
            except StopIteration:
                data = (
                    Utils.packaging(server_data, _dataclass=ServerData),
                    Utils.packaging(client_data, _dataclass=ClientData)
                )
                if any(data):
                    return data
                raise Exception(f"Nothing has been found for this date: {Utils.get_datetime(date)}")
