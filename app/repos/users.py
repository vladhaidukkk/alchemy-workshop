from sqlalchemy.sql import insert, select

from app.db.core import async_engine, async_session, sync_engine, sync_session
from app.db.models import UserModel
from app.db.tables import users_table
from app.models import User, UserCreate

from .repo import AsyncRepo, SyncRepo


class SyncCoreUsersRepository(SyncRepo[User]):
    @staticmethod
    def get_all() -> list[User]:
        with sync_engine.connect() as conn:
            query = select(users_table)
            result = conn.execute(query)
            users = result.mappings().all()
        return [User(**user) for user in users]

    @staticmethod
    def create(data: UserCreate) -> None:
        with sync_engine.connect() as conn:
            stmt = insert(users_table).values(**data.model_dump())
            conn.execute(stmt)
            conn.commit()


class AsyncCoreUsersRepository(AsyncRepo[User]):
    @staticmethod
    async def get_all() -> list[User]:
        async with async_engine.connect() as conn:
            query = select(users_table)
            result = await conn.execute(query)
            users = result.mappings().all()
        return [User(**user) for user in users]

    @staticmethod
    async def create(data: UserCreate) -> None:
        async with async_engine.connect() as conn:
            stmt = insert(users_table).values(**data.model_dump())
            await conn.execute(stmt)
            await conn.commit()


class SyncOrmUsersRepository(SyncRepo[User]):
    @staticmethod
    def get_all() -> list[User]:
        with sync_session() as session:
            query = select(UserModel.__table__)
            result = session.execute(query)
            users = result.mappings().all()
        return [User(**user) for user in users]

    @staticmethod
    def create(data: UserCreate) -> None:
        with sync_session() as session:
            user = UserModel(**data.model_dump())
            session.add(user)
            session.commit()


class AsyncOrmUsersRepository(AsyncRepo[User]):
    @staticmethod
    async def get_all() -> list[User]:
        async with async_session() as session:
            query = select(UserModel.__table__)
            result = await session.execute(query)
            users = result.mappings().all()
        return [User(**user) for user in users]

    @staticmethod
    async def create(data: UserCreate) -> None:
        async with async_session() as session:
            user = UserModel(**data.model_dump())
            session.add(user)
            await session.commit()
