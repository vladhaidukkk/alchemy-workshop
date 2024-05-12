from enum import StrEnum, auto
from typing import Annotated

from pydantic import BaseModel
from typer import Context, Option


class ProcessingMode(StrEnum):
    SYNC = auto()
    ASYNC = auto()


class RootCommon(BaseModel):
    processing_mode: ProcessingMode

    @property
    def is_sync(self) -> bool:
        return self.processing_mode == ProcessingMode.SYNC

    @property
    def is_async(self) -> bool:
        return self.processing_mode == ProcessingMode.ASYNC


def inject_root_common(
    ctx: Context,
    async_: Annotated[bool, Option("--async", "-a")] = False,
):
    ctx.obj = RootCommon(
        processing_mode=ProcessingMode.ASYNC if async_ else ProcessingMode.SYNC,
    )
