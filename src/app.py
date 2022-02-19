#!/usr/bin/env python

from base64 import b64encode
from flask import Flask, render_template, request
# from flask_bootstrap import Bootstrap
import requests

from retrieveImage import retrieveImage

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
            return render_template("index.html", output=output)

        # Information to send back to page
        output = "Picture Found." # output can be a string
        image = "" # image should be returned as a b64 encoded string

        if token_id:
            try:
                # TODO: Check max file size of NFT? Could it crash the server?
                # TODO: Function that retrieves image from NFT token

                # just returns input
                # output = f"{token_id}"

                image = retrieveImage(contract_address, token_id)

                # b64 encode file to pass back to page
                # image = b64encode(file).decode("utf-8")

            # If anything goes wrong
            except Exception as e:
                print(e)
                output = "[Error] Invalid NFT"
        else:
            return render_template("index.html")

        print(image[:50])
        return render_template("index.html", output=output, image=image)

    elif request.method == "GET":
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
