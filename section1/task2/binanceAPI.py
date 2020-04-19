import os
import requests
import json
import time
import dateparser
import pytz

import pandas as pd
import numpy as np 

from datetime import datetime
from binance.client import Client


API_KEY = ""
API_SECRET = ""
# client = Client(API_KEY, API_SECRET, {"verify": False, "timeout": 20})
# print(client.get_exchange_info())


# def date_to_milliseconds(date_str):
#     """Convert UTC date to milliseconds
#     If using offset strings add "UTC" to date string e.g. "now UTC", "11 hours ago UTC"
#     See dateparse docs for formats http://dateparser.readthedocs.io/en/latest/
#     :param date_str: date in readable format, i.e. "January 01, 2018", "11 hours ago UTC", "now UTC"
#     :type date_str: str
#     """
#     # get epoch value in UTC
#     epoch = datetime.utcfromtimestamp(0).replace(tzinfo=pytz.utc)
#     # parse our date string
#     d = dateparser.parse(date_str)
#     # if the date is not timezone aware apply UTC timezone
#     if d.tzinfo is None or d.tzinfo.utcoffset(d) is None:
#         d = d.replace(tzinfo=pytz.utc)

#     # return the difference in time
#     return int((d - epoch).total_seconds() * 1000.0)


# def interval_to_milliseconds(interval):
#     """Convert a Binance interval string to milliseconds
#     :param interval: Binance interval string 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w
#     :type interval: str
#     :return:
#          None if unit not one of m, h, d or w
#          None if string not in correct format
#          int value of interval in milliseconds
#     """
#     ms = None
#     seconds_per_unit = {
#         "m": 60,
#         "h": 60 * 60,
#         "d": 24 * 60 * 60,
#         "w": 7 * 24 * 60 * 60
#     }

#     unit = interval[-1]
#     if unit in seconds_per_unit:
#         try:
#             ms = int(interval[:-1]) * seconds_per_unit[unit] * 1000
#         except ValueError:
#             pass
#     return ms



class BinanceAPI():
    
    def __init__(self):
        self.base_endpoint = 'https://api.binance.com'


    def _safeRequest(self, url):
        while True:
            try:
                response = requests.get(url)
            except Exception as e:
                print(f'Connection Failed: {e}. Reconnecting...')
                time.sleep(1)
            else:
                break
        resp = response.json()
        if response.status_code != 200:
            raise Exception(resp)
        return resp


    def test(self, url):
        query_url = self.base_endpoint + url
        return self._safeRequest(query_url)


if __name__ == '__main__':
    b_api = BinanceAPI()
    js = b_api.test('/api/v3/exchangeInfo')
    print(js)

