from enum import StrEnum

from pydantic import BaseModel


class ExecutionMode(StrEnum):
    CORE = "core"
    ORM = "orm"


class Common(BaseModel):
    mode: ExecutionMode
