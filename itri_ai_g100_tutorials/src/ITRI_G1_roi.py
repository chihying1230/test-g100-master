#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from io import BytesIO

#import time, os, sys, platform, random, re
#import datetime as dt
import numpy as np
import cv2
  

#def pre_process(self,img): #by yuyun 
def pre_process(img, roi):
    #print(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img[roi[0]:roi[1],roi[2]:roi[3]]
    #return img[self.roi[0]:self.roi[1],self.roi[2]:self.roi[3]]
    
#def post_process(self, receive, height, width):   #by yuyun
def post_process( roi, receive, height, width):#by yuyun
    merge_img = np.zeros([height, width])
    #print(self.roi, receive.shape)
    #merge_img[self.roi[0]:self.roi[1],self.roi[2]:self.roi[3]] = receive
    merge_img[roi[0]:roi[1],roi[2]:roi[3]] = receive#by yuyun
    return merge_img
