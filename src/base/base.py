from typing import Generator


class BaseDB:
    pass


class BaseStorage:

    def read(self) -> Generator:
        raise NotImplementedError
