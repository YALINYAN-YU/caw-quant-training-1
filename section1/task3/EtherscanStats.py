from etherscan.stats import Stats
from EtherscanAPI import EtherscanAPI

import os
import json

DATA_DIR = './StatsData'
api = EtherscanAPI()
API_KEY = api.key
api._create_data_folder(DATA_DIR)


def save_json(data, filename, save):
    if save:
        filepath = os.path.join(DATA_DIR, filename)
        with open(filepath, 'w') as json_file:
            json.dump(data, json_file, indent=4)

if __name__=='__main__':
    # test_address = '0xfb6916095ca1df60bb79ce92ce3ea74c37c5d359'

    api = Stats(api_key=API_KEY)
    last_price = api.get_ether_last_price()
    filename = f'last_price.json'
    save_json(last_price, filename, save=True)
    print(last_price)

    supply = api.get_total_ether_supply()
    print(supply)
    

    