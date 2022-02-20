#!/usr/bin/env python

from threading import Thread
from flask import Flask, render_template, request, flash, url_for, redirect
import requests
import json
import warnings
from serpapi import GoogleSearch
from nn.check_if_real import predict
from time import time

warnings.filterwarnings('ignore')

app = Flask(__name__)
app.config['SECRET_KEY'] = b'\xa7\xd8\x89JB\xa9sj\x05\x03S\x1a\x83\xb3\x15\xee\x92\x9f&\xe0l\xdc\xc3\xd3'


def getOpenseaMetadata(contract_address:str, token_id:int):
    """
    Retrieves Opensea metadata about the NFT
    """
    token_id = str(hex(token_id))
    r = requests.get(f"https://api.opensea.io/api/v1/metadata/{contract_address}/{token_id}?format=json")
    return json.loads(r.text)


def verifyContract(contract_address) -> str:
    """
    Checks if contract was verified by Etherscan
    """
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
    """
    Url of the image for which you want to check if a duplicate exists
    """
    params = {
      "engine": "google_reverse_image",
      "image_url": image_url,
      "api_key": "cecf4cdc7fbbcf37ba6c3bf17a7d025894988aca8c4e41be585d23991ec5f7db"
    }

    results = GoogleSearch(params).get_dict()
    n_found = results['search_information']['total_results'] 
    print("Finished findDuplicates")

    image_results = results['image_results']
    links = [r['link'] for r in image_results]    
    return links


def checkEnhance(image_url):
    """
    Use `nn` models to detect whether an image may have been enhanced or not
    """

    enhanced = predict(image_url)

    if enhanced:
        return "Image not manipulated"
    else:
        return "Image manipulations found"


# Thread functions
def getEnhanceOutput(image_url, result, index):
    result[index] = checkEnhance(image_url)

def getDuplicatesOutput(image_url, result, index):
    result[index] = findDuplicates(image_url)



# Application routes
@app.route("/opensea", methods=["GET"])
def opensea():
    try:
        url = request.args.get('url')
        if url:
            print(url)
            if 'https://opensea.io/assets/' in url:
                contract_address, token_id = url.split('0x')[1].split("/")
                return redirect(f'/?contract=0x{contract_address}&token={token_id}')
        else:
            print(f"No url? {url}")
            return redirect(url_for('index'))

    except Exception as e:
        print(e)
        return redirect(url_for('index'))



@app.route("/", methods=["GET"])
def index():
    start = time() # Analyzing performance

    token_id = request.args.get('token')
    contract_address = request.args.get('contract')


    if token_id and contract_address:
        try:
        
            NFTMetadata = getOpenseaMetadata(contract_address, int(token_id))
            
            name = f"<a target=\"_blank\" rel=\"noopener noreferrer\" href=\"https://opensea.io/assets/{contract_address}/{token_id}\">{NFTMetadata['name']}</a>"

            image_url = NFTMetadata['image']
            description = NFTMetadata['description']                
            
            # TODO: Make bottom two async
            # duplicates_links = findDuplicates(image_url)

            # enhance_msg, duplicates_links = asyncio.run(processImage(image_url))            

            messages = [None] * 2

            duplicates_thread = Thread(target=getDuplicatesOutput, args=(image_url, messages, 0))
            enhance_thread = Thread(target=getEnhanceOutput, args=(image_url, messages, 1))
            
            duplicates_thread.start()
            enhance_thread.start()

            duplicates_thread.join()
            enhance_thread.join()
            
            duplicates_msg = f"We have found {len(messages[0])} similar results"
            enhance_msg = messages[1]

            # enhance_msg = checkEnhance(image_url)
            # enhance_msg = "This image may be enhanced"

            verify = f"NFT's <a target=\"_blank\" rel=\"noopener noreferrer\" href=\"https://etherscan.io/address/{contract_address}\">contract</a> is {verifyContract(contract_address)}"
            
            end = time() # Analyzing performance
            time_elapsed = "{:.2f}s".format(end - start)

            # return render_template('index.html', **locals())
            return {"duplicates": max(len(messages[0])-2, 0),
                    "enhance": enhance_msg,
                    "verify": verify
                    }
        
        except Exception as e:
            print(e)
            flash(f'Invalid contract or token', 'danger')

    return render_template('index.html')  


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", threaded=True)
