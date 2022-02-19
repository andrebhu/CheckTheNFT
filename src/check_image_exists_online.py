# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 21:16:52 2022

@author: kkrao
"""


# import cv2
import requests
import json

filePath = './images/monkey.jpg'



searchTerm = 'parrot'
startIndex = '1'
key = ' Your API key here. '
cx = ' Your CSE ID:USER here. '
searchUrl = "https://www.googleapis.com/customsearch/v1?q=" + \
    searchTerm + "&start=" + startIndex + "&key=" + key + "&cx=" + cx + \
    "&searchType=image"
r = requests.get(searchUrl)
response = r.content.decode('utf-8')
result = json.loads(response)
print(searchUrl)
print(r)
print(result)



# webbrowser.get(fetchUrl)

