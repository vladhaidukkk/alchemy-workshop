import asyncio
from typing import Annotated

from rich import print
from sqlalchemy.sql import text
from typer import Context, Option, Typer

import app.commands.schema as schema
from app.common import Common, ExecutionMode
from app.db.core import async_engine, sync_engine

app = Typer()


@app.callback()
def common(
    ctx: Context,
    mode: Annotated[ExecutionMode, Option("--mode", "-m")] = ExecutionMode.ORM,
):
    ctx.obj = Common(mode=mode)


def _get_db_version():
    with sync_engine.connect() as conn:
        query = text("SELECT VERSION()")
        result = conn.execute(query)
        return result.scalar()


async def _get_db_version_async():
    async with async_engine.connect() as conn:
        query = text("SELECT VERSION()")
        result = await conn.execute(query)
        return result.scalar()


@app.command()
def version(async_: Annotated[bool, Option("--async", "-a")] = False):
    ver = asyncio.run(_get_db_version_async()) if async_ else _get_db_version()
    print(ver)


app.add_typer(schema.app, name="schema")


if __name__ == "__main__":
    app()
