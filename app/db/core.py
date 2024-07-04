from datetime import datetime
from typing import ClassVar

from sqlalchemy import DateTime, MetaData, create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

sync_engine = create_engine(
    url=settings.sync_db_url,
    echo=settings.echo,
    pool_size=settings.pool_size,
    max_overflow=settings.max_overflow,
)
async_engine = create_async_engine(
    url=settings.async_db_url,
    echo=settings.echo,
    pool_size=settings.pool_size,
    max_overflow=settings.max_overflow,
)

sync_session = sessionmaker(sync_engine)
async_session = async_sessionmaker(async_engine)

metadata = MetaData()


class Base(DeclarativeBase):
    # Define mappings from Python types to SQLAlchemy types,
    # e.g. Mapped[datetime] -> DateTime(timezone=True)
    type_annotation_map: ClassVar[dict] = {
        datetime: DateTime(timezone=True),
    }
