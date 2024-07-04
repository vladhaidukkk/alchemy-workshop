import asyncio

from sqlalchemy.sql import text
from typer import Context, Typer

from app.cli.commands import schema_app, users_app
from app.cli.common import inject_root_common
from app.cli.console import console
from app.config import settings
from app.db.core import async_engine, sync_engine

app = Typer(callback=inject_root_common, pretty_exceptions_show_locals=settings.debug)


def _get_db_version() -> str:
    with sync_engine.connect() as conn:
        query = text("SELECT VERSION()")
        result = conn.execute(query)
        return result.scalar()


async def _get_db_version_async() -> str:
    async with async_engine.connect() as conn:
        query = text("SELECT VERSION()")
        result = await conn.execute(query)
        return result.scalar()


@app.command()
def version(ctx: Context) -> None:
    ver = _get_db_version() if ctx.obj.is_sync else asyncio.run(_get_db_version_async())
    console.print(ver)


app.add_typer(schema_app, name="schema")
app.add_typer(users_app, name="users")
