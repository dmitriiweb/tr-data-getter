from abc import ABC, abstractmethod
from data_getter import Config


class DataGetter(ABC):
    def __init__(self, config: Config):
        self.config = config
    @abstractmethod
    def get_data(self):
        ...
