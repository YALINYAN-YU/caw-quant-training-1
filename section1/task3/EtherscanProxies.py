from EtherscanAPI import EtherscanAPI
from etherscan.proxies import Proxies

import pandas as pd
import json
import os

DATA_DIR = './ProxiesData'

class Proxy(EtherscanAPI):
    def __init__(self):
        super().__init__()
        self.api = Proxies(api_key=self.key)
        self._create_data_folder(DATA_DIR)

    
    # def gas_price(self):
    #     price = self.api.gas_price()
    #     return price

    def _save_json(self, data, filename, save):
        if save:
            filepath = os.path.join(DATA_DIR, filename)
            with open(filepath, 'w') as json_file:
                json.dump(data, json_file, indent=4)

    def get_most_recent_block(self, save=False):
        block = self.api.get_most_recent_block()
        filename = f'most-recent-block.json'
        self._save_json(block, filename, save)
        return block

    def get_block_by_number(self, block_num, save=False):
        block = self.api.get_block_by_number(block_num)
        filename = f'block-{block_num}-data.json'
        self._save_json(block, filename, save)
        return block

    def get_uncle_by_blocknumber_index(self, block_num, index, save=False):
        uncles = self.api.get_uncle_by_blocknumber_index(block_number=block_num, index=index)
        filename = f'block-{block_num}-{index}-uncles-data.json'
        self._save_json(uncles, filename, save)
        return uncles

    def get_block_transaction_count_by_number(self, block_num, save=False):
        tx_count = self.api.get_block_transaction_count_by_number(block_number=block_num)
        return int(tx_count, 16)

    def get_transaction_by_hash(self, tx_hash, save=False):
        transaction = self.api.get_transaction_by_hash(tx_hash=tx_hash)
        filename = f'transaction-data-of-hash-{tx_hash}.json'
        self._save_json(transaction, filename, save)
        return transaction

    def get_transaction_by_blocknumber_index(self, block_num, index, save=False):
        transaction = self.api.get_transaction_by_blocknumber_index(block_number=block_num,
                                                       index=index)
        filename = f'transaction-data-of-block-{block_num}.json'
        self._save_json(transaction, filename, save)
        return transaction

    def get_transaction_count(self, address, save=False):
        count = self.api.get_transaction_count(address)
        return int(count, 16)

    def get_transaction_receipt(self, tx_hash, save=False):
        receipt = self.api.get_transaction_receipt(tx_hash)
        filename = f'transaction-recepit-of-hash-{tx_hash}.json'
        self._save_json(receipt, filename, save)
        return receipt

    # def get_code(self, address: str):
    #     code = self.api.get_code(address)
    #     return code

    # def get_storage_at(self, address, position):
    #     value = self.api.get_storage_at(address, position)
    #     return value


if __name__=='__main__':
    proxies = Proxy()
    test_address = '0x6E2446aCfcec11CC4a60f36aFA061a9ba81aF7e0'
    test_block = '0x57b2cc'
    test_index = '0x0'
    test_block_num = 5747732
    test_hash = '0x1e2910a262b1008d0616a0beb24c1a491d78771baa54a33e66065e03b1f46bc1'
    proxies.get_most_recent_block(save=True)
    proxies.get_block_by_number(test_block_num, save=True)
    proxies.get_uncle_by_blocknumber_index(test_block, test_index, save=True)
    print(proxies.get_block_transaction_count_by_number(test_block))
    proxies.get_transaction_by_hash(test_hash, save=True)
    proxies.get_transaction_by_blocknumber_index(test_block,test_index, save=True)
    print(proxies.get_transaction_count(test_address))
    proxies.get_transaction_receipt(test_hash, save=True)


