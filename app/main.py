from typing import Annotated

from typer import Context, Option, Typer

import app.commands.schema as schema
from app.common import Common, ExecutionMode

app = Typer()


@app.callback()
def common(
    ctx: Context,
    mode: Annotated[ExecutionMode, Option("--mode", "-m")] = ExecutionMode.ORM,
):
    ctx.obj = Common(mode=mode)


app.add_typer(schema.app, name="schema")


def main():
    app()


if __name__ == "__main__":
    main()
