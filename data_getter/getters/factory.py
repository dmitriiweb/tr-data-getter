from data_getter import schemas

from .bitmap import Bitstamp
from .getter import DataGetter


def get_data_getter(config: schemas.Config) -> DataGetter:
    match config.data_getter:
        case schemas.DataGetter.BITSTAMP:
            return Bitstamp(config)
        case _:
            raise ValueError(f"{config.data_getter} is not a valid DataGetter")
