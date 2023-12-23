from datetime import datetime
from typing import Iterator

import pandas as pd
import requests
from tqdm import tqdm

from data_getter import schemas

from .getter import DataGetter


class Bitstamp(DataGetter):
    API_URL = "https://www.bitstamp.net/api/v2/ohlc/{pair}"
    API_PARAMS = {
        "step": 60,  # Get 1-minute candles
        "limit": 1000,
    }

    def get_data(self) -> Iterator[list[schemas.OHLCResult]]:
        date_ranges = self._get_date_ranges()
        for start_date, end_date in tqdm(
            zip(date_ranges, date_ranges[1:]), total=len(date_ranges)
        ):
            params = self.API_PARAMS.copy()
            params["start"] = start_date
            params["end"] = end_date

            r = requests.get(
                self.API_URL.format(pair=self.config.symbol), params=params
            )
            results = [
                schemas.OHLCResult(
                    symbol=self.config.symbol,
                    date=datetime.fromtimestamp(int(i["timestamp"])),
                    open=i["open"],
                    high=i["high"],
                    low=i["low"],
                    close=i["close"],
                    volume=i["volume"],
                )
                for i in r.json()["data"]["ohlc"]
            ]
            yield results

    def _get_date_ranges(self) -> list[int]:
        dates = pd.date_range(self.config.start_date, self.config.end_date, freq="6H")
        dates = [int(x.value / 10**9) for x in dates]
        return dates
