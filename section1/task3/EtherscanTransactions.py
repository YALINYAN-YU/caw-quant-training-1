from etherscan.transactions import Transactions
from EtherscanAPI import EtherscanAPI

import os
import json

DATA_DIR = './TransactionsData'
api = EtherscanAPI()
API_KEY = api.key
api._create_data_folder(DATA_DIR)

if __name__=='__main__':
    test_hash = '0x15f8e5ea1079d9a0bb04a4c58ae5fe7654b5b2b4463375ff7ffb490aa0032f3a'
    api = Transactions(api_key=API_KEY)
    status = api.get_status(tx_hash=test_hash)
    print(status)

    receipt_status = api.get_tx_receipt_status(tx_hash=test_hash)
    print(receipt_status)   
    