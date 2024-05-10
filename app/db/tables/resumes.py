from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func

from app.db.core import metadata

resumes_table = Table(
    "resumes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), nullable=False),
    Column("title", String, nullable=False),
    Column("industry", String, nullable=False),
    Column("content", String, nullable=False),
    Column("skills", JSONB, nullable=False, server_default="[]"),
    Column("languages", JSONB, nullable=False, server_default="[]"),
    Column(
        "created_at",
        DateTime(timezone=True),
        nullable=False,
        server_default=func.current_timestamp(),
    ),
    Column(
        "updated_at",
        DateTime(timezone=True),
        nullable=False,
        server_default=func.current_timestamp(),
        onupdate=datetime.now,
    ),
)
