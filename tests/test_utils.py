"""Test utils. In the file `src.utils.py` `Utils` class """
import unittest
from dataclasses import dataclass
from datetime import datetime

from src.utils import Utils


@dataclass()
class TestDataClass:
    testId: int
    testInfo: str


class TestUtils(unittest.TestCase):
    def test_get_timestamp(self):
        assert Utils.get_timestamp("12.12.1999") == (944946000, 945032399)
        assert Utils.get_timestamp(datetime.strptime("12.12.1999", "%d.%m.%Y")) == (944946000, 945032399)
        assert Utils.get_timestamp(1658290937) == (1658264400, 1658350799)

    def test_get_datetime(self):
        assert Utils.get_datetime(1658291067) == "20.07.2022"

    def test_get_time_now(self):
        d, h = Utils.get_time_now().split(" ")
        assert len(d.split("-")) == 3
        assert len(h.split(":")) == 3

    def test_packaging(self):
        data = [
            {"testId": 12, "testInfo": "test info num 1"}, {"testId": 15, "testInfo": "test info num 2"},
            {"testId": 55, "testInfo": "test info num 3"}, {"testId": 65, "testInfo": "test info num 4"}
        ]
        data = Utils.packaging(data, TestDataClass)
        assert isinstance(data, list)
        assert isinstance(data[0], TestDataClass)
        assert data[0].testId == 12 and data[0].testInfo == "test info num 1"
