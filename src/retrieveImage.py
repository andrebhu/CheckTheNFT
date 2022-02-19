from base64 import b64encode
import requests
import json
import web3
import re
from getJSON import getJSON

# def fetchABI(contract_address):
#     # Exports contract ABI in JSON

#     url = "https://api.etherscan.io/api"

#     params = {
#         "module": "contract",
#         "action": "getabi",
#         "address": contract_address,
#         "apikey": "GTU9P9K5741Y761585SRRY38NP8I1YMC8M"
#     }

#     response = requests.get(url, data=params)
#     response_json = response.json()
#     abi_json = json.loads(response_json['result'])
    
#     return abi_json

def getImageUrl(contract_address, token_id):
    '''
    Returns URL of NFT image
    '''
    json = getJSON(contract_address, token_id)
    for key in json.keys():
        if 'image' in key:
            return json[key]

    # INFURA_URL = 'https://mainnet.infura.io/v3/63c3c9dcf79441d0916d436ff98a9040'
    # w3 = web3.Web3(web3.HTTPProvider(INFURA_URL))
    
    # https://ethereum.stackexchange.com/questions/15603/web3-js-get-contract-abi-knowing-only-contract-address
    # try:
    #     abi = fetchABI(contract_address)
    #     contract = w3.eth.contract(address=contract_address, abi=abi)
    #     url = contract.functions.tokenURI(token_id).call()

    #     if 'ipfs://' in url:
    #         data = json.loads(requests.get('https://ipfs.io/ipfs/' + url.split("//")[1]).text)
    #         # print(data.keys())
    #         for key in data.keys():
    #             if 'image' in key:
    #                 return data[key]
            
    #     elif 'https' in url:
    #         data = json.loads(requests.get(url).text)
    #         for key in data.keys():
    #             if 'image' in key:
    #                 return data[key]


    # except Exception as e:
    # print("Bad token format, we only support 721 atm")

def retrieveImage(contract_address, token_id):
    '''
    Given a contract_address and tokenId, return image encoded in base64
    '''
    image_url = getImageUrl(contract_address, token_id)
    
    print(f"Getting image from {image_url}")

    image_file = requests.get(image_url).content
    return b64encode(image_file).decode("utf-8")
    

# print(retrieveImage('0x1b79c7832ed9358E024F9e46E9c8b6f56633691B', 51)[:50])
# retrieveImage('0x5c3Cc8D8f5C2186d07D0bd9E5b463Dca507b1708', 4599)
# retrieveImage('0x5c1a0cc6dadf4d0fb31425461df35ba80fcbc110', 3778)

