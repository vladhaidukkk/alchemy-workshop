from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    username: str
    first_name: str | None
    last_name: str | None
    phone_number: str | None
    address: str | None


class User(UserBase):
    id: int
    hashed_password: str
    created_at: datetime


class UserCreate(UserBase):
    hashed_password: str


class UserOutput(UserBase):
    id: int
    created_at: datetime
