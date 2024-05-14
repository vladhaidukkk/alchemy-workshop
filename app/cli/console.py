from typing import Type

from pydantic import BaseModel
from rich.console import Console
from rich.table import Table

console = Console()


def print_model_as_table[
    T: BaseModel
](model: Type[T], data: list[T], title: str | None = None) -> None:
    title = title or model.__name__
    headers = model.__fields__.keys()
    table = Table(*headers, title=title)
    for row in data:
        table.add_row(*(str(value) for value in row.model_dump().values()))
    console.print(table)
