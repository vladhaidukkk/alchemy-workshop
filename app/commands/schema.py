from typer import Context, Typer

from app.common import ExecutionMode
from app.db.core import ModelBase, metadata, sync_engine

# isort: split
import app.tables.users  # noqa

# isort: split
import app.models.order  # noqa
import app.models.user  # noqa

app = Typer()


@app.command()
def drop(ctx: Context):
    if ctx.obj.mode == ExecutionMode.ORM:
        ModelBase.metadata.drop_all(sync_engine)
    else:
        metadata.drop_all(sync_engine)


@app.command()
def create(ctx: Context):
    if ctx.obj.mode == ExecutionMode.ORM:
        ModelBase.metadata.create_all(sync_engine)
    else:
        metadata.create_all(sync_engine)


@app.command()
def reset(ctx: Context):
    if ctx.obj.mode == ExecutionMode.ORM:
        ModelBase.metadata.drop_all(sync_engine)
        ModelBase.metadata.create_all(sync_engine)
    else:
        metadata.drop_all(sync_engine)
        metadata.create_all(sync_engine)


if __name__ == "__main__":
    app()
