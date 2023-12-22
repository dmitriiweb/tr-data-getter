from data_getter import schemas

from .getter import DataGetter


class Bitstamp(DataGetter):
    def get_data(self) -> list[schemas.OHLCResult]:
        print("Getting data from Bitstamp")
