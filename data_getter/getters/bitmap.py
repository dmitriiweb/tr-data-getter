from .getter import DataGetter


class Bitstamp(DataGetter):
    def get_data(self):
        print("Getting data from Bitstamp")
