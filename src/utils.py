from typing import Union, List, Tuple, Dict
from datetime import datetime


class Utils:
    @staticmethod
    def get_timestamp(date: Union[str, datetime, int]) -> Tuple[int, int]:
        if isinstance(date, str):
            date: datetime = datetime.strptime(date, "%d.%m.%Y")
        elif isinstance(date, datetime):
            date: datetime = date
        elif isinstance(date, int) and len(str(date)) == 10:
            date: datetime = datetime.fromtimestamp(date)
        else:
            return Utils.get_timestamp(date=datetime.now())
        return (
            int(datetime.timestamp(date.replace(hour=0, minute=0, second=0, microsecond=0))),
            int(datetime.timestamp(date.replace(hour=23, minute=59, second=59, microsecond=0)))
        )

    @staticmethod
    def get_datetime(date: int) -> str:
        return datetime.fromtimestamp(date).strftime("%d.%m.%Y")

    @staticmethod
    def get_time_now() -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def packaging(data: List[Dict], _dataclass: object) -> Union[List[object], List]:
        if len(data) > 0:
            return [_dataclass(**d) for d in data]
        return data

    @staticmethod
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
