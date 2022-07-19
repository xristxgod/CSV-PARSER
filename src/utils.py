from typing import Union
from datetime import datetime


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
