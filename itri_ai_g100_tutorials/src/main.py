import cv2
import numpy as np
import matplotlib.pyplot as plt

from ITRI_G1_roi import pre_process
from ITRI_G1_thinning import thin

if __name__ == "__main__":
    # load image
    img = cv2.imread("test.JPG")
    
    # define ROI
    roi = [20,120,20,120] #[y_begin, y_end, x_begin, x_end]
    roi_img = pre_process(img, roi)
    
    #thinning
    thinning_result = thin(roi_img, 90)
   
    # show result
    plt.subplot(1,3,1)
    plt.imshow(img, vmin=0, vmax=255)
    plt.plot([roi[0]]*2, [roi[2],roi[3]], color="r")
    plt.plot([roi[1]]*2, [roi[2],roi[3]], color="r")
    plt.plot([roi[0],roi[1]], [roi[2]]*2, color="r")
    plt.plot([roi[0],roi[1]], [roi[3]]*2, color="r")
    plt.title("Original")
    plt.axis("off")
    plt.subplot(1,3,2)
    plt.imshow(roi_img, cmap="gray", vmin=0, vmax=255)
    plt.title("ROI")
    plt.axis("off")
    plt.subplot(1,3,3)
    plt.imshow(thinning_result, cmap="gray")
    plt.title("Thinning")
    plt.axis("off")
    plt.show()


