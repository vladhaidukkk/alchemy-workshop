from enum import StrEnum, auto
from typing import Annotated

from typer import Context, Option

from .root import RootCommon


class AlchemyMode(StrEnum):
    CORE = auto()
    ORM = auto()


class SubCommon(RootCommon):
    alchemy_mode: AlchemyMode

    @property
    def is_core(self) -> bool:
        return self.alchemy_mode == AlchemyMode.CORE

    @property
    def is_orm(self) -> bool:
        return self.alchemy_mode == AlchemyMode.ORM


def inject_sub_common(
    ctx: Context,
    mode: Annotated[
        AlchemyMode, Option("--mode", "-m", case_sensitive=False)
    ] = AlchemyMode.CORE,
):
    ctx.obj = SubCommon(**ctx.obj.model_dump(), alchemy_mode=mode)
