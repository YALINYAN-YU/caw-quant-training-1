import urllib.request
import urllib.parse
import urllib.error
import ssl
import json
import pandas as pd
from datetime import datetime

api_key = False
#api_key = 'f1ec848d3e1f70325fe15398cc707fb3e6aab5290ab22d6299924f26116bf367'
if api_key is False:
    api_key = 42
    serviceurl = 'https://min-api.cryptocompare.com/data/v2/histohour?'
else:
    serviceurl = 'https://min-api.cryptocompare.com/data/v2/histohour?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:

    '''
    fsym: string Required
    The cryptocurrency symbol of interest [ Min length - 1] [ Max length - 10]
    '''
    fsym = input('The cryptocurrency symbol of interest: ')
    if len(fsym) < 1 or len(fsym) > 10:
        break

    '''
    tsym: string Required
    The currency symbol to convert into [ Min length - 1] [ Max length - 10]
    '''
    tsym = input('The currency symbol to convert into: ')
    if len(tsym) < 1 or len(tsym) > 10:
        break

    limit = input('The number of data points to return (default - 168): ')

    parms = dict()
    parms['fsym'] = fsym
    parms['tsym'] = tsym
    parms['limit'] = limit

    if api_key is not False:
        parms['api_key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    js = json.loads(data)
    df = pd.DataFrame(columns=['close', 'high', 'low',
                               'open', 'volume', 'baseVolume', 'datetime'])

    for data in js['Data']['Data']:
        close_price = data['close']
        high_price = data['high']
        low_price = data['low']
        open_price = data['open']
        volume = data['volumefrom']
        base_volume = data['volumeto']
        timestamp = data['time']
        dt = datetime.fromtimestamp(timestamp)
        row = {'close': close_price, 'high': high_price, 'low': low_price,
               'open': open_price, 'volume': volume, 'baseVolume': base_volume, 'datetime': dt}
        df = df.append(row, ignore_index = True)


    df.to_csv('try.csv', index=False)

    #df = pd.read_json(json.dumps(js['Data']['Data'], indent=4))
    #df.to_csv('try.csv', index=None)





'''
toTs timestamp
Returns historical data before that timestamp. 
If you want to get all the available historical data, 
you can use limit=2000 and keep going back in time using the toTs param. 
You can then keep requesting batches using: 
&limit=2000&toTs={the earliest timestamp received}
'''