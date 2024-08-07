from typer import Context, Typer

from app.cli.common import inject_sub_common
from app.db.core import Base, metadata, sync_engine

# isort: split
from app.db.tables import resumes_table, users_table  # noqa: F401

# isort: split
from app.db.models import ResumeModel, UserModel  # noqa: F401

app = Typer(callback=inject_sub_common)


@app.command()
def drop(ctx: Context) -> None:
    if ctx.obj.is_core:
        metadata.drop_all(sync_engine)
    else:
        Base.metadata.drop_all(sync_engine)


@app.command()
def create(ctx: Context) -> None:
    if ctx.obj.is_core:
        metadata.create_all(sync_engine)
    else:
        Base.metadata.create_all(sync_engine)


@app.command()
def reset(ctx: Context) -> None:
    if ctx.obj.is_core:
        metadata.drop_all(sync_engine)
        metadata.create_all(sync_engine)
    else:
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
