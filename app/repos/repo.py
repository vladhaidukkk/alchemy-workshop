from abc import ABC, abstractmethod

from pydantic import BaseModel


class SyncRepo[T: BaseModel](ABC):
    @staticmethod
    @abstractmethod
    def get_all() -> list[T]:
        pass

    @staticmethod
    @abstractmethod
    def create(data: any) -> None:
        pass


class AsyncRepo[T: BaseModel](ABC):
    @staticmethod
    @abstractmethod
    async def get_all() -> list[T]:
        pass

    @staticmethod
    @abstractmethod
    async def create(data: any) -> None:
        pass


class RepoFactory[T: BaseModel](ABC):
    def __init__(self, *, is_sync: bool, is_core: bool) -> None:
        self.is_sync = is_sync
        self.is_core = is_core

    @property
    @abstractmethod
    def sync_repo(self) -> type[SyncRepo[T]]:
        pass

    @property
    @abstractmethod
    def async_repo(self) -> type[AsyncRepo[T]]:
        pass

    @abstractmethod
    def get_all(self) -> list[T]:
        pass

    @abstractmethod
    def create(self, data: any) -> None:
        pass
