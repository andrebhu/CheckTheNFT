# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 14:49:52 2022

@author: kkrao
"""


import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
from torchvision import datasets, models, transforms
from torch.utils.data import DataLoader, Dataset
from PIL import Image, ImageOps
import torchvision.datasets as dset
import torchvision.transforms as T

import numpy as np

import matplotlib.pyplot as plt
import time
import os
import copy
import scipy.ndimage
import pandas as pd
import matplotlib.patches as patches
import requests
from io import BytesIO


class ImageFolderWithPaths(datasets.ImageFolder):
    """Custom dataset that includes image file paths. Extends
    torchvision.datasets.ImageFolder
    """
    
    # override the __getitem__ method. this is the method that dataloader calls
    def __getitem__(self, index):
        def remove_prefix(str, prefix):
         return str.lstrip(prefix)
        
        # this is what ImageFolder normally returns 
        original_tuple = super(ImageFolderWithPaths, self).__getitem__(index)
        # the image file path
        path = self.imgs[index][0]
        path = remove_prefix(path, 'imagenet/test/images')
        
        # make a new tuple that includes original and the path
        tuple_with_path = (original_tuple + (path,))
        return tuple_with_path
def set_parameter_requires_grad(model, feature_extracting):
    if feature_extracting:
        for param in model.parameters():
            param.requires_grad = False

def initialize_model(num_classes, width, channels, feature_extract, use_pretrained=True):
    # Initialize these variables which will be set in this if statement. Each of these
    #   variables is model specific.
    model_ft = None
    input_size = 0

             
    model_ft = models.resnet18(pretrained=use_pretrained)
    set_parameter_requires_grad(model_ft, feature_extract)
    num_ftrs = model_ft.fc.in_features
    model_ft.fc = nn.Linear(num_ftrs, num_classes)
    input_size = 224

    if(width != input_size):       
      W1 = width
      if (input_size > W1):
        F = 1
        P = int((input_size - W1) / 2)
      else:
        P = 0
        F = W1 - input_size +1
      
      first_conv_layer = nn.Conv2d(channels, 3, kernel_size=F, stride=1, padding=P, dilation=1, groups=1, bias=True)
      model_ft = nn.Sequential(first_conv_layer, model_ft)
  

    return model_ft, input_size


def predict(image_url):
    
    response = requests.get(image_url)
    im = Image.open(BytesIO(response.content))
    img = np.asarray(im)
    
    img.shape
    
    
    # Initialize the model for this run
    num_classes = 2
    width = 224
    channels = 3
    feature_extract = True
    device = torch.device('cpu')
    
    model_ft, input_size = initialize_model(num_classes, width, channels, feature_extract, use_pretrained=True)
    
    
    BATCH_SIZE = 128
    FOLDERNAME = 'imagenet/test'
    
    data_transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.CenterCrop(width),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])
        ])
    
    
    data = data_transform(img)
    data = data[None,:,:,:]
    
    model, input_size = initialize_model(num_classes, width, channels, feature_extract, use_pretrained=True)
    
    CHECKPOINT_PATH = "./nn/model.pth"
    loaded_checkpoint = torch.load(CHECKPOINT_PATH, map_location=torch.device('cpu'))
    epoch = loaded_checkpoint["epoch"]
    model_state = loaded_checkpoint["model_state"]
    
    
    model.load_state_dict(model_state)
    model.to(device)
    
    
    output_df = pd.DataFrame({'image': [], 'real': []})
    SCALE=1e7

    with torch.no_grad():
      outputs = model(data)
      _, preds = torch.max(outputs, 1)
    
    #returns 1 if not enhanced.
    # 0 otherwise.
    return preds.item()

def main():
    image_url = "https://lh3.googleusercontent.com/aoZYvjIAhmxVNfUr7-pwhCZBYzYiEoMI23DtLwpoaq_OmMLqiSdQ_gAuwJtmesuDqCdnlbeUPBtYyTdzAt_T0F0nT3pldHxgNzjp-ec=w600"

    is_real = predict(image_url)
    print(is_real)

if __name__ == '__main__':
    main()