import urllib.request
import urllib.parse
import urllib.error
import ssl
import json
import pandas as pd
from datetime import datetime

FIRST_BTC_TRADE_TIMESTAMP = 1274400000

def date_to_timestamp(date):
    date

def get_service_url(timeframe):
    '''return correct service url based on timeframe set

    Parameters
    ----------
    timeframe : str
        indicate daily, hourly or minute

    Raise
    -----
    ValueError

    Returns
    -------
    str
        a string of corresponding service url from cryptoCompare.com
    '''

    if timeframe == 'daily':
        return 'https://min-api.cryptocompare.com/data/v2/histoday?'
    elif timeframe == 'hourly':
        return 'https://min-api.cryptocompare.com/data/v2/histohour?'
    elif timeframe == 'minute':
        return 'https://min-api.cryptocompare.com/data/v2/histominute?'
    else:
        raise ValueError('timeframe must be set as daily or hourly or minute')


def set_url_parameter(url_parms):
    '''set parameters for service url

    Parameters
    ----------
    url_parms : dict, required
        Dictionary contains fsym, tsym, limit, api_key, toTs
        fsym : str, required
            The cryptocurrency symbol of interest
        tsym: str, required
            The currency symbol to convert into
        limit: int
            The number of data points to return [ Min - 1] [ Max - 2000]
        api_key: str
        toTs: timestamp

    Returns
    -------
    str
        a string of parameter to add behind service url
    '''
    parms = dict()
    parms['fsym'] = url_parms['fsym']
    parms['tsym'] = url_parms['tsym']
    parms['limit'] = url_parms['limit']
    if url_parms['toTs'] != -1:
        parms['toTs'] = url_parms['toTs']
    if url_parms['e'] != None:
        parms['e'] = url_parms['e']
    if url_parms['api_key'] is not False:
        parms['api_key'] = url_parms['api_key']
    return(urllib.parse.urlencode(parms))


def get_data(url_parms, serviceurl, ctx, earliest_timestamp):
    '''open url with parameters and earliest time stamp of your choice

    Parameters
    ----------
    url_parms : dict, required
        Dictionary contains fsym, tsym, limit, api_key, toTs
    serviceurl: str, required
        base url from cryptoCompare.com
    ctx: ssl object
    earliest_timestamp:
        set the timestamp to start retriving data from

    Returns
    -------
    str or None
        if earliest timestamp go beyond the first trade date, return None
        else return data retrived (string format)
    '''
    if earliest_timestamp < FIRST_BTC_TRADE_TIMESTAMP:
        return None
    else:
        url_parms['toTs'] = earliest_timestamp
        url = serviceurl + set_url_parameter(url_parms)
        print('Retrieving', url)
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')
        return data
   


if __name__ == "__main__":
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    api_key = 'f1ec848d3e1f70325fe15398cc707fb3e6aab5290ab22d6299924f26116bf367'

    serviceurl = get_service_url('hourly')

    # TODO: make url_parms as a function
    url_parms = {'fsym': 'btc', 'tsym': 'usd',
                 'limit': 2000, 'api_key': api_key}
    
    earliest_timestamp = int(datetime.timestamp(datetime.now()))
    all_js_data = []
    data = ''

    # start to retrieve all history data
    while True:
        data = get_data(url_parms, serviceurl, ctx, earliest_timestamp)
        if data is None:
            break
        else:
            js = json.loads(data)
            earliest_timestamp = js['Data']['TimeFrom']-1
            all_js_data = js['Data']['Data'] + all_js_data

    # output data to a json file
    with open('btc_usd_hourly.json', 'w') as json_file:
        json.dump(all_js_data, json_file, indent=4)


