from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func, insert

from app.csv_loader import csv_loader
from app.db import ModelBase, sync_engine, sync_session


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
    with sync_session.begin() as session:
        mock_users = csv_loader.load("users")
        users = [UserModel(**user) for user in mock_users]
        session.add_all(users)


if __name__ == "__main__":
    _insert_mock_users()
