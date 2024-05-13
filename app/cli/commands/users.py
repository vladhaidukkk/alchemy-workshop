import hashlib
from typing import Annotated, Optional

from pydantic import EmailStr, TypeAdapter, ValidationError
from typer import BadParameter, Context, Option, Typer

from app.cli.common import inject_sub_common
from app.db.core import sync_session
from app.db.models import User

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
    with sync_session() as session:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user = User(
            email=email,
            hashed_password=hashed_password,
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            address=address,
        )
        session.add(user)
        session.commit()
