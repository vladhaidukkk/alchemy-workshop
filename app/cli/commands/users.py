import asyncio
import hashlib
from dataclasses import asdict
from typing import Annotated, Optional

from pydantic import EmailStr, TypeAdapter, ValidationError
from sqlalchemy.sql import insert
from typer import BadParameter, Context, Option, Typer

from app.cli.common import inject_sub_common
from app.db.core import async_engine, async_session, sync_engine, sync_session
from app.db.models import User
from app.db.tables import users_table
from app.models import UserCreate

app = Typer(callback=inject_sub_common)


def email_validator(value: str) -> str:
    try:
        TypeAdapter(EmailStr).validate_python(value)
    except ValidationError as err:
        error = err.errors()[0]
        msg = error.get("ctx", {}).get("reason") or error["msg"]
        raise BadParameter(msg)
    return value


def _create_user_sync_core(data: UserCreate):
    with sync_engine.connect() as conn:
        stmt = insert(users_table).values(**asdict(data))
        conn.execute(stmt)
        conn.commit()


async def _create_user_async_core(data: UserCreate):
    async with async_engine.connect() as conn:
        stmt = insert(users_table).values(**asdict(data))
        await conn.execute(stmt)
        await conn.commit()


def _create_user_sync_orm(data: UserCreate):
    with sync_session() as session:
        user = User(**asdict(data))
        session.add(user)
        session.commit()


async def _create_user_async_orm(data: UserCreate):
    async with async_session() as session:
        user = User(**asdict(data))
        session.add(user)
        await session.commit()


@app.command()
def create(
    ctx: Context,
    email: Annotated[
        str,
        Option(
            "--email", "-e", prompt=True, callback=email_validator, show_default=False
        ),
    ],
    password: Annotated[
        str,
        Option("--password", "-p", prompt=True, hide_input=True, show_default=False),
    ],
    username: Annotated[
        str, Option("--username", "-u", prompt=True, show_default=False)
    ],
    first_name: Annotated[
        Optional[str], Option("--fname", "-f", prompt=True, prompt_required=False)
    ] = None,
    last_name: Annotated[
        Optional[str], Option("--lname", "-l", prompt=True, prompt_required=False)
    ] = None,
    phone_number: Annotated[
        Optional[str], Option("--phone", "-ph", prompt=True, prompt_required=False)
    ] = None,
    address: Annotated[
        Optional[str], Option("--address", "-a", prompt=True, prompt_required=False)
    ] = None,
):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    new_user_data = UserCreate(
        email=email,
        hashed_password=hashed_password,
        username=username,
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        address=address,
    )

    if ctx.obj.is_core:
        if ctx.obj.is_sync:
            _create_user_sync_core(new_user_data)
        else:
            asyncio.run(_create_user_async_core(new_user_data))
    else:
        if ctx.obj.is_sync:
            _create_user_sync_orm(new_user_data)
        else:
            asyncio.run(_create_user_async_orm(new_user_data))