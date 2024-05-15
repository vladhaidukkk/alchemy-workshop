import asyncio
from typing import Type

from app.models import User, UserCreate

from .repo import AsyncRepo, RepoFactory, SyncRepo
from .users import (
    AsyncCoreUsersRepo,
    AsyncOrmUsersRepo,
    SyncCoreUsersRepo,
    SyncOrmUsersRepo,
)


class UsersRepoFactory(RepoFactory[User]):
    @property
    def sync_repo(self) -> Type[SyncRepo[User]]:
        return SyncCoreUsersRepo if self.is_core else SyncOrmUsersRepo

    @property
    def async_repo(self) -> Type[AsyncRepo[User]]:
        return AsyncCoreUsersRepo if self.is_core else AsyncOrmUsersRepo

    def get_all(self) -> list[User]:
        if self.is_sync:
            return self.sync_repo.get_all()
        else:
            return asyncio.run(self.async_repo.get_all())

    def create(self, data: UserCreate) -> None:
        if self.is_sync:
            self.sync_repo.create(data)
        else:
            asyncio.run(self.async_repo.create(data))
