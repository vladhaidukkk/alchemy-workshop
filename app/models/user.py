from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func, insert

from app.csv_loader import csv_loader
from app.db import ModelBase, sync_engine


class UserModel(ModelBase):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )


def _insert_mock_users():
    with sync_engine.begin() as conn:
        mock_users = csv_loader.load("users")
        stmt = insert(UserModel).values(mock_users)
        conn.execute(stmt)


if __name__ == "__main__":
    _insert_mock_users()
