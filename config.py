import os
import logging


# Dirs
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))       # Root dir
FILES_DIR = os.path.join(ROOT_DIR, "files")                 # Files dir
# Files
CLIENT_FILE = os.path.join(FILES_DIR, "client.csv")         # Client csv file
SERVER_FILE = os.path.join(FILES_DIR, "server.csv")         # Server csv file
CHEATERS_DB = os.path.join(FILES_DIR, "cheaters.db")        # Cheaters db file
MAIN_DB = os.path.join(FILES_DIR, "main.db")                # Main db file


logger = logging.getLogger(__name__)
logging.basicConfig(
    format=u"[%(asctime)s][%(filename)s][LINE:%(lineno)d][%(levelname)s] | %(message)s",
    level=logging.INFO
)


class Config:
    MAIN_DB_PATH = os.getenv("MAIN_DB_PATH", MAIN_DB)
    CHEATERS_DB_PATH = os.getenv("CHEATERS_DB_PATH", CHEATERS_DB)
    CLIENT_FILE = os.getenv("CLIENT_FILE", CLIENT_FILE)
    SERVER_FILE = os.getenv("SERVER_FILE", SERVER_FILE)
