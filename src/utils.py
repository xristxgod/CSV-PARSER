from typing import Union, List, Dict
from datetime import datetime

from .base.schemas import ServerData, ClientData


class Utils:
    @staticmethod
    def get_timestamp(date: Union[str, datetime, int]) -> int:
        if isinstance(date, str):
            return int(datetime.timestamp(datetime.strptime(date, "%d.%m.%Y")))
        elif isinstance(date, datetime):
            return int(datetime.timestamp(date))
        elif isinstance(date, int) and len(str(date)) == 10:
            return date
        else:
            return Utils.get_timestamp(date=datetime.now())

    @staticmethod
    def get_datetime(date: int) -> str:
        return datetime.fromtimestamp(date).strftime("%d.%m.%Y")

    @staticmethod
    def packaging(data: List[Dict], _dataclass: object) -> Union[List[object], List]:
        if len(data) > 0:
            return [_dataclass(**d) for d in data]
        return data
