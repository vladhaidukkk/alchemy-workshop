from typer import Context, Typer

from app.common import ExecutionMode
from app.db.core import ModelBase, metadata, sync_engine

# isort: split
from app.tables.users import users_table  # noqa

# isort: split
from app.models.order import OrderModel  # noqa
from app.models.user import UserModel  # noqa

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
