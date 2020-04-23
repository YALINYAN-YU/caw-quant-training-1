import pandas as pd
import json
import os

from etherscan.accounts import Account
from EtherscanAPI import EtherscanAPI

DATA_DIR = './AccountData'

class Accounts(EtherscanAPI):
    
    def __init__(self, address):
        super().__init__()
        self.address = address
        self.api = Account(address=address, api_key=self.key)
        self._create_data_folder(DATA_DIR)
    
    def _data_to_df_save(self, data, filename, save=False):
        df = pd.DataFrame(data)
        df['timeStamp'] = pd.to_datetime(df['timeStamp'], unit='s')
        df.set_index('timeStamp', inplace=True)

        if save:
            filepath = os.path.join(DATA_DIR, filename)
            df.to_csv(filepath)
            print ('Data file saved')
        return df
        
    def get_balance(self):
        balance = self.api.get_balance()
        return balance

    def get_balance_multi(self):
        balances = self.api.get_balance_multiple()
        return balances

    def get_block_mined(self, page=1,
                        offset=10000, blocktype='blocks', save=False):
        block = self.api.get_blocks_mined_page(
            page=page, offset=offset, blocktype=blocktype)

        filename = f'{self.address}-page{page}-offset{offset}-blocks-mined.csv'
        blocks_df = self._data_to_df_save(block, filename, save=save)
        return blocks_df

    def get_all_blocks_mined(self, offset=10000, blocktype='blocks', save=False):
        blocks = self.api.get_all_blocks_mined(
            offset=offset, blocktype=blocktype)

        filename = f'{self.address}-all-blocks-mined.csv'
        blocks_df = self._data_to_df_save(blocks, filename, save=save)
        return blocks_df

    def get_all_transactions(self, offset=1000, sort='acs', internal=False, save=False):
        transactions = self.api.get_all_transactions(
            offset=offset, sort=sort, internal=internal)

        filename = f'{self.address}-all-transactions.csv'
        transac_df = self._data_to_df_save(transactions, filename, save=save)
        return transac_df

    def get_transaction_page(self, page=1, offset=10000, sort='asc',
                             internal=False, erc20=False, save=True):
        transactions = self.api.get_transaction_page(
            page=page, offset=offset, sort=sort, internal=internal, erc20=erc20)
        transac_df = pd.DataFrame(transactions)
        transac_df['timeStamp'] = pd.to_datetime(transac_df['timeStamp'], unit='s')
        transac_df.set_index('timeStamp', inplace=True)

        filename = f'{self.address}-page{page}-offset{offset}-transactions.csv'
        transac_df = self._data_to_df_save(transactions, filename, save=save)
        return transac_df

if __name__ == '__main__':
    address = '0x9dd134d14d1e65f84b706d6f205cd5b1cd03a46b'
    address_multi = ['0x49edf201c1e139282643d5e7c6fb0c7219ad1db7',
                     '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a']
    account = Accounts(address)
    account.get_block_mined(save=True)
    account.get_all_blocks_mined(save=True)
    account.get_balance()
    account.get_balance_multi()
    account.get_transaction_page(save=True)
    account.get_all_transactions(save=True)

