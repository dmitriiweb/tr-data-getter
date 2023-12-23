from abc import ABC, abstractmethod
from typing import Iterator

from data_getter import schemas


class DataGetter(ABC):
    def __init__(self, config: schemas.Config):
        self.config = config

    @abstractmethod
    def get_data(self) -> Iterator[list[schemas.OHLCResult]]:
        ...
