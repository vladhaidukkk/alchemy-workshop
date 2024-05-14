from abc import ABC, abstractmethod
from typing import Sequence

from app.db.core import Base


class SyncOrmRepo[T: Base](ABC):
    @staticmethod
    @abstractmethod
    def get_all() -> Sequence[T]:
        pass


class AsyncOrmRepo[T: Base](ABC):
    @staticmethod
    @abstractmethod
    async def get_all() -> Sequence[T]:
        pass
