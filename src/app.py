#!/usr/bin/env python

from base64 import b64encode
from flask import Flask, render_template, request, flash
import requests
import json

from check_image_exists_online import duplicates

app = Flask(__name__)

app.config['SECRET_KEY'] = b'\xa7\xd8\x89JB\xa9sj\x05\x03S\x1a\x83\xb3\x15\xee\x92\x9f&\xe0l\xdc\xc3\xd3'
# app.config["BOOTSTRAP_SERVE_LOCAL"] = True
# bootstrap = Bootstrap(app)

def getOpenseaMetadata(contract_address:str, token_id:int):
    '''
    Retrieves Opensea metadata about the NFT
    '''    
    token_id = str(hex(token_id))
    r = requests.get(f"https://api.opensea.io/api/v1/metadata/{contract_address}/{token_id}?format=json")
    return json.loads(r.text)

def verifyContract(contract_address) -> str:
    '''
    Checks if contract was verified by Etherscan
    '''
    url = "https://api.etherscan.io/api"

    data = {
        "module": "contract",
        "action": "getabi",
        "address": contract_address,
        "apikey": "GTU9P9K5741Y761585SRRY38NP8I1YMC8M"
    }

    r = requests.get(url, data=data)

    if r.json()['status'] == '1':
        return 'verified'
    elif r.json()['status'] == '0':
        return 'unverified'
    

def findDuplicates(image_url):
    '''
    Future, maybe return all found links on opensea as well?
    '''
    dups_found = duplicates(image_url)
    if dups_found == 0:
        return f"No Duplicates Found. Image has {dups_found} duplicates online."
    else:
        return f"Duplicates Found! Image has {dups_found} duplicates online."


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # token_id = 0
        # contract_address="None"
        try:
            token_id = int(request.form["tokenId"])
            contract_address = request.form["contractAddress"]

        except Exception as e:
            flash('Invalid contract address or token ID', 'danger')
            return render_template('index.html')        


        if token_id and contract_address:

            try:
                NFTMetadata = getOpenseaMetadata(contract_address, token_id)

                name = NFTMetadata['name']
                image_url = NFTMetadata['image']
                description = NFTMetadata['description']

                json_data = json.dumps(NFTMetadata, indent=4, sort_keys=True)
                
                # duplicates = findDuplicates(image_url) # Maybe make async in the future

                return render_template('index.html', **locals())
            
            except Exception as e:
                print(e)
                flash(f'Invalid NFT<br>{contract_address}<br>{token_id}', 'danger')
        else:
            flash('Missing contract address or token ID', 'danger')

    return render_template('index.html')  


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
