# Huobi Market Data

For user to get historical market data as csv files, such as kline, trade data, it's the reason that there is this project.
</br></br>

# Spot
* `Kline`
* `Trade`

## Kline
The data fields of kline data as same as `/market/history/kline` REST API interface, and the data fields are as follows:

| id | open | close | high | low | vol | amount |
| -- | -- | -- | -- | -- | -- | -- |
| 1621267200 | 43342.5 | 45004.68 | 45781.52 | 42106.0 | 1.5694329022947967E9 | 35623.935414808795 |
</br>

## Periods
Periods are supported as follows: 
`1min`, `5min`, `15min`, `30min`, `60min`, `4hour`, `1day`, `1mon`, `1week`, `1year`
</br></br>

## Trade
The data fields of kline data as same as `/market/trade` REST API interface, and the data fields are as follows:
| id | ts | price | amount | direction |
| -- | -- | -- | --| -- |
| 102189537905 | 1621331937334 | 3471.95 | 0.0653 | buy |
</br>

# Future/Swap/Linear-Swap/Option
* `Kline`
* `Trade`

## Kline
The data fields of kline data as same as `/market/history/kline`(Future), `/swap-ex/market/history/kline`(Swap), `/linear-swap-ex/market/history/kline`(Linear-Swap), `/option-ex/market/history/kline`(Option) REST API interface, and the data fields are as follows:

| id | open | close | high | low | vol | amount |
| -- | -- | -- | -- | -- | -- | -- |
| 1621332060 | 45707.76 | 45705.88 | 45725.05 | 45700.89 | 13220 | 28.9204701984171414886879489503784944634 |
</br>

## Periods
Periods are supported as follows: 
`1min`, `5min`, `15min`, `30min`, `60min`, `4hour`, `1day`, `1mon`
</br></br>

## Trade
The data fields of kline data as same as `/market/trade`(Future), `/swap-ex/market/trade`(Swap) REST API interface, and the data fields are as follows:
| id | ts | price | amount | quantity | direction |
| -- | -- | -- | -- | -- | -- |
| 1358791271630000 | 1621332195189 | 45665.58 | 2 | 0.0043796662606716043024089478333572025 | sell |
</br>

The data fields of kline data as same as `/linear-swap-ex/market/trade`(Linear-Swap), `/option-ex/market/trade`(Option) REST API interface, and the data fields are as follows:
| id | ts | price | amount | quantity | trade_turnover | direction |
| -- | -- | -- | -- | -- | -- | -- |
| 363599553790000 | 1621332282860 | 45004.1 | 424 | 0.424 | 19081.7384 | sell |
</br>

# Url formation
The base url is `https://futures.huobi.com`
</br></br>

## Kline csv file url as follow:
`{base_url}/data/klines/[spot|future|swap|linear-swap|option]/[daily|monthly]/{symbol}/{period}/{file}`
</br>such as:</br>
`https://futures.huobi.com/data/klines/spot/daily/HTUSDT/60min/HTUSDT-60min-2021-01-01.zip`</br>
`https://futures.huobi.com/data/klines/spot/monthly/HTUSDT/60min/HTUSDT-60min-2021-01.zip`
</br></br>

## Trade csv file url as follow:
`{base_url}/data/trades/[spot|future|swap|linear-swap|option]/[daily|monthly]/{symbol}/{file}`
</br>such as:</br>
`https://futures.huobi.com/data/trades/swap/daily/BTC-USD/BTC-USD-trades-2021-01-01.zip`</br>
`https://futures.huobi.com/data/trades/swap/monthly/BTC-USD/BTC-USD-trades-2021-01.zip`
</br></br>

# How to download
You can download the market data via web browser or by shell/python.</br>
There are python/shell scripts for one key downloading csv files

```shell

# download a single file
curl -s "https://futures.huobi.com/data/trades/linear-swap/daily/BTC-USDT/BTC-USDT-trades-2021-01-01.zip" -o BTC-USDT-trades-2021-01-01.zip

# or
wget "https://futures.huobi.com/data/trades/linear-swap/daily/BTC-USDT/BTC-USDT-trades-2021-01-01.zip"
```
</br></br>

# CHECKSUM
Each zip file has a check key to check the integrity of the file.

```shell
# From Linux, sha256sum -c <zip_file_name.CHECKSUM>
sha256sum -c BTC-USDT-trades-2021-01-01.CHECKSUM

# From MacOS
shasum -a 256 -c BTC-USDT-trades-2021-01-01.CHECKSUM
```
