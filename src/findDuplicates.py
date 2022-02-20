# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 21:16:52 2022

@author: kkrao
"""


from serpapi import GoogleSearch
import json
import asyncio

async def findDuplicates(image_url):
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
    
    results = GoogleSearch(params).get_dict()
    image_results = results['image_results']
    links = [r['link'] for r in image_results]    
    return links
    
    
"""
def main():

    logging.getLogger().setLevel(logging.INFO)

    original = "https://raw.githubusercontent.com/andrebhu/TreeHacks2022/main/src/images/original.jpg"
    # fake = "https://raw.githubusercontent.com/andrebhu/TreeHacks2022/main/src/images/monkey.jpg"
    fake ="https://lh3.googleusercontent.com/9l0UICNfBK-bBfZ8EGbJPPC9L5MFGeJApN6IcxuKMfE4fPntsIYCE-dmZkAhJvk7kFcjUJbYY6znSS_c4t_Og59bwTpng4roMV8Vx1Y=s0"
    n_found = duplicates(fake)
    
    if n_found==0:
        logging.info("Image is original.")
    else:
        logging.info(f"Image has {n_found} duplicates online.")

if __name__ == "__main__":
    main()

"""
