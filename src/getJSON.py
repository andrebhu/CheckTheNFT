import requests
import json
import web3

def fetchABI(contract_address):
    # Exports contract ABI in JSON

    url = "https://api.etherscan.io/api"

    params = {
        "module": "contract",
        "action": "getabi",
        "address": contract_address,
        "apikey": "GTU9P9K5741Y761585SRRY38NP8I1YMC8M"
    }

    response = requests.get(url, data=params)
    response_json = response.json()
    abi_json = json.loads(response_json['result'])
    
    return abi_json


def getJSON(contract_address, token_id):
    INFURA_URL = 'https://mainnet.infura.io/v3/63c3c9dcf79441d0916d436ff98a9040'
    w3 = web3.Web3(web3.HTTPProvider(INFURA_URL))

    try:
        abi = fetchABI(contract_address)
        contract = w3.eth.contract(address=contract_address, abi=abi)
        url = contract.functions.tokenURI(token_id).call()

        if 'ipfs://' in url:
            return json.loads(requests.get('htttps://ipfs.io/ipfs/' + url.split("//")[1]).text)
        
        elif 'https' in url:
            return json.loads(requests.get(url).text)
        
        else:
            print(f"New Type? {url}")
            

    except Exception as e:
        print(e)


# TESTING
# print(getJSON('0x1b79c7832ed9358E024F9e46E9c8b6f56633691B', 51))