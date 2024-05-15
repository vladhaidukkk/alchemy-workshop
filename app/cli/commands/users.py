import asyncio
import hashlib
from typing import Annotated, Optional

from pydantic import EmailStr, TypeAdapter, ValidationError
from typer import BadParameter, Context, Option, Typer

from app.cli.common import inject_sub_common
from app.cli.console import print_model_as_table
from app.models import UserCreate, UserOutput
from app.repos import (
    AsyncCoreUsersRepository,
    AsyncOrmUsersRepository,
    SyncCoreUsersRepository,
    SyncOrmUsersRepository,
)

app = Typer(callback=inject_sub_common)


def email_validator(value: str) -> str:
    try:
        TypeAdapter(EmailStr).validate_python(value)
    except ValidationError as err:
        error = err.errors()[0]
        msg = error.get("ctx", {}).get("reason") or error["msg"]
        raise BadParameter(msg)
    return value


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
            SyncCoreUsersRepository.create(new_user_data)
        else:
            asyncio.run(AsyncCoreUsersRepository.create(new_user_data))
    else:
        if ctx.obj.is_sync:
            SyncOrmUsersRepository.create(new_user_data)
        else:
            asyncio.run(AsyncOrmUsersRepository.create(new_user_data))


def _get_users_sync_core() -> list[UserOutput]:
    users = SyncCoreUsersRepository.get_all()
    return [UserOutput(**user.model_dump()) for user in users]


async def _get_users_async_core() -> list[UserOutput]:
    users = await AsyncCoreUsersRepository.get_all()
    return [UserOutput(**user.model_dump()) for user in users]


def _get_users_sync_orm() -> list[UserOutput]:
    users = SyncOrmUsersRepository.get_all()
    return [UserOutput(**user.model_dump()) for user in users]


async def _get_users_async_orm() -> list[UserOutput]:
    users = await AsyncOrmUsersRepository.get_all()
    return [UserOutput(**user.model_dump()) for user in users]


@app.command("list")
def list_(ctx: Context):
    if ctx.obj.is_core:
        if ctx.obj.is_sync:
            users = _get_users_sync_core()
        else:
            users = asyncio.run(_get_users_async_core())
    else:
        if ctx.obj.is_sync:
            users = _get_users_sync_orm()
        else:
            users = asyncio.run(_get_users_async_orm())
    print_model_as_table(model=UserOutput, data=users, title="Users")
