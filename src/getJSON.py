import requests
import json

def getJSON(contract_address:str, token_id:int):
    '''
    Retrieves opensea metadata about the NFT
    '''    
    token_id = str(hex(token_id))
    r = requests.get(f"https://api.opensea.io/api/v1/metadata/{contract_address}/{token_id}?format=json")
    return json.loads(r.text)