from typing import Optional


class BaseDB:
    def connect(self) -> Optional:
        raise NotImplementedError
