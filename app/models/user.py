from dataclasses import dataclass


@dataclass
class UserCreate:
    email: str
    hashed_password: str
    username: str
    first_name: str | None
    last_name: str | None
    phone_number: str | None
    address: str | None
