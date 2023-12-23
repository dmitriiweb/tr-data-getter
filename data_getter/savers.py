import csv
from dataclasses import asdict

from data_getter import schemas


class CsvDataSaver:
    def __init__(self, config: schemas.Config):
        self.config = config

    def save(self, data: list[schemas.OHLCResult]):
        rows = [asdict(row) for row in data]
        headers = list(rows[0].keys())
        is_file_exists = self.config.output_file.exists()
        with open(self.config.output_file, "a") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            if not is_file_exists:
                writer.writeheader()
            writer.writerows(rows)
