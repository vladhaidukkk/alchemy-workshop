from sqlalchemy import Column, DateTime, Integer, String, Table
from sqlalchemy.sql import func

from app.db.core import metadata

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False, unique=True),
    Column("hashed_password", String, nullable=False),
    Column("username", String, nullable=False, unique=True),
    Column("first_name", String),
    Column("last_name", String),
    Column("phone_number", String),
    Column("address", String),
    Column(
        "created_at",
        DateTime(timezone=True),
        nullable=False,
        server_default=func.current_timestamp(),
    ),
)
