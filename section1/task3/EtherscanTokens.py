from etherscan.tokens import Tokens
from EtherscanAPI import EtherscanAPI

import os
import json

DATA_DIR = './TokenData'
api = EtherscanAPI()
API_KEY = api.key
api._create_data_folder(DATA_DIR)

if __name__=='__main__':
    test_address = '0xe04f27eb70e025b78871a2ad7eabe85e61212761'
    test_contract_address = '0x57d90b64a1a57749b0f932f1a3395792e12e7055'

    api = Tokens(contract_address=test_contract_address, api_key=API_KEY)
    balance = api.get_token_balance(address=test_address)
    print(balance)

    api = Tokens(contract_address=test_contract_address, api_key=API_KEY)
    supply = api.get_total_supply()
    print(supply)