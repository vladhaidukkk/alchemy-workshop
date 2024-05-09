from sqlalchemy import Column, DateTime, Integer, String, Table
from sqlalchemy.sql import func, insert

from app.csv_loader import csv_loader
from app.db.core import metadata, sync_engine

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False, unique=True),
    Column("hashed_password", String, nullable=False),
    Column("first_name", String, nullable=False),
    Column("last_name", String, nullable=False),
    Column(
        "created_at",
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    ),
)


def _insert_mock_users():
    with sync_engine.begin() as conn:
        mock_users = csv_loader.load("users")
        stmt = insert(users_table).values(mock_users)
        conn.execute(stmt)


if __name__ == "__main__":
    _insert_mock_users()
