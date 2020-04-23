import os
import json
import requests
from etherscan.accounts import Account

from etherscan.client import Client, ConnectionRefused, BadRequest, EmptyResponse


class NewClient(Client):

    def connect(self):
        # TODO: deal with "unknown exception" error
        try:
            req = self.http.get(self.url)
        except requests.exceptions.ConnectionError:
            raise ConnectionRefused

        if req.status_code == 200:
            # Check for empty response
            if req.text:
                data = req.json()
                status = data.get('status')
                if status == '1' or self.check_keys_api(data):
                    return data
                else:
                    return data
                    # raise EmptyResponse(data.get('message', 'no message'))
        raise BadRequest(
            "Problem with connection, status code: %s" % req.status_code)





class EtherscanAPI():

    def __init__(self):
        with open('../../../api-keys/Etherscan-API-Key.json', mode='r') as key_file:
            self.key = json.loads(key_file.read())['key']
        Client.connect = NewClient.connect

    def _create_data_folder(self, DATA_DIR):
        if not os.path.isdir(DATA_DIR):
            print('Create data folder to store')
            os.mkdir(DATA_DIR)



