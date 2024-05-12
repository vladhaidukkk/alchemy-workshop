from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel
from typer import Context, Option


class ExecutionMode(StrEnum):
    CORE = "core"
    ORM = "orm"


class Common(BaseModel):
    mode: ExecutionMode


def inject_common(
    ctx: Context,
    mode: Annotated[ExecutionMode, Option("--mode", "-m")] = ExecutionMode.ORM,
):
    ctx.obj = Common(mode=mode)
