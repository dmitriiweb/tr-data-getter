from .getter import DataGetter
from .bitmap import Bitstamp
from data_getter import DataGetter as DataGetterEnum, Config


def get_data_getter(config: Config) -> DataGetter:
    match config.data_getter:
        case DataGetterEnum.BITSTAMP:
            return Bitstamp(config)
        case _:
            raise ValueError(f"{config.data_getter} is not a valid DataGetter")