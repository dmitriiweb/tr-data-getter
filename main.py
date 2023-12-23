from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

import pandas as pd
import typer
from typing_extensions import Annotated

import data_getter as dg


def data_postprocessing(config: dg.schemas.Config):
    df = pd.read_csv(config.output_file)
    df.drop_duplicates(inplace=True)
    df["date"] = pd.to_datetime(df["date"])
    df = df[df["date"] >= config.start_date]
    df = df[df["date"] <= config.end_date]
    df.sort_values(by=["date"], inplace=True)
    df.to_csv(config.output_file, index=False)


def main(
    symbol: Annotated[
        str,
        typer.Option(
            "--symbol",
            "-s",
            help="Symbol to fetch data for, e.g. btcusd",
        ),
    ],
    output_file: Annotated[
        Path, typer.Option("--output-file", "-o", help="Path to csv file to write to")
    ],
    data_getter: Annotated[
        str,
        typer.Option(
            "--data-getter",
            "-g",
            help="Data getter to use, must be one of: bitstamp",
        ),
    ] = "bitstamp",
    start_date: Annotated[
        Optional[datetime],
        typer.Option(
            "--start-date",
            help="Start date of data to fetch, if not specified, will use datetime.now() - 365 days",
        ),
    ] = None,
    end_date: Annotated[
        Optional[datetime],
        typer.Option(
            "--end-date",
            help="End date of data to fetch, if not specified, will use datetime.now()",
        ),
    ] = None,
):
    config = dg.Config(
        symbol=symbol,
        output_file=output_file,
        data_getter=dg.DataGetter.from_string(data_getter),
        start_date=start_date or datetime.now() - timedelta(days=365),
        end_date=end_date or datetime.now(),
    )
    data_getter = dg.getters.get_data_getter(config)
    datas = data_getter.get_data()
    saver = dg.savers.CsvDataSaver(config)
    for data in datas:
        saver.save(data)

    data_postprocessing(config)


if __name__ == "__main__":
    typer.run(main)
