import typer
from pathlib import Path
from datetime import datetime, timedelta
from typing_extensions import Annotated


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
        datetime,
        typer.Option(
            "--start-date",
            "-s",
            help="Start date of data to fetch, if not specified, will use datetime.now() - 365 days",
        ),
    ] = None,
    end_date: Annotated[
        datetime,
        typer.Option(
            "--end-date",
            "-e",
            help="End date of data to fetch, if not specified, will use datetime.now()",
        ),
    ] = None,
):
    pass


if __name__ == "__main__":
    typer.run(main)
