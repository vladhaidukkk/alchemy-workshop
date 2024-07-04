import asyncio

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
    def sync_repo(self) -> type[SyncRepo[User]]:
        return SyncCoreUsersRepo if self.is_core else SyncOrmUsersRepo

    @property
    def async_repo(self) -> type[AsyncRepo[User]]:
        return AsyncCoreUsersRepo if self.is_core else AsyncOrmUsersRepo

    def get_all(self) -> list[User]:
        if self.is_sync:
            return self.sync_repo.get_all()
        return asyncio.run(self.async_repo.get_all())

    def create(self, data: UserCreate) -> None:
        if self.is_sync:
            self.sync_repo.create(data)
        else:
            asyncio.run(self.async_repo.create(data))
