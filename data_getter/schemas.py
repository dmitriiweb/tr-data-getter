from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from pathlib import Path


class DataGetter(str, Enum):
    BITSTAMP = "bitstamp"

    @classmethod
    def from_string(cls, value: str) -> DataGetter:
        try:
            return cls(value)
        except ValueError:
            raise ValueError(f"{value} is not a valid DataGetter")


@dataclass
class Config:
    start_date: datetime
    end_date: datetime
    data_getter: DataGetter
    symbol: str
    output_file: Path


@dataclass
class OHLCResult:
    symbol: str
    date: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float
