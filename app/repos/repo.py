from abc import ABC, abstractmethod

from pydantic import BaseModel


class SyncRepo[T: BaseModel](ABC):
    @staticmethod
    @abstractmethod
    def get_all() -> list[T]:
        pass

    @staticmethod
    @abstractmethod
    def create(data: BaseModel) -> None:
        pass


class AsyncRepo[T: BaseModel](ABC):
    @staticmethod
    @abstractmethod
    async def get_all() -> list[T]:
        pass

    @staticmethod
    @abstractmethod
    async def create(data: BaseModel) -> None:
        pass
