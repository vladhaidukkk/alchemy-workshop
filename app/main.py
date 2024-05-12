import asyncio

from rich import print
from sqlalchemy.sql import text
from typer import Context, Typer

from app.cli.commands import schema_app
from app.cli.common import inject_root_common
from app.config import settings
from app.db.core import async_engine, sync_engine

app = Typer(callback=inject_root_common, pretty_exceptions_show_locals=settings.debug)


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
def version(ctx: Context):
    ver = _get_db_version() if ctx.obj.is_sync else asyncio.run(_get_db_version_async())
    print(ver)


app.add_typer(schema_app, name="schema")


if __name__ == "__main__":
    app()
