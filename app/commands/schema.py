from enum import StrEnum
from typing import Annotated

from typer import Option, Typer

from app.db.core import ModelBase, metadata, sync_engine

# isort: split
import app.tables.users  # noqa

# isort: split
import app.models.order  # noqa
import app.models.user  # noqa


class ExecutionMode(StrEnum):
    CORE = "core"
    ORM = "orm"


app = Typer()


@app.command()
def drop(mode: Annotated[ExecutionMode, Option("--mode", "-m")] = ExecutionMode.ORM):
    if mode == ExecutionMode.ORM:
        ModelBase.metadata.drop_all(sync_engine)
    else:
        metadata.drop_all(sync_engine)


@app.command()
def create(mode: Annotated[ExecutionMode, Option("--mode", "-m")] = ExecutionMode.ORM):
    if mode == ExecutionMode.ORM:
        ModelBase.metadata.create_all(sync_engine)
    else:
        metadata.create_all(sync_engine)


@app.command()
def reset(mode: Annotated[ExecutionMode, Option("--mode", "-m")] = ExecutionMode.ORM):
    if mode == ExecutionMode.ORM:
        ModelBase.metadata.drop_all(sync_engine)
        ModelBase.metadata.create_all(sync_engine)
    else:
        metadata.drop_all(sync_engine)
        metadata.create_all(sync_engine)


if __name__ == "__main__":
    app()
