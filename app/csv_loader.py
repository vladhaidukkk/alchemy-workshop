import csv
from functools import cache


class CSVLoader:
    def __init__(self, dir_path: str):
        self.dir_path = dir_path

    @cache
    def load(self, filename: str) -> list[dict]:
        with open(f"{self.dir_path}/{filename}.csv") as file:
            reader = csv.DictReader(file)
            return list(reader)


csv_loader = CSVLoader(dir_path="data")
