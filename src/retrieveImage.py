import requests
import json
import web3


def fetchABI(contract_address):
    # Exports contract ABI in JSON

    url = "https://api.etherscan.io/api"
#    ?module=contract
#    &action=getabi
#    &address=0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413
#    &apikey=YourApiKeyToken"

    params = {
        "module": "contract",
        "action": "getabi",
        "address": contract_address,
        "apikey": "GTU9P9K5741Y761585SRRY38NP8I1YMC8M"
    }

    response = requests.get(url, data=params)
    response_json = response.json()
    abi_json = json.loads(response_json['result'])
    # result = json.dumps({"abi":abi_json}, indent=4, sort_keys=True)
    # print(result)
    return abi_json

def retrieveImage(contract_address, token_id):
    INFURA_URL = 'https://mainnet.infura.io/v3/63c3c9dcf79441d0916d436ff98a9040'
    w3 = web3.Web3(web3.HTTPProvider(INFURA_URL))
    
    # https://ethereum.stackexchange.com/questions/15603/web3-js-get-contract-abi-knowing-only-contract-address
    try:
        abi = fetchABI(contract_address)
        contract = w3.eth.contract(address=contract_address, abi=abi)
        print(contract.functions.tokenURI(token_id).call())
    except:
        print("Bad token :(")


    



retrieveImage('0x1b79c7832ed9358E024F9e46E9c8b6f56633691B', 51)
retrieveImage('0x5c3Cc8D8f5C2186d07D0bd9E5b463Dca507b1708', 4599)
# retrieveImage('0x5c1a0cc6dadf4d0fb31425461df35ba80fcbc110', 3778)
