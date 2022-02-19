#!/usr/bin/env python

from base64 import b64encode
from flask import Flask, render_template, request
# from flask_bootstrap import Bootstrap
import requests
import json


from check_image_exists_online import duplicates

# from getImageUrl import getImageUrl
from getJSON import getJSON

app = Flask(__name__)

# app.config["BOOTSTRAP_SERVE_LOCAL"] = True
# bootstrap = Bootstrap(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        
        # Retrieve NFT information from page, rename `file` later
        token_id = 0
        contract_address="None"
        try:
            token_id = int(request.form["tokenId"])
            contract_address = request.form["contractAddress"]
            
        except Exception as e:
            print(e)
            output = f"[ERROR] Not Found\
            \nContract Address: {contract_address}\
            \nToken Id: {token_id}"
            return render_template("index.html", metadata=metadata)

        # Information to send back to page
        metadata = "Picture Found." # output can be a string
        duplicate = "" # duplicate can be a string
        image_url = ""

        if token_id:
            try:
                # TODO: Check max file size of NFT? Could it crash the server?
    
                image_metadata = getJSON(contract_address, token_id) # Currently executes two requests to the network, make it one later
                image_url = image_metadata['image']
                
                # NFT Metadata
                metadata = json.dumps(image_metadata, indent=4, sort_keys=True)
                print(metadata)

            # If anything goes wrong
            except Exception as e:
                print(e)
                metadata = "[Error] Invalid NFT"
        else:
            return render_template("index.html")

        
        # Image duplicate search
        dups_found = duplicates(image_url)
        if dups_found == 0:
            duplicate = f"No Duplicates Found. Image has {dups_found} duplicates online."
        else:
            duplicate = f"Duplicates Found! Image has {dups_found} duplicates online."

        return render_template("index.html", metadata=metadata, image=image_url, duplicate=duplicate)

    elif request.method == "GET":
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
