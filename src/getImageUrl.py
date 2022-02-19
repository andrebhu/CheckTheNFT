import json

def getImageUrl(json):
    '''
    Returns URL of NFT image from JSON
    '''
    # json = getJSON(contract_address, token_id)
    for key in json.keys():
        if 'image' in key:
            return json[key]


# def retrieveImage(json):
#     '''
#     Given a contract_address and tokenId, return image encoded in base64
#     '''
#     image_url = getImageUrl(contract_address, token_id)
    
#     print(f"Getting image from {image_url}")

#     image_file = requests.get(image_url).content
#     return b64encode(image_file).decode("utf-8")
    

# print(retrieveImage('0x1b79c7832ed9358E024F9e46E9c8b6f56633691B', 51)[:50])
# retrieveImage('0x5c3Cc8D8f5C2186d07D0bd9E5b463Dca507b1708', 4599)
# retrieveImage('0x5c1a0cc6dadf4d0fb31425461df35ba80fcbc110', 3778)

