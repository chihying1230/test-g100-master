#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ROS step01. 要引用rospy這個模組，就可以使用 ros client API啦!
import rospy


from io import BytesIO

#import time, os, sys, platform, random, re
#import datetime as dt
import numpy as np
import cv2
  

# ROS step02. 接著初始化一個新的node
rospy.init_node('itri_ai_g100_roi_node')
# ROS step02. 新增完node了以後，使用loginfo印出資訊
rospy.loginfo('itri_ai_g100_roi_node --- init ok!')


#def pre_process(self,img): #by yuyun 
def pre_process(img, roi):
    #print(img)
    rospy.loginfo("cv2.cvtColor src type(img)=",type(img))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rospy.loginfo("cv2.cvtColor return type(img)=",type(img))
    return img[roi[0]:roi[1],roi[2]:roi[3]]
    #return img[self.roi[0]:self.roi[1],self.roi[2]:self.roi[3]]
