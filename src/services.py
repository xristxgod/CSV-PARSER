from typing import Union, Tuple, List, Dict
from datetime import datetime

from .models import Database, CSVStorage
from .utils import Utils
from .base.schemas import ServerData, ClientData, GeneralData
from config import Config, logger


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
        start_time, end_time = Utils.get_timestamp(date)
        server_data, client_data = [], []
        server_iteration, client_iteration = self.__server_storage.read(), self.__client_storage.read()
        server_iter, client_iter = next(server_iteration), next(client_iteration)
        cheaters = set([player_id["player_id"] for player_id in self.__cheaters_db.read(
            f"SELECT player_id FROM cheaters WHERE ban_time > '{Utils.get_time_now()}'", True
        )])
        while True:
            if start_time <= int(server_iter.get("timestamp")) <= end_time:
                server_data.append(server_iter)
            if start_time <= int(client_iter.get("timestamp")) <= end_time \
                    and int(client_iter.get("player_id")) not in cheaters:
                client_data.append(client_iter)
            try:
                server_iter, client_iter = next(server_iteration), next(client_iteration)
            except StopIteration:
                data = (
                    Utils.packaging(server_data, _dataclass=ServerData),
                    Utils.packaging(client_data, _dataclass=ClientData)
                )
                if any(data):
                    return data
                return None, None
            except Exception as error:
                logger.error(f"{error}")

    @staticmethod
    def merge_data(server_data: List[ServerData], client_data: List[ClientData]) -> List[GeneralData]:
        general_data: List[GeneralData] = []
        for player in client_data:
            server = list(filter(lambda x: x["error_id"] == player.error_id, server_data))
            if len(server) > 0:
                general_data.append(GeneralData(
                    timestamp=player.timestamp,
                    player_id=player.player_id,
                    event_id=server[0].event_id,
                    error_id=player.error_id,
                    json_client=player.description,
                    json_server=server[0].description
                ))
        return general_data

    def add_to_database(self, general_data: List[GeneralData]) -> bool:
        if len(general_data) == 1:
            self.__main_db.create((
                "INSERT INTO general (timestamp, player_id, event_id, error_id, json_server, json_client) "
                "VALUES (%d, %d, %d, %s, %s, %s)"
            ))
