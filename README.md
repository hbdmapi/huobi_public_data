# Huobi Market Data

For user to get historical market data as csv files, such as kline, trade data, it's the reason that there is this project.
</br></br>

# Spot
* `Kline`
* `Trade`

## Kline
The data fields of kline data as same as `/market/history/kline` REST API interface, and the data fields are as follows:

| id | open | high | low | close | vol | amount |
| -- | -- | -- | --| -- | --| --|
| 1620748800 | 56047.34 | 57352.06 | 55749.73 | 57042.49 | 5.218369366635794E8 | 9222.601164750704 |
</br>

## Periods
Periods are supported as follows: 
`1min`, `5min`, `15min`, `30min`, `60min`, `4hour`, `1day`, `1mon`, `1week`, `1year`
</br></br>

## Trade
The data fields of kline data as same as `/market/trade` REST API interface, and the data fields are as follows:
| id | price | amount | ts | direction |
| -- | -- | -- | --| -- |
| 102176219713 | 4268.68 | 0.0231 | 1620789069405 | buy |
</br></br>

# Futures/Swap/Linear-Swap/Options
* `Kline`
* `Trade`

## Kline
The data fields of kline data as same as `/market/history/kline`(Futures), `/swap-ex/market/history/kline`(Swap), `/linear-swap-ex/market/history/kline`(Linear-Swap), `/option-ex/market/history/kline`(Options) REST API interface, and the data fields are as follows:

| id | open | high | low | close | vol | amount |
| -- | -- | -- | --| -- | --| --|
| 1620748800 | 56146.4 | 57418.2 | 55868 | 57361.2 | 18101556 | 31926.0045740418288417736911359330675244168 |
</br>

## Periods
Periods are supported as follows: 
`1min`, `5min`, `15min`, `30min`, `60min`, `4hour`, `1day`, `1mon`
</br></br>

## Trade
The data fields of kline data as same as `/market/trade`(Futures), `/swap-ex/market/trade`(Swap), `/linear-swap-ex/market/trade`(Linear-Swap), `/option-ex/market/trade`(Options) REST API interface, and the data fields are as follows:
| id | price | amount | quantity | direction | ts |
| -- | -- | -- | --| -- | -- |
| 958050135700000 | 57657.4 | 62 | 0.1075317305324208167555248762517907502 | buy | 1620790956586 |
</br></br>

# Url formation
The base url is `https://data.huobi.vision`
</br></br>

## Kline csv file url as follow:
`{base_url}/data/[spot|futures|swap|linear-swap|options]/[daily|monthly]/kline/{symbol}/{period}/{file}`
</br>such as:</br>
`https://data.huobi.vision/data/spot/daily/kline/HTUSDT/60min/HTUSDT-60min-2021-01-01.zip`</br>
`https://data.huobi.vision/data/spot/monthly/kline/HTUSDT/60min/HTUSDT-60min-2021-01.zip`
</br></br>

## Trade csv file url as follow:
`{base_url}/data/[spot|futures|swap|linear-swap|options]/[daily|monthly]/trade/{symbol}/{file}`
</br>such as:</br>
`https://data.huobi.vision/data/swap/daily/trade/BTCUSDT/BTCUSDT-trade-2021-01-01.zip`</br>
`https://data.huobi.vision/data/swap/monthly/trade/BTCUSDT/BTCUSDT-trade-2021-01.zip`
</br></br>

# How to download
You can download the market data via web browser or by shell/python.</br>
There are python/shell scripts for one key downloading csv files

```shell

# download a single file
curl -s "https://data.huobi.vision/data/swap/daily/trade/BTCUSDT/BTCUSDT-trade-2021-01-01.zip" -o BTCUSDT-trade-2021-01-01.zip

# or
wget "https://data.huobi.vision/data/swap/daily/trade/BTCUSDT/BTCUSDT-trade-2021-01-01.zip"
```
</br></br>

# CHECKSUM
Each zip file has a check key to check the integrity of the file.

```shell
# From Linux, sha256sum -c <zip_file_name.CHECKSUM>
sha256sum -c BTCUSDT-trade-2021-01-01.zip.CHECKSUM

# From MacOS
shasum -a 256 -c BTCUSDT-trade-2021-01-01.zip.CHECKSUM
```
