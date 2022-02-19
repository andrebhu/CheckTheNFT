# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 21:16:52 2022

@author: kkrao
"""

import logging

from serpapi import GoogleSearch


def duplicates(image_url):
    """
    image_url : url of the image for which you want to check if a duplicate exists

    Returns
        1 if original
        0 if duplicate/coutnerfeit

    """
    params = {
      "engine": "google_reverse_image",
      "image_url": image_url,
      "api_key": "cecf4cdc7fbbcf37ba6c3bf17a7d025894988aca8c4e41be585d23991ec5f7db"
    }
    
    search = GoogleSearch(params)
    results = search.get_dict()
    n_found = results['search_information']['total_results']

    #-2 because uploading to github raw counts as twice 
    return n_found-2 
    

def main():
    logging.getLogger().setLevel(logging.INFO)

    original = "https://raw.githubusercontent.com/andrebhu/TreeHacks2022/main/src/images/original.jpg"
    fake = "https://raw.githubusercontent.com/andrebhu/TreeHacks2022/main/src/images/monkey.jpg"
    n_found = duplicates(fake)
    
    if n_found==0:
        logging.info("Image is original.")
    else:
        logging.info(f"Image has {n_found} duplicates online.")

if __name__ == "__main__":
    main()


