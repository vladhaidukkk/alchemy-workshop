from typing import Sequence

from sqlalchemy.sql import select

from app.db.core import async_session, sync_session
from app.db.models import User

from .repo import AsyncOrmRepo, SyncOrmRepo


class SyncOrmUsersRepository(SyncOrmRepo[User]):
    @staticmethod
    def get_all() -> Sequence[User]:
        with sync_session() as session:
            query = session.query(User)
            return query.all()


class AsyncOrmUsersRepository(AsyncOrmRepo[User]):
    @staticmethod
    async def get_all() -> Sequence[User]:
        async with async_session() as session:
            query = select(User)
            result = await session.execute(query)
            return result.scalars().all()
