from abc import ABC, abstractmethod
from typing import Type

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


class RepoFactory[T: BaseModel](ABC):
    def __init__(self, is_sync: bool, is_core: bool):
        self.is_sync = is_sync
        self.is_core = is_core

    @property
    @abstractmethod
    def sync_repo(self) -> Type[SyncRepo[T]]:
        pass

    @property
    @abstractmethod
    def async_repo(self) -> Type[AsyncRepo[T]]:
        pass

    @abstractmethod
    def get_all(self) -> list[T]:
        pass

    @abstractmethod
    def create(self, data: BaseModel) -> None:
        pass
