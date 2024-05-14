from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserBase:
    email: str
    username: str
    first_name: str | None
    last_name: str | None
    phone_number: str | None
    address: str | None


@dataclass
class UserCreate(UserBase):
    hashed_password: str


@dataclass
class UserOutput(UserBase):
    id: int
    created_at: datetime
