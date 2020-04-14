import pandas as pd
import json
from datetime import datetime


def extract_from_json_to_df(js_data, df):
    '''clean up json data and extract info to a panda dataframe

    Parameters
    ----------
    js_data: js, required
        Dictionary contains fsym, tsym, limit, api_key, toTs
    df: dataframe, required

    Returns
    -------
    dataframe
        a dataframe containing close, high, low, open, volumefrom, volumeto and time info
    '''
    for data in js_data:
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

    return df


if __name__ == '__main__':

    df = pd.DataFrame(columns=['close', 'high', 'low',
                               'open', 'volume', 'baseVolume', 'datetime'])

    json_file_name = 'btc_usd_hourly.json'
    csv_file_name = 'btc_usd_hourly.csv'

    # open json file and clean up data, extract info
    with open(json_file_name) as json_file:
        print ('Loaded Json file')
        js_data = json.load(json_file)
        df_to_output = extract_from_json_to_df(js_data, df)
        print ('Extracted Json data')

    # save to csv file
    with open(csv_file_name, 'w') as csv_file:
        print ('Writing to csv file')
        df_to_output.to_csv(csv_file, index=False)
        print ('csv file saved')

    