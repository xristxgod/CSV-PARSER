"""Test core services helper. In the file `src.services.py` `Core` class """
import unittest
from unittest.mock import Mock, patch
from typing import Generator, List, Tuple, Dict

from src.services import core


TEST_SERVER_DATA = [
    {"timestamp": 1658291854, "event_id": 14, "error_id": "ERROR-NUMBER-ONE", "description": '{"testdata": "test"}'},
    {"timestamp": 1652768806, "event_id": 1, "error_id": "ERROR-NUMBER-TWO", "description": '{"testdata": "test2"}'},
    {"timestamp": 1652250406, "event_id": 11, "error_id": "ERROR-NUMBER-THREE", "description": '{"testdata": "test3"}'},
    {"timestamp": 1658291854, "event_id": 15, "error_id": "ERROR-NUMBER-SIX", "description": '{"testdata": "test6"}'}
]
TEST_CLIENT_DATA = [
    {"timestamp": 1658291854, "player_id": 5, "error_id": "ERROR-NUMBER-ONE", "description": '{"testplay": "play1"}'},
    {"timestamp": 1658291854, "player_id": 12, "error_id": "ERROR-NUMBER-FOUR", "description": '{"testplay": "play6"}'},
    {"timestamp": 1658291854, "player_id": 6, "error_id": "ERROR-NUMBER-FIVE", "description": '{"testplay": "play9"}'},
    {"timestamp": 1658291854, "player_id": 7, "error_id": "ERROR-NUMBER-SIX", "description": '{"testplay": "play3"}'},
]
TEST_CHEATERS_DATA = [
    {"player_id": 7}
]


class Test:
    @staticmethod
    def test_server_read() -> Generator:
        # Test server generator
        for data in TEST_SERVER_DATA:
            yield data

    @staticmethod
    def test_client_read() -> Generator:
        # Test client generator
        for data in TEST_CLIENT_DATA:
            yield data


class TestCore(unittest.TestCase):
    @patch("src.services.core._Core__server_storage.read")
    @patch("src.services.core._Core__client_storage.read")
    @patch("src.services.core._Core__cheaters_db.read")
    def test_get_data_by_time(self, server_read: Mock, client_read: Mock, cheaters_db: Mock):
        server_iter, client_iter = Test.test_server_read(), Test.test_client_read()
        server_read.return_value = server_iter
        client_read.return_value = client_iter
        cheaters_db.return_value = TEST_CHEATERS_DATA
        result: Tuple = core.get_data_by_time(date=1658291854)

    def test_merge_data(self, test_core: Mock):
        pass

    def test_add_to_database(self):
        pass
