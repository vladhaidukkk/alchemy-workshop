from sqlalchemy.orm import Mapped, mapped_column

from app.db.core import Base
from app.db.types import created_at, intpk


class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    username: Mapped[str] = mapped_column(unique=True)
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    phone_number: Mapped[str | None]
    address: Mapped[str | None]
    created_at: Mapped[created_at]
