# import json

# def getImageUrl(json):
#     '''
#     Returns URL of NFT image from JSON
#     '''

#     pass
    # json = getJSON(contract_address, token_id)
    # try:
    #     for key in json.keys():
    #         if 'image' in key:
    #             return json[key]
    # except:
    # # If not found, print json.keys()
    #     print(json.keys())

    
# import web3

# def fetchABI(contract_address):
#     '''
#     Retrieves ABI based on contract
#     '''
#     print("Fetching contract ABI")
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


    # print("Getting NFT metadata")
    # INFURA_URL = 'https://mainnet.infura.io/v3/63c3c9dcf79441d0916d436ff98a9040'
    # w3 = web3.Web3(web3.HTTPProvider(INFURA_URL))

    # try:
    #     abi = fetchABI(contract_address)
    #     contract_address = web3.Web3.toChecksumAddress(contract_address)
    #     contract = w3.eth.contract(address=contract_address, abi=abi)
    #     print(f"Contract {contract}")

        # ERC-721
        # url = contract.functions.tokenURI(token_id).call()
        
        # ERC-1155
        # url = contract.functions.uri(token_id).call()

        # print(url)

        # if 'ipfs://' in url:
        #     return json.loads(requests.get('https://ipfs.io/ipfs/' + url.split("//")[1]).text)
        
        # elif 'https' in url:
        #     return json.loads(requests.get(url).text)
        
        # else:
        #     print(f"New Type? {url}")
        #     print("Did not return metadata")
            
    # except Exception as e:
    #     print(e)

    # Information to send back to page
        # metadata = "Picture" # output can be a string
        # duplicates = "" # duplicate can be a string
        # image_url = ""

    #     if token_id:
    #         try:    
    #             image_metadata = getOpenseaMetadata(contract_address, token_id)
    #             image_url = image_metadata['image']
                
    #             # NFT Metadata
    #             metadata = json.dumps(image_metadata, indent=4, sort_keys=True)
    #             print(metadata)

    #         # If anything goes wrong
    #         except Exception as e:
    #             print(e)
    #             metadata = "[Error] Invalid NFT"
    #     else:
    #         return render_template("index.html")

    #     # Image duplicate search
    #     duplicates = findDuplicates(image_url)

    #     return render_template("index.html", metadata=metadata, image=image_url, duplicate=duplicates)

    # elif request.method == "GET":
    #     return render_template("index.html")

# def main():
    
#     logging.getLogger().setLevel(logging.INFO)

#     original = "https://raw.githubusercontent.com/andrebhu/TreeHacks2022/main/src/images/original.jpg"
#     # fake = "https://raw.githubusercontent.com/andrebhu/TreeHacks2022/main/src/images/monkey.jpg"
#     fake ="https://lh3.googleusercontent.com/9l0UICNfBK-bBfZ8EGbJPPC9L5MFGeJApN6IcxuKMfE4fPntsIYCE-dmZkAhJvk7kFcjUJbYY6znSS_c4t_Og59bwTpng4roMV8Vx1Y=s0"
#     n_found = duplicates(fake)
    
#     if n_found==0:
#         logging.info("Image is original.")
#     else:
#         logging.info(f"Image has {n_found} duplicates online.")

# if __name__ == "__main__":
#     main()
