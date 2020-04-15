# Task1 Get hourly candle data from CryptoCompare

[CryptoCompare](https://www.cryptocompare.com/) is a free cryptocurrency data source, where you can download market data, social media, news about cryptocurrencies. This task requires you to download data from CryptoCompare and do basic formatting.

## 1. Explore CryptoCompare Data API

[CryptoCompare Homepage](https://min-api.cryptocompare.com/)

[CryptoCompare Data API Documentation](https://min-api.cryptocompare.com/documentation)

### Required

#### 1. **Write a function** to download histohour data, parameters:

fsym: BTC, tsym: USDT, start_time="2017-04-01", end_time="2020-04-01", e='binance'

Hint:

1. check this url: https://min-api.cryptocompare.com/documentation?key=Historical&cat=dataHistohour

2. Learn how to do http request by python's [request](https://requests.readthedocs.io/en/master/user/quickstart/) library

3. Formatting downloaded data by [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html), desired output example [BTC-USDT-1h.csv](./BTC_USDT_1h.csv)

### Optional

#### 1. Modularize your code

- [x] **write a class**  for CryptoCompare data api object and put your function into a member function.

#### 2. Add one more data endpoint

- [x] **write a member function**  for one more endpoint, e.x. [Toplist by Market Cap Full Data](https://min-api.cryptocompare.com/documentation?key=Toplists&cat=TopTotalMktCapEndpointFull). (feel free to choose another one) and put it as another member function.

### Work Log

#### 4/13
Wrote files `get_all_histo_price_json.py`, `data_json_to_csv.py`, `learn_rest_api.py`

Generated data file `btc_usd_hourly.json`, `btc_usd_hourly.csv`


#### 4/14
Studied samply file `ata_fetcher_cc_example.py`

Studied OOP, munipulate pandas DataFrame, unix timestamp

Wrote new file `histo_MCap_data_fetcher.py`. This file contains CryptoCompareAPI class and member functions to fetch history data and market cap data

Modularized code and used OOP. `class CryptoCompareAPI():`

Reimplemented function `def getHistoData(self, fsym, tsym, freq, e='CCCAGG', start_time=None, end_time=None, limit=None)` with start time and end time choice

Used pandas to pandas to load js directly

Wrote `def _setBaseUrl(self, fsym, tsym, freq, e)` to better use the base url. TODO: revisit this function to make it more general

Wrote function `def getTopListMCap(self, tsym, rank_from=None, rank_to=None, ascending=False, sign=False)` to fetch [Toplist by Market Cap Full Data](https://min-api.cryptocompare.com/documentation?key=Toplists&cat=TopTotalMktCapEndpointFull). This member function can fetch all coin's market cap, or certain ranks of coins if rank_from and rank_to is set. The results export to a csv file have similar layout as [CoinMarketCap](https://coinmarketcap.com) TODO: add descending/ascending function

Generated data file `BTC_USDT_1h_20170401_20200401.csv`, `all_coin_market_cap.csv`, `coin_market_cap_rank20_140.csv`, `coin_market_cap_top120.csv`