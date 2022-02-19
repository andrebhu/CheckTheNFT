# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 01:24:08 2022

@author: kkrao
"""

import os
import PIL
import numpy as np
import scipy.ndimage

def augment_images(directory=None, factor = 10):
    filenames = os.listdir(directory)
    for filename in filenames:
        if os.path.splitext(filename)[1] == ".jpg":
            print(filename)
            im = PIL.Image.open(os.path.join(directory,filename))
            size= im.size
            new_size = (int(size[0]/factor), int(size[1]/factor))
            im = im.resize(new_size, PIL.Image.ANTIALIAS)
            im = im.resize(size, PIL.Image.ANTIALIAS)
            
            new_filename = os.path.splitext(filename)[0]+'_%s.jpg'%factor
            im.save(os.path.join("./images/",new_filename))


directory = "./images/"
augment_images(directory)