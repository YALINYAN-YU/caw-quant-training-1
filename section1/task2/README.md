# Task2 Get market data from Binance

In task1, you learned how to download data from data sources like [CryptoCompare](https://www.cryptocompare.com/). While CryptoCompare is free with good data quality, sometimes you do need to get market data directly from crypto-exchanges, especially when you're trading.

This task will guide you to get data from [Binance](https://www.binance.com/en), one of the top crypto-exchanges.

## 1. Explore Binance Data API

[Binance API Documentation](https://binance-docs.github.io/apidocs/spot/en/#change-log)

[Binance Github Homepage](https://github.com/binance-exchange)

[Binance REST/WebSocket endpoints](https://github.com/binance-exchange/binance-official-api-docs)

[Binance Python SDK](https://github.com/binance-exchange/python-binance)

Binance provides two market categories: **Spot Market** and **Future Market**(you will be focusing on spot market), two data types: **Public Data** and **Private Data**.(public data is open to anyone with some constraints associated, while private data contains information like account balance, trade history, which requires you to have an account in Binance to access)

### Required

#### 1. **Use Binance Python SDK** to get public data

The worst case is, you don't have SDK(Software Development Kit) for the language you use, and have to deal with http request like what you did in task1. Fortunately, we have one this time. Using SDK will save you a lot of work since it has already done those tedious work for you.

**Write a script (.py file)**

- [x] get candle data(aka kline, histo)
- [x] get transactions(aka trades)
- [x] get market depth(aka orderbook)

Format the data the way you like using pandas, save them seperately as csv.

Hint:

1. check its sdk repo: https://github.com/binance-exchange/python-binance, take a look at examples and source codes (client.py), you might find something similar to what you've done in task1(if you did the optional task). Find the specific endpoint you need.

2. Note that you don't need a api key to get public data.

### Optional

#### 1. Trade in Binance by its python SDK

- [x] setup a binance account
- [x] setup its trading api(you need to create a api key, api secret pair to trade)
- [x] check python SDK, create a test order.

Note:

1. You don't need to have money in your account to create a test order.
2. Of course, You can put some money in it and create a real order, starting your life as a quantitative trader.


### Work Log

#### 4/15

Studied Binance API documentation Spot/Margin/Lending page, set up Binance account and got API key & API secret. Took a look at the Postman APP.

Wrote `binanceAPI.py` file to play with API calls with out using Binance SDK. Didn't finished playing with it.

TODO: write member function in `binanceAPI.py` to get histo/trades/orderbook with out using SDK as practice. Will use [Source code for binance.client](https://python-binance.readthedocs.io/en/latest/_modules/binance/client.html#Client.get_exchange_info) as a reference.

Took a look at SDK and tried making calls using SDK, successed. Found this [tutorial page](https://sammchardy.github.io/binance/2018/01/08/historical-data-download-binance.html) very helpful. Studied functions `def interval_to_milliseconds(interval)`, `def date_to_milliseconds(date_str)`

TODO: write get histo/trades/orderbook functions with python-binance SDK.

Today was slow on Task 2 since I had to help out my Dad. Will work more on 4/16

#### 4/16

Tested API using Postman APP, very helpful for me to understand the data.

Found this [retriving Binance post](https://medium.com/swlh/retrieving-full-historical-data-for-every-cryptocurrency-on-binance-bitmex-using-the-python-apis-27b47fd8137f) very useful, rewrote function `get_all_klines` in file `binanceAPI_SDK.py`

confused about the format used in this `datetime.strptime('1 Jan 2017', '%d %b %Y')`, need to dig in to understand the format of datetime

note: when do `pd.reac_csv`, previous index set won't be effective. It will reasign numbers as indexes

Today was also slow on Task 2.

Generated data file `products_listed.csv`

#### 4/17

studied `strptime()` function and corresponding datetime format. Reference [here](https://www.journaldev.com/23365/python-string-to-datetime-strptime#python-strptime)

Rewrote member function `get_all_klines` to `def getAllKlines`, refactored and added helper functions: `def _retriveKlinesToDF`, `def _promptRetriveInfo`, `def _getLastCurrentTime`, `def _returnFilePathAndDF`. Function `def getAllKlines` will retrive all historical kline data if no time range set. It will search for corresponding data file and update data.

TODO: finish the prompt message function

Wrote member function `def getAllTrades` to get all transaction data. This will retrive data from Binance and update existing data file.

Unfortunately, it would take a long time to retrive all historical trades. I set an id for testing purpose.

TODO: add time range selection for above function

Wrote member function `def getOrderBook` to get order book data.

Wrote member function `def testOrder` to run a test order.

NOTE: When testing order, I encountered error `binance.exceptions.BinanceAPIException: APIError(code=-1021): Timestamp for this request is outside of the recvWindow.` After searching online, I found out the reason was that my computer's internet time is lagging. I solved above problem by rescyn my computer internet time. Used command line code: `sudo sntp -sS time.apple.com`. [reference](https://stackoverflow.com/questions/52548093/ntpdate-command-not-found-in-macos-mojave)

Used [Market Data Endpoints](https://python-binance.readthedocs.io/en/latest/market_data.html) as a reference when implementing above functions

Generated data files: `BTCUSDT-1h-data.csv`, `BTCUSDT-1h-end-at-5 MAY 2018-data.csv`, `BTCUSDT-1h-from-1 APR 2019-to-1 APR 2020-data.csv`, `BTCUSDT-1h-starts-at-1 APR 2019-data.csv`, `BTCUSDT-historical-trades-data.csv`, `BTCUSDT-order-book.csv`

Finished Task 2