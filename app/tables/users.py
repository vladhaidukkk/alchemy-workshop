from sqlalchemy import Column, Integer, String, Table, DateTime
from sqlalchemy.sql import func, insert

from app.db import metadata, sync_engine

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
        stmt = insert(users_table).values(
            [
                {
                    "email": "john.doe@example.com",
                    "hashed_password": "hashed_password1",
                    "first_name": "John",
                    "last_name": "Doe",
                },
                {
                    "email": "jane.smith@example.com",
                    "hashed_password": "hashed_password2",
                    "first_name": "Jane",
                    "last_name": "Smith",
                },
                {
                    "email": "alice.johnson@example.com",
                    "hashed_password": "hashed_password3",
                    "first_name": "Alice",
                    "last_name": "Johnson",
                },
            ]
        )
        conn.execute(stmt)


if __name__ == "__main__":
    _insert_mock_users()
