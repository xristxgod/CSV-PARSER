from typing import List, Dict
from dataclasses import dataclass


@dataclass()
class ServerData:
    timestamp: int
    event_id: int
    error_id: str
    description: str

    @property
    def to_dict(self) -> Dict:
        return self.__dict__


@dataclass()
class ClientData:
    timestamp: int
    player_id: int
    error_id: str
    description: str

    @property
    def to_dict(self) -> Dict:
        return self.__dict__


@dataclass()
class GeneralData:
    timestamp: int
    player_id: int
    event_id: int
    error_id: str
    json_server: str
    json_client: str

    @property
    def to_list(self) -> List:
        return [
            self.timestamp, self.player_id, self.event_id, self.error_id, self.json_server, self.json_server
        ]
