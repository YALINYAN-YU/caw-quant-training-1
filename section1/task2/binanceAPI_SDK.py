import os
import re
import math
import os.path
import time
import json
import pandas as pd

from binance.client import Client
from datetime import timedelta, datetime
from dateutil import parser

DATA_DRI = './data'

API_KEY = ''
API_SECRET = ''

# BINSIZES = {'m': 1, 'h': 60, 'd': 1440}
MAX_LIMIT = 500


class BinanceAPI():

    def __init__(self):
        self.client = Client(api_key=API_KEY, api_secret=API_SECRET)
        self._crate_data_folder()

    def _crate_data_folder(self):
        ''' Helper function to initiate data folder
        '''
        if not os.path.isdir(DATA_DRI):
            print('Create folder data to store')
            os.mkdir(DATA_DRI)

    def _returnFilePathAndDF(self, symbol, kline_size, start_time, end_time):
        ''' This function sets file path to output to and return existing data if exists

            :param symbol: Name of a trading pair, Required
            :type symbol: str
            :param kline_size: kline size, Required
            :type kline_size: str
            :param start_time: kline start date
            :type start_time: str in format %d %b %Y
            :param end_time: kline end date
            :type end_tiem: str in format %d %b %Y

            :return: filepath to export and data in pd.DataFrame format
        '''
        if start_time != None:
            start_time = start_time.upper()
        if end_time != None:
            end_time = end_time.upper()

        if start_time == None and end_time == None:
            filename = f'{symbol}-{kline_size}-data.csv'
        elif start_time != None and end_time == None:
            filename = f'{symbol}-{kline_size}-starts-at-{start_time}-data.csv'
        elif start_time == None and end_time != None:
            filename = f'{symbol}-{kline_size}-end-at-{end_time}-data.csv'
        elif start_time != None and end_time != None:
            filename = f'{symbol}-{kline_size}-from-{start_time}-to-{end_time}-data.csv'

        filepath = os.path.join(DATA_DRI, filename)

        if os.path.isfile(filepath):
            data_df = pd.read_csv(filepath)
        else:
            data_df = pd.DataFrame()

        return filepath, data_df

    def _getLastCurrentTime(self, symbol, kline_size, start_time, end_time, old_df):
        ''' Helper function to generate start time and end time to retrive data from client

            :param symbol: Name of a trading pair, Required
            :type symbol: str
            :param kline_size: kline size, Required
            :type kline_size: str
            :param start_time: kline start date
            :type start_time: str in format %d %b %Y
            :param end_time: kline end date
            :type end_tiem: str in format %d %b %Y
            :param old_df: already saved data file
            :type old_df: pd.DataFrame

            :return: earliest and current time to retrive data from
        '''
        if start_time == None and end_time == None:
            if len(old_df) > 0:
                last_saved_time = pd.to_datetime(old_df['timestamp'].iloc[-1])
            else:
                last_saved_time = datetime.strptime('1 Jan 2017', '%d %b %Y')
            current_time = pd.to_datetime(self.client.get_klines(
                symbol=symbol, interval=kline_size, limit=1)[0][0], unit='ms')
            return last_saved_time, current_time

        elif start_time != None and end_time == None:
            if len(old_df) > 0:
                last_saved_time = pd.to_datetime(old_df['timestamp'].iloc[-1])
            else:
                last_saved_time = datetime.strptime(start_time, '%d %b %Y')
            current_time = pd.to_datetime(self.client.get_klines(
                symbol=symbol, interval=kline_size, limit=1)[0][0], unit='ms')
            return last_saved_time, current_time

        elif start_time == None and end_time != None:
            last_saved_time = datetime.strptime('1 Jan 2017', '%d %b %Y')
            current_time = datetime.strptime(end_time, '%d %b %Y')
            return last_saved_time, current_time

        elif start_time != None and end_time != None:
            last_saved_time = datetime.strptime(start_time, '%d %b %Y')
            current_time = datetime.strptime(end_time, '%d %b %Y')
            return last_saved_time, current_time

        else:
            raise ValueError(
                f'start time {start_time} or end time {end_time} not valid')

    # def _get_binsize(self, kline_size):
        ''' Helper function for def _promptRetriveInfo(self, symbol, kline_size, start_time, end_time
            
            :param kline_size: kline size
            :type kline_size: str

            :return: total minutes of given kline size
        '''
        # agg = int(re.findall(r"\d+", kline_size)[0])
        # freq = re.findall(r"[a-z]", kline_size)[0]
        # return agg*BINSIZES[freq]

    def _promptRetriveInfo(self, symbol, kline_size, start_time, end_time):
        ''' This function prompts messages to terminal to indicate the process of retriving data
            TODO: implement this function
        '''
        # delta_min = (current_time - last_saved_time).total_seconds()/60
        # available_data = math.ceil(delta_min/self._get_binsize(kline_size))
        # if start_time == datetime.strptime('1 Jan 2017', '%d %b %Y'):
        #     print(
        #         f'Downloading {kline_size} data for {symbol} from {last_saved_time} to {current_time}. Be patient..!')
        # else:
        #     print(
        #         f'Downloading {delta_min} minutes of new data available for {symbol}, i.e. {available_data} instances of {kline_size} data.')
        return None

    def _retriveKlinesToDF(self, symbol, kline_size, start_time, end_time):
        ''' This function retrives data from binance and returns cleaned dataframe

            :param symbol: Name of a trading pair, Required
            :type symbol: str
            :param kline_size: kline size, Required
            :type kline_size: str
            :param start_time: kline start date
            :type start_time: str in format %d %b %Y
            :param end_time: kline end date
            :type end_tiem: str in format %d %b %Y

            :return: data in pd.DataFrame format
        '''
        klines = self.client.get_historical_klines(symbol, kline_size, start_time.strftime(
            "%d %b %Y %H:%M:%S"), end_time.strftime("%d %b %Y %H:%M:%S"))

        # data to DataFrame and clean up
        data = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close',
                                             'volume', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore'])
        data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')

        return data

    def getAllKlines(self, symbol, kline_size, start_time=None, end_time=None, save=False):
        ''' This function gets all kline data of a trading pair that set in specific kline size
            It will automatically search file in 'data' folder and update corresponding data

            :param symbol: Name of a trading pair, Required
            :type symbol: str
            :param kline_size: kline size, Required
            :type kline_size: str
            :param start_time: kline start date
            :type start_time: str in format %d %b %Y
            :param end_time: kline end date
            :type end_tiem: str in format %d %b %Y
            :param save: save data to csv file or not
            :type save: boolean

            :return: csv file saved in ./data folder and data in pd.DataFrame format
        '''
        symbol = symbol.upper()

        filepath, data_df = self._returnFilePathAndDF(
            symbol, kline_size, start_time, end_time)

        last_saved_time, current_time = self._getLastCurrentTime(
            symbol, kline_size, start_time, end_time, data_df)

        # TODO: implement prompt message function def _promptRetriveInfo(self, symbol, kline_size, start_time, end_time)
        # self._promptRetriveInfo(self, symbol, kline_size, start_time, end_time)

        data = self._retriveKlinesToDF(
            symbol, kline_size, last_saved_time, current_time)

        if len(data_df) > 0:
            temp_df = pd.DataFrame(data)
            data_df = data_df.append(temp_df)
        else:
            data_df = data

        data_df.set_index('timestamp', inplace=True)

        # save to csv
        if save:
            data_df.to_csv(filepath)
            print('Data saved')
        print('All caught up..!')

        return data_df

    def _retriveTradesFromId(self, symbol, id):
        ''' this function uses binance SDK to retrive historical trades from a given id #

            :param symbol: Name of a trading pair, Required
            :type symbol: str
            :param id: starting id to retrive data from
            :type id: int

            :return: retrived data in pd.DataFrame format
        '''
        trades_js = []
        most_recent_id = self.client.get_historical_trades(
            symbol=symbol, limit=1)[0]['id']
        while id < most_recent_id:
            trades = self.client.get_historical_trades(
                symbol=symbol, fromId=id)
            trades_js += trades
            id += MAX_LIMIT
            time.sleep(0.25)
        data = pd.DataFrame(trades_js, columns=[
                            'id', 'price', 'qty', 'quoteQty', 'time', 'isBuyerMaker', 'isBestMatch'])
        data['timestamp'] = pd.to_datetime(data['time'], unit='ms')
        data = data.drop(columns='time')
        return data

    def getAllTrades(self, symbol, save=False):
        ''' This function is suppose to get all historical trade data of a given symbol
            Due to long requesting time, I set the starting retriving id at 296280000

            TODO: give this function a starting time and end time to choose trade range, this data should be choosen from already save data file

            :param symbol: Name of a trading pair, Required
            :type symbol: str
            :param save: save data to csv file or not
            :type save: boolean

            :return: retrived data in pd.DataFrame format
        '''
        symbol = symbol.upper()
        filename = f'{symbol}-historical-trades-data.csv'
        filepath = os.path.join(DATA_DRI, filename)

        if os.path.isfile(filepath):
            print(f'{symbol} historical trades data fetched before')
            data_df = pd.read_csv(filepath)
        else:
            print(f'{symbol} historical trades data never fethed')
            data_df = pd.DataFrame()

        if len(data_df) > 0:
            last_id = data_df['id'].iloc[-1]+1
            print('update trades data to most current')
            data = self._retriveTradesFromId(symbol, last_id)
            data_df = data_df.append(data, ignore_index=True)
        else:
            # last_id = 0
            # this id is for testing purpose, should start with id 0
            last_id = 296280000
            print(
                f'retrive all historical trades data for {symbol} till current time')
            data = self._retriveTradesFromId(symbol, last_id)
            data_df = data

        if save:
            data_df.set_index('timestamp', inplace=True)
            data_df.to_csv(filepath)
            print(f'{symbol} historical trades up to date and saved')

        return data_df

    def getOrderBook(self, symbol, save=False):
        ''' This function retrives market depth from binane

            :param symbol: Required, trading pairs
            :type symbol: str

            :return: dataframe
        '''
        depth = self.client.get_order_book(symbol=symbol)
        bids = depth['bids']
        asks = depth['asks']

        bids_df = pd.DataFrame(bids, columns=['bid_price', 'bid_qty'])
        asks_df = pd.DataFrame(asks, columns=['ask_price', 'ask_qty'])
        df = pd.concat([bids_df, asks_df], axis=1)

        if save:
            filename = f'{symbol}-order-book.csv'
            filepath = os.path.join(DATA_DRI, filename)
            df.to_csv(filepath, index=False)
            print(f'{symbol} order book saved')
        return df

    def testOrder(self, symbol='BTCUSDT',
                  side='BUY',
                  type='LIMIT',
                  timeInForce="GTC",
                  quantity=100,
                  price='7125'):
        '''
            :param symbol: required
            :type symbol: str
            :param side: required
            :type side: str
            :param t: required
            :type t: str
            :param timeInForce: required if limit order
            :type timeInForce: str
            :param quantity: required
            :type quantity: decimal
            :param price: required
            :type price: str
            :param newClientOrderId: A unique id for the order. Automatically generated if not sent.
            :type newClientOrderId: str
            :param icebergQty: Used with iceberg orders
            :type icebergQty: decimal
            :param newOrderRespType: Set the response JSON. ACK, RESULT, or FULL; default: RESULT.
            :type newOrderRespType: str
            :param recvWindow: The number of milliseconds the request is valid for
            :type recvWindow: int

            :returns: API response
        '''
        # self._adjustTime()
        resp = self.client.create_test_order(
            symbol=symbol, side=side, type=type, timeInForce=timeInForce, quantity=quantity, price=price)

        if resp == {}:
            print('test order success')
        else:
            print('test order failed')
        return resp


def pretty_json(js):
    return json.dumps(js, indent=4)

def make_pd(js):
    return pd.DataFrame(js)

if __name__ == '__main__':
    # client = Client(API_KEY, API_SECRET)
    # Return list of products currently listed on Binance
    # products = client.get_products()['data']
    # df = make_pd(products)
    # df.to_csv(os.path.join(DATA_DRI, 'products_listed.csv'))

    # Return rate limits and list of symbols
    # exchange_info = client.get_exchange_info()
    # print(pretty_json(exchange_info))

    # Return info about a symbol
    # symbol = client.get_symbol_info('ETHBTC')
    # print(pretty_json(symbol))

    b_api = BinanceAPI()
    # b_api.getAllKlines('BTCUSDT', '1h', start_time='1 Apr 2019', save=True)
    # b_api.getAllKlines('BTCUSDT', '1h', end_time='5 may 2018', save=True)
    # b_api.getAllKlines('BTCUSDT', '1h', save=True)
    # b_api.getAllKlines('BTCUSDT', '1h', start_time='1 apr 2019', end_time='1 apr 2020', save=True)

    # b_api.getAllTrades('BTCUSDT', save=True)

    # b_api.getOrderBook('BTCUSDT', save=True))

    b_api.testOrder()
