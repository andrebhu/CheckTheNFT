#!/usr/bin/env python

from base64 import b64encode
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)

app.config["BOOTSTRAP_SERVE_LOCAL"] = True
bootstrap = Bootstrap(app)


def retrieveImage(tokenId):
    '''
    Given a tokenId, return corresponding image
    '''

    return


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        
        # Retrieve NFT information from page, rename `file` later
        tokenId = request.form["tokenId"]

        # Information to send back to page
        output = "" # output can be a string
        image = "" # image should be returned as a b64 encoded string

        if tokenId:
            try:
                # TODO: Check max file size of NFT? Could it crash the server?
                # TODO: Function that retrieves image from NFT token

                # just returns input
                output = f"{tokenId}"

                retrieveImage(output)

                # b64 encode file to pass back to page
                # image = b64encode(file).decode("utf-8")

            # If anything goes wrong
            except:
                output = "Invalid NFT"
        else:
            return render_template("index.html")

        return render_template("index.html", output=output, image=image)

    elif request.method == "GET":
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
