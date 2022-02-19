# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 21:16:52 2022

@author: kkrao
"""

from serpapi import GoogleSearch
import json

def findDuplicates(image_url):
    """
    image_url : url of the image for which you want to check if a duplicate exists

    Returns
        1 if original
        0 if duplicate/coutnerfeit

    """
    params = {
      "engine": "google_reverse_image",
      "image_url": image_url,
      "api_key": "cecf4cdc7fbbcf37ba6c3bf17a7d025894988aca8c4e41be585d23991ec5f7db",
    }
    
    search = GoogleSearch(params)
    results = search.get_dict()
    image_results = results['image_results']

    links = [r['link'] for r in image_results]

    
    # for result in image_results:
    #     # print(result['link'])
    #     if 'opensea.io' in result['link']:
    #         dupCount += 1

    # return dupCount
    print(len(links))
    print(links)


findDuplicates("https://lh3.googleusercontent.com/lvT5NVKfuYs98D0vReydoXqPmYqvVvgvvD-5oSSzil6p4EPPiQAFOf5hb7P2ytJRawl2fWXjKtko2J981yGwp13_-qVi36rs_5rM")