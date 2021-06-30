#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from itri_ai_g100_tutorials.srv import * 
import rospy


from io import BytesIO

#import time, os, sys, platform, random, re
#import datetime as dt
import numpy as np
import cv2
  
#def pre_process(self,img): #by yuyun 
def handle_g100_roi(req):
    print( "Input filename:test.JPG; RIO[%d,%d,%d,%d]",req.xy[0],req.xy[1],req.xy[2],req.xy[3])
    
    #print(img)
    #img  = cv2.imread(req.a)
    img =cv2.imread(req.input_filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(req)
    outimg= img[req.xy[0]:req.xy[1],req.xy[2]:req.xy[3]]
    cv2.imwrite('output.JPG', outimg)
    return G100RoiResponse("output.JPG") 

def g100_roi_server():
    rospy.init_node('g100_roi_server') #roi_server
    s = rospy.Service('g100_roi', G100Roi, handle_g100_roi)
    print("Ready.")
    rospy.spin() #此語句保證直到節點被關閉，程式碼才會停止執行


if __name__ == "__main__":
    g100_roi_server()

