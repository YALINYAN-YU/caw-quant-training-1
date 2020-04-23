from etherscan.contracts import Contract
from EtherscanAPI import EtherscanAPI

import os
import json

DATA_DIR = './ContractData'
api = EtherscanAPI()
API_KEY = api.key
api._create_data_folder(DATA_DIR)

def save_json(data, filename, save):
    if save:
        filepath = os.path.join(DATA_DIR, filename)
        with open(filepath, 'w') as json_file:
            json.dump(data, json_file, indent=4)

def save_sol(data, filename, save):
    if save:
        filepath = os.path.join(DATA_DIR, filename)
        with open(filepath, 'w') as sol_file:
            sol_file.write(data)

if __name__=='__main__':
    test_address = '0xfb6916095ca1df60bb79ce92ce3ea74c37c5d359'

    contract = Contract(address=test_address, api_key=API_KEY)
    abi = contract.get_abi()
    js = json.loads(abi)
    abi_filename = f'abi-address-{test_address}.json'
    save_json(js, abi_filename, save=True)

    sourcecode = contract.get_sourcecode()
    sourcecode_filename = f'contract-sourcecode-address-{test_address}.sol'
    save_sol(sourcecode[0]['SourceCode'], sourcecode_filename, save=True)


    