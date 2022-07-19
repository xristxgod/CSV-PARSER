
from .models import CheatersDB
from config import Config, SERVER_FILE, CLIENT_FILE


class Core:
    """Core - this base class"""
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Core, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.__cheaters_db = CheatersDB()
        self.__server_storage = ""
