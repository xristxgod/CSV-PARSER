from typing import Generator, Optional, List, Dict, Any


class BaseDB:

    def read(self, sql: str, is_all: bool = False) -> Any:
        raise NotImplementedError

    def create(self, sql: str, is_transaction: bool = False) -> bool:
        raise NotImplementedError


class BaseStorage:

    def read(self) -> Generator:
        raise NotImplementedError

    def get(self) -> List[Dict]:
        raise NotImplementedError
