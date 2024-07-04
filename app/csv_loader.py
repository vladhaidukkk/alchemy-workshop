import csv
from functools import cache


@cache
def load_csv(filepath: str) -> list[dict]:
    with open(filepath) as file:
        reader = csv.DictReader(file)
        return list(reader)


class CSVLoader:
    def __init__(self, dir_path: str) -> None:
        self.dir_path = dir_path

    def load(self, filename: str) -> list[dict]:
        return load_csv(filepath=f"{self.dir_path}/{filename}.csv")


csv_loader = CSVLoader(dir_path="data")
