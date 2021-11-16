#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries
import boto3, re, sys, math, json, os, sagemaker, urllib.request
from sagemaker import get_execution_role
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import Image
from IPython.display import display
from time import gmtime, strftime
from sagemaker.predictor import csv_serializer


from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img


# In[12]:


from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from PIL import Image
import s3fs

fs = s3fs.S3FileSystem()

datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

f = fs.open(f's3://<path to your image present inside the s3 bucket>.jpeg')
display(Image.open(f))
img = load_img(f)
x = img_to_array(img)


# In[13]:


display(x.shape)
x = x.reshape((1,) + x.shape)


# In[14]:


display(x.shape)


# In[15]:


# the .flow() command below generates batches of randomly transformed images
# and saves the results to the `preview/` directory
#g = fs.open(f's3://your-sage-maker-tutorial-s3-bucket/preview/', 'wb')
#display(g)
i = 0
for batch in datagen.flow(x, batch_size=1,save_to_dir='<create a directory in your jupyter notebook and provide its name here>', save_prefix='aug', save_format='jpeg'):
    i += 1
    if i > 40:
        break  # otherwise the generator would loop indefinitely

