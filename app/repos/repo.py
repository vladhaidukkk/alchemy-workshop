from abc import ABC, abstractmethod


class SyncRepo[T](ABC):
    @staticmethod
    @abstractmethod
    def get_all() -> list[T]:
        pass


class AsyncRepo[T](ABC):
    @staticmethod
    @abstractmethod
    async def get_all() -> list[T]:
        pass
