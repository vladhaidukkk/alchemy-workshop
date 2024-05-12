import asyncio
from typing import Annotated

from rich import print
from sqlalchemy.sql import text
from typer import Option, Typer

from app.cli.commands import schema_app
from app.cli.common import inject_common
from app.config import settings
from app.db.core import async_engine, sync_engine

app = Typer(callback=inject_common, pretty_exceptions_show_locals=settings.debug)


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


app.add_typer(schema_app, name="schema")


if __name__ == "__main__":
    app()
