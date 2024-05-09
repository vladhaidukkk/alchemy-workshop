import asyncio
import sys
from itertools import islice

from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import text

from app.config import settings

echo = True
pool_size = 5  # default
max_overflow = 10  # default

sync_engine = create_engine(
    url=settings.sync_db_url,
    echo=echo,
    pool_size=pool_size,
    max_overflow=max_overflow,
)
async_engine = create_async_engine(
    url=settings.async_db_url,
    echo=echo,
    pool_size=pool_size,
    max_overflow=max_overflow,
)

metadata = MetaData()


class ModelBase(DeclarativeBase):
    pass


def _get_db_version():
    with sync_engine.connect() as conn:
        query = text("SELECT VERSION()")
        result = conn.execute(query)
        return result.scalar()


async def _get_db_version_async():
    async with async_engine.connect() as conn:
        query = text("SELECT VERSION()")
        result = await conn.execute(query)
        return result.scalar()


if __name__ == "__main__":
    mode = next(islice(sys.argv, 1, None), "sync").lower()
    version = (
        _get_db_version() if mode == "sync" else asyncio.run(_get_db_version_async())
    )
    print(version)
