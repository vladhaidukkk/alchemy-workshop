from sqlalchemy.sql import select

from app.db.core import async_engine, async_session, sync_engine, sync_session
from app.db.models import UserModel
from app.db.tables import users_table
from app.models import User

from .repo import AsyncRepo, SyncRepo


class SyncCoreUsersRepository(SyncRepo[User]):
    @staticmethod
    def get_all() -> list[User]:
        with sync_engine.connect() as conn:
            query = select(users_table)
            result = conn.execute(query)
            users = result.mappings().all()
        return [User(**user) for user in users]


class AsyncCoreUsersRepository(AsyncRepo[User]):
    @staticmethod
    async def get_all() -> list[User]:
        async with async_engine.connect() as conn:
            query = select(users_table)
            result = await conn.execute(query)
            users = result.mappings().all()
        return [User(**user) for user in users]


class SyncOrmUsersRepository(SyncRepo[User]):
    @staticmethod
    def get_all() -> list[User]:
        with sync_session() as session:
            query = select(UserModel.__table__)
            result = session.execute(query)
            users = result.mappings().all()
        return [User(**user) for user in users]


class AsyncOrmUsersRepository(AsyncRepo[User]):
    @staticmethod
    async def get_all() -> list[User]:
        async with async_session() as session:
            query = select(UserModel.__table__)
            result = await session.execute(query)
            users = result.mappings().all()
        return [User(**user) for user in users]
