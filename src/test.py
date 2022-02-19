import requests
import json
def fetchABI(contract_address):
    '''
    Retrieves ABI based on contract
    '''
    print("Fetching contract ABI")
    url = "https://api.etherscan.io/api"

    params = {
        "module": "contract",
        "action": "getabi",
        "address": contract_address,
        "apikey": "GTU9P9K5741Y761585SRRY38NP8I1YMC8M"
    }

    response = requests.get(url, data=params)


    response_json = response.json()
    print(response_json)
    print(response_json['status'])
    print(type(response_json['status']))
    # abi_json = json.loads(response_json['result'])
    
    # return abi_json

fetchABI('0x552d72f86f04098a4eaeda6d7b665ac12f846ad2')