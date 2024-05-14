from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.db.core import Base
from app.db.types import created_at, intpk, updated_at


class ResumeModel(Base):
    __tablename__ = "resumes"

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    title: Mapped[str]
    industry: Mapped[str]
    content: Mapped[str]
    skills: Mapped[list[str]] = mapped_column(JSONB, server_default="[]")
    languages: Mapped[list[str]] = mapped_column(JSONB, server_default="[]")
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
