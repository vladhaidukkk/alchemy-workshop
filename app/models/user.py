from sqlalchemy.orm import Mapped, mapped_column

from app.csv_loader import csv_loader
from app.db.core import ModelBase, sync_session
from app.db.types import created_at, intpk


class UserModel(ModelBase):
    __tablename__ = "users"

    id: Mapped[intpk]
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    created_at: Mapped[created_at]


def _insert_mock_users():
    with sync_session.begin() as session:
        mock_users = csv_loader.load("users")
        users = [UserModel(**user) for user in mock_users]
        session.add_all(users)


if __name__ == "__main__":
    _insert_mock_users()
