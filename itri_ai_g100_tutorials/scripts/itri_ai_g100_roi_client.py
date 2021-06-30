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
import matplotlib.pyplot as plt 

def g100_roi_client(input_img, y_begin, y_end, x_begin, x_end):
    rospy.wait_for_service('g100_roi')  
    try:
        g100_roi = rospy.ServiceProxy('g100_roi', G100Roi)
        xy = [y_begin,y_end,x_begin,x_end]
        resp = g100_roi('test.JPG', xy)
        return resp.output_filename
    except rospy.ServiceException(e):
        print("Service call failed: %s",e)

def usage():
    return "%s: Input_Image_Filename [y_begin, y_end, x_begin, x_end]"%sys.argv[0] 

if __name__ == "__main__":
    if len(sys.argv) == 6:
        input_img = str(sys.argv[1])
        y_begin   = int(sys.argv[2])
        y_end     = int(sys.argv[3])
        x_begin   = int(sys.argv[4])
        x_end     = int(sys.argv[5])
         
    else:
        print( usage())
        sys.exit(1)

    print ("ROI Processing...%s [%d,%d,%d,%d]",input_img, y_begin, y_end, x_begin, x_end)
    image_output_filename = g100_roi_client(str(input_img), int(y_begin), int(y_end), int(x_begin), int(x_end))
    img_input = cv2.imread(input_img)
    img_output = cv2.imread(image_output_filename)
    # show result
    plt.subplot(1,3,1)
    plt.imshow(img_input, vmin=0, vmax=255)
    plt.plot([y_begin]*2, [x_begin,x_end], color="r")
    plt.plot([y_end]*2, [x_begin,x_end], color="r")
    plt.plot([y_begin,y_end], [x_begin]*2, color="r")
    plt.plot([y_begin,y_end], [x_end]*2, color="r")
    plt.title("Original")
    plt.axis("off")
    plt.subplot(1,3,2)
    plt.imshow(img_output, cmap="gray", vmin=0, vmax=255)
    plt.title("ROI")
    plt.axis("off")
    plt.show()
