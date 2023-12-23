# tr-data-getter

Tools to download 1-minute OHLC data from bitstamp.net


## Installation
```bash
git clone git@github.com:dmitriiweb/tr-data-getter.git
cd tr-data-getter
poetry shell
poetry install
```

## Usage
```bash
poetry shell
python main.py --help
```

## Example
```bash
poetry shell
python main.py -s ethusd -o eth-usd.csv --start-date 2023-12-20
cat ethusd.csv
symbol,date,open,high,low,close,volume
ethusd,2023-12-20 00:00:00,2177.0,2178.6,2177.0,2178.6,7.8709
ethusd,2023-12-20 00:01:00,2178.2,2178.2,2178.0,2178.2,0.24596564
ethusd,2023-12-20 00:02:00,2178.5,2178.9,2177.2,2177.2,1.82661474
ethusd,2023-12-20 00:03:00,2179.0,2179.0,2179.0,2179.0,0.013
ethusd,2023-12-20 00:04:00,2179.0,2179.0,2179.0,2179.0,0.0
ethusd,2023-12-20 00:05:00,2176.8,2176.9,2170.6,2171.3,9.02953846
ethusd,2023-12-20 00:06:00,2170.7,2171.9,2170.0,2170.0,2.8935
ethusd,2023-12-20 00:07:00,2169.2,2171.0,2165.3,2167.5,32.48347483
ethusd,2023-12-20 00:08:00,2165.6,2165.9,2165.0,2165.0,7.39897433
ethusd,2023-12-20 00:09:00,2164.7,2166.2,2163.5,2165.7,28.97833365
...
```