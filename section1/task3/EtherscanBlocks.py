from etherscan.blocks import Blocks
from EtherscanAPI import EtherscanAPI

DATA_DIR = './BlocksData'

class Block(EtherscanAPI):

    def __init__(self):
        super().__init__()
        self.api = Blocks(api_key=self.key)
        self._create_data_folder(DATA_DIR)


    def get_block_reward(self, block):
        reward = self.api.get_block_reward(block)
        return reward


if __name__ == '__main__':
    blocks = Block()
    print(blocks.get_block_reward(2165403))