from dataclasses import dataclass


@dataclass()
class ServerData:
    timestamp: int
    event_id: int
    error_id: int
    description: str


@dataclass()
class ClientData:
    timestamp: int
    player_id: int
    error_id: int
    description: str


@dataclass()
class GeneralData:
    timestamp: int
    player_id: int
    event_id: int
    error_id: int
    description: str
